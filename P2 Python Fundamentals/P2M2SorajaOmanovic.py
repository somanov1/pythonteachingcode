# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 

# P2M2: Module 2 Required Coding Activity
# Program: List-o-matic

# Create the list-o-matic function
def list_o_matic(item, items):

    if item == "":
        removed_item = items.pop()
        return removed_item + " popped from list"

    elif item in items:
        items.remove(item)
        return "1 instance of " + item + " removed from list"

    else:
        items.append(item)
        return "1 instance of " + item + " appended to list"


# Create a list of animals
animals = ["cat", "goat", "cat"]

# Run the program while the list is not empty
while animals:

    print("Welcome, Soraja Omanovic. Look at all the animals", animals)

    # Get user input
    user_input = input("enter the name of an animal: ")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        break

    # Call the function and print the result
    message = list_o_matic(user_input, animals)
    print(message)

# End the program
print("Goodbye!")
