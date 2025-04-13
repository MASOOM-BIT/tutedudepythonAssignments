# Step 1: Write user input to a file
with open("output.txt", "w") as file:
    user_input = input("Enter text to write to the file: ")
    file.write(user_input + "\n")

# Step 2: Append additional data to the same file
with open("output.txt", "a") as file:
    additional_input = input("Enter additional text to append to the file: ")
    file.write(additional_input + "\n")

# Step 3: Read and display the final content of the file
with open("output.txt", "r") as file:
    print("\nFinal content of the file:")
    print(file.read())