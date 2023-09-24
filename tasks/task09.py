def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


if __name__ == '__main__':
    while True:
        print("Choose an operation:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Select an operation (1/2/3): ")

        if choice == '3':
            print("Thank you for using the program.")
            break

        if choice not in ('1', '2'):
            print("Invalid operation choice")
            continue

        temperature = float(input("Enter the temperature: "))

        if choice == '1':
            converted_temperature = celsius_to_fahrenheit(temperature)
            print(f"{temperature} degrees Celsius is equal to {converted_temperature} degrees Fahrenheit")
        elif choice == '2':
            converted_temperature = fahrenheit_to_celsius(temperature)
            print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature} degrees Celsius")