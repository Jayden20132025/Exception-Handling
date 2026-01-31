age = input("Enter your age: ")

# Check if the input is an integer
if age.isdigit():
    age = int(age)

    # Check odd or even
    if age % 2 == 0:
        print("The age is EVEN.")
    else:
        print("The age is ODD.")

else:
    print("Error: Please enter a valid whole number for age.")
