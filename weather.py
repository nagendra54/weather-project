import requests

# ✅ Replace this with your actual API key
API_KEY = 'e8bdd11e291d7bcec44c5bf8007bde28'

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code != 200:
            return f"❌ Could not find weather for '{city.title()}'. Please check the city name."

        weather = data["main"]
        weather_desc = data["weather"][0]["description"].capitalize()
        temperature = weather["temp"]
        humidity = weather["humidity"]

        return (
            f"📍 Weather in {city.title()}:\n"
            f"🌤️ Condition: {weather_desc}\n"
            f"🌡️ Temperature: {temperature}°C\n"
            f"💧 Humidity: {humidity}%"
        )

    except Exception as e:
        return f"⚠️ Error: {e}"

def chatbot():
    print("🤖 Hello! I am your Weather Chatbot. Type 'exit' to quit.")
    print("📌 You can ask like: weather in Mumbai")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("👋 Goodbye! Stay safe!")
            break

        if 'weather in' in user_input.lower():
            city = user_input.lower().split('weather in')[-1].strip()
            if city:
                weather_info = get_weather(city)
                print("Bot:", weather_info)
            else:
                print("Bot: Please specify a city name.")
        else:
            print("Bot: I can only provide weather updates. Please use: weather in <city>")

if __name__ == "__main__":
    chatbot()
