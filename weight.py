# conversions 

def g_kg(number) :
    return number / 1000

def kg_g(number) :
    return number * 1000

def kg_lb(number) :
    return number * 2.20462

def lb_kg(number) :
    return number / 2.20462


# dictionary mapping

weight_conversions = {
    "1" : ("Gram --> Kilogram" , g_kg , "G") ,
    "2": ("Kilogram --> Gram", kg_g, "KG"),
    "3": ("Kilogram --> Pound", kg_lb, "KG"),
    "4": ("Pound --> Kilogram", lb_kg, "Pound")
}

def weight_menu():
    print("\n===== Weight Converter =====")

    for key, value in weight_conversions.items():
        print(f"{key}. {value[0]}")

    choice = input("\nChoose (1-4): ").strip()

    if choice in weight_conversions:
        title, func, unit = weight_conversions[choice]

        try:
            value = float(input(f"{unit}: "))
            result = func(value)

            print(f"{title} --> {result}")

        except ValueError:
            print("Please enter a valid number!")

    else:
        print("Invalid choice!")