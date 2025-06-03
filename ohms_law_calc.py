from colorama import init, Fore, Style

# Initialize colorama
init()

def ohms_law_calculator():
    print(Fore.CYAN + Style.BRIGHT + r"""
   ____ _                      _                  _               
  / ___| |__   ___  _ __   ___| |_ _ __ ___   ___| |__   ___ _ __ 
 | |   | '_ \ / _ \| '_ \ / __| __| '__/ _ \ / __| '_ \ / _ \ '__|
 | |___| | | | (_) | | | | (__| |_| | | (_) | (__| | | |  __/ |   
  \____|_| |_|\___/|_| |_|\___|\__|_|  \___/ \___|_| |_|\___|_|
  
    """)
    print(Style.RESET_ALL)

# Ask what to calculate
while True:
    print("\nWhat would you like to calculate?")
    print("Type V for Voltage, I for Current, or R for Resistance.")
    choice = input("Your choice: ").upper()

    try:
        if choice == "V":
            current = float(input("Enter current (in amps): "))
            resistance = float(input("Enter resistance (in ohms): "))
            voltage = current * resistance
            print(f"Voltage is {round(voltage, 2)} volts (V)")

        elif choice == "I":
            voltage = float(input("Enter voltage (in volts): "))
            resistance = float(input("Enter resistance (in ohms): "))
            current = voltage / resistance
            print(f"Current is {round(current, 2)} amps (A)")

        elif choice == "R":
            voltage = float(input("Enter voltage (in volts): "))
            current = float(input("Enter current (in amps): "))
            resistance = voltage / current
            print(f"Resistance is {round(resistance, 2)} ohms (Ω)")

        else:
            print("Invalid choice. Please run the program again and choose V, I, or R.")

    except ValueError:
        print("⚠️ Please enter numeric values only.")
    except ZeroDivisionError:
        print("⚠️ Division by zero is not allowed.")

    again = input("\nDo you want to make another calculation? (y/n): ").lower()
    if again != 'y':
        print("Thanks for using the Ohm's Law Calculator. Goodbye!")
        break

#Run the calculator
ohms_law_calculator()
    
