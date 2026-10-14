# [] create words after "G" following the Assignment requirements use of functions, methods and keyowrds
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)

def words_after_g():
    quote = input("Welcome Soraja Omanovic! Enter a 1 sentence quote, non-alpha separate words: ")
    word = ""

    for char in quote + " ":
        if char.isalpha():
            word += char
        else:
            if word != "":
                if word[0].lower() > "g":
                    print(word.upper())
            word = ""

words_after_g()