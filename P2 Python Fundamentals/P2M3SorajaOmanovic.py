# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  

# P2M3: Module 3 Required Coding Activity
# Program: Poem Mixer

# Create the word_mixer function
def word_mixer(word_list):

    word_list.sort()
    new_words = []

    while len(word_list) > 5:
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())

    return new_words


# Get user input
poem = input("Welcome Soraja Omanovic! Enter a saying or poem: ")

# Split the poem into a list of words
words_list = poem.split()

# Find the length of the list
list_length = len(words_list)

# Change words to lowercase or uppercase
for index in range(list_length):

    if len(words_list[index]) <= 3:
        words_list[index] = words_list[index].lower()

    elif len(words_list[index]) >= 7:
        words_list[index] = words_list[index].upper()

# Call the word_mixer function
mixed_words = word_mixer(words_list)

# Print the mixed poem
for word in mixed_words:
    print(word, end=" ")

print()

