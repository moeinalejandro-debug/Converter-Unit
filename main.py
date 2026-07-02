from length import length_menu
from weight import weight_menu
from temperature import temperature_menu


def main():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Exit")

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            length_menu()

        elif choice == "2":
            weight_menu()

        elif choice == "3":
            temperature_menu()

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()