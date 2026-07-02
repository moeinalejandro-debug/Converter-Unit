# conversions

def m_km(number):
    return number / 1000

def km_m(number):
    return number * 1000

def mile_km(number):
    return number * 1.60934

def km_mile(number):
    return number / 1.60934

def cm_mm(number):
    return number * 10

def mm_cm(number):
    return number / 10


# dictionary mapping

lenght_conversions = {
    "1": ("CM --> KM", m_km, "M"),
    "2": ("KM --> CM", km_m, "KM"),
    "3": ("Mile --> KM", mile_km, "Mile"),
    "4": ("KM --> Mile", km_mile, "KM"),
    "5": ("CM --> MM", cm_mm, "CM"),
    "6": ("MM --> CM", mm_cm, "MM")
}


# menu

def length_menu():
    print("\n===== Length Converter =====")

    for key, value in lenght_conversions.items():
        print(f"{key}. {value[0]}")

    choice = input("\nChoose (1-6): ").strip()

    if choice in lenght_conversions:
        title, func, unit = lenght_conversions[choice]

        try:
            value = float(input(f"{unit}: "))
            result = func(value)

            print(f"{title} --> {result}")

        except ValueError:
            print("Please enter a valid number!")

    else:
        print("Invalid choice!")