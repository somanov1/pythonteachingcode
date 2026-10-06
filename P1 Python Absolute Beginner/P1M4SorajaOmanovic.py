# [ ] create, call and test the str_analysis() function  

def str_analysis(test_string):
    if test_string.isdigit():
        number = int(test_string)

        if number > 99:
            return test_string + " is a pretty big number"
        else:
            return test_string + " is a smaller number than expected"

    else:
        if test_string.isalpha():
            return '"' + test_string + '" is all alphabetical characters!'
        else:
            return '"' + test_string + '" has multiple character types'


user_input = ""

while user_input == "":
    user_input = input("Soraja Omanovic, enter word or integer: ")

print(str_analysis(user_input))


