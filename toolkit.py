# My Python Toolkit
# Three simple tools for everyday tasks

# Store formatted names in a list while the program runs
saved_names = []

# Welcome the user to the toolkit
print("Welcome to My Python Toolkit!")
print("Choose a tool and let's get started!")

# Keep displaying the menu until the user chooses Quit
while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. Even or Odd Checker")
    print("3. Name Formatter")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ").strip()

    # Tool 1: Add two numbers and display their sum
    if choice == "1":
        print("\nSimple Calculator")
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            total = number1 + number2
            print(f"The sum of {number1:g} and {number2:g} is {total:g}.")
        except ValueError:
            print("Please enter valid numbers. Try again!")

    # Tool 2: Check whether a whole number is even or odd
    elif choice == "2":
        print("\nEven or Odd Checker")
        try:
            number = int(input("Enter a whole number: "))

            if number % 2 == 0:
                print(f"Great! {number} is an even number.")
            else:
                print(f"Great! {number} is an odd number.")

        except ValueError:
            print("Please enter a valid whole number.")

    # Tool 3: Format names and add them to a changing list
    elif choice == "3":
        print("\nName Formatter")
        print("Enter names one by one.")
        print("Press Enter without typing a name to finish.")

        while True:
            name = input("Enter a name: ").strip()

            if name == "":
                break

            formatted_name = name.title()
            saved_names.append(formatted_name)
            print(f"Name saved successfully: {formatted_name}")

        if saved_names:
            print("\nYour saved names:")
            for saved_name in saved_names:
                print(f"- {saved_name}")
        else:
            print("No names have been saved yet.")

        print(f"You have saved {len(saved_names)} name(s).")

    # Quit the toolkit and end the menu loop
    elif choice == "4":
        print("Thank you for using My Python Toolkit. Goodbye!")
        break

    # Handle choices that are not on the menu
    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please select 1, 2, 3, or 4.")