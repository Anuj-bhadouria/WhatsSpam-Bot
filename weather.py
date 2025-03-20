# Weather data dictionary
weather_data = {
    "Monday": 25,
    "Tuesday": 28,
    "Wednesday": 22,
    "Thursday": 30,
    "Friday": 27,
    "Saturday": 26,
    "Sunday": 24
}

# Calculate and display the average temperature
avg_temp = sum(weather_data.values()) / len(weather_data)
print(f"Average temperature for the week: {avg_temp:.2f}°C")

# Find and display the highest and lowest temperature days
highest_day = max(weather_data, key=weather_data.get)
lowest_day = min(weather_data, key=weather_data.get)

print(f"Highest temperature: {weather_data[highest_day]}°C on {highest_day}")
print(f"Lowest temperature: {weather_data[lowest_day]}°C on {lowest_day}")

# Loop for user input
while True:
    day = input("\nEnter a day to check the temperature (or 'exit' to quit): ").strip().title()
    
    if day.lower() == "exit":
        print("Goodbye!")
        break

    if day in weather_data:
        print(f"Temperature on {day}: {weather_data[day]}°C")
    else:
        print("Invalid day. Please enter a valid day (e.g., Monday, Tuesday, etc.).")
