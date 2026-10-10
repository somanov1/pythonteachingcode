# [ ] create, call and test the adding_report() function

def adding_report(report="T"):
    total = 0
    items = ""

    print('Input an integer to add to the total or "Q" to quit')

    while True:
        user_input = input('Enter an integer or "Q": ')

        if user_input.isdigit():
            number = int(user_input)
            total = total + number

            if report == "A":
                items = items + user_input + "\n"

        else:
            if user_input.upper().startswith("Q"):

                if report == "A":
                    print()
                    print("Items")
                    print(items)

                print("Total")
                print(total)
                print("Calculated by: Soraja Omanovic")
                break

            else:
                print(user_input + " is invalid input")


adding_report("A")
adding_report("T")