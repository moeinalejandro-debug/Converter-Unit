# conversions 

def c_f(c):
    return (c * 9/5) + 32

def f_c(f):
    return (f - 32) * 5/9

def c_k(c):
    return c + 273.15

def k_c(k):
    return k - 273.15

def f_k(f):
    return (f - 32) * 5/9 + 273.15

def k_f(k):
    return (k - 273.15) * 9/5 + 32


# dictionary mapping 

temp_conversions = {
    "1": ("Celsius --> Fahrenheit", c_f, "°C"),
    "2": ("Fahrenheit --> Celsius", f_c, "°F"),
    "3": ("Celsius --> Kelvin", c_k, "°C"),
    "4": ("Kelvin --> Celsius", k_c, "K"),
    "5": ("Fahrenheit --> Kelvin", f_k, "°F"),
    "6": ("Kelvin --> Fahrenheit", k_f, "K")
}


# menu

def temperature_menu():
    print("\n===== Temperature Converter =====")

    for key, value in temp_conversions.items():
        print(f"{key}. {value[0]}")

    choice = input("\nChoose (1-6): ").strip()

    if choice in temp_conversions:
        title, func, unit = temp_conversions[choice]

        try:
            value = float(input(f"{unit}: "))
            result = func(value)

            print(f"{title} --> {result:.2f}")

        except ValueError:
            print("Please enter a valid number!")

    else:
        print("Invalid choice!")