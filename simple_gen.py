# Strong Password Generator Mini Project
import random  # Used to select random characters

# Define the pool of characters: lowercase, uppercase, digits, and special symbols
characters_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# Program Greeting
print("====================================================")
print("         Welcome to the Strong Password Generator   ")
print("====================================================")
print("This tool helps you generate a secure password using letters, numbers, and symbols.\n")

# Infinite loop to keep the program running until the user chooses to exit
while True:
    print("\nChoose an option:")
    print("1. Create a new password")
    print("2. Exit the program\n")

    try:
        user_option = int(input("Enter your option (1 or 2): "))

        if user_option == 1:
            try:
                # Ask user for desired password length
                password_length = int(input("Enter desired password length: "))

                # Initialize an empty string to store the password
                generated_password = ""

                # Generate password by randomly selecting characters from the pool
                for i in range(password_length):
                    generated_password += random.choice(characters_pool)

                # Display the final password
                print("\nYour generated strong password is:")
                print(generated_password)

            except ValueError:
                # Handle invalid (non-integer) input for password length
                print("Invalid input. Please enter a valid number for password length.")

        elif user_option == 2:
            # Exit message
            print("\nThank you for using the Password Generator.")
            print("Program closed.")
            break

        else:
            # Handle if user enters option other than 1 or 2
            print("Please enter a valid option (1 or 2).")

    except ValueError:
        # Handle non-integer input for menu options
        print("Invalid input. Please enter 1 or 2.")
