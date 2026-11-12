# [] create Element_Quiz

from urllib.request import urlretrieve


def get_names():
    responses = []

    while len(responses) < 5:
        name = input("Enter the name of an element: ").strip().lower()

        if name == "":
            print("Please enter a name.")

        elif name in responses:
            print(name, "was already entered")

        else:
            responses.append(name)

    return responses


url = "https://raw.githubusercontent.com/MicrosoftLearning/introPython/master/elements1_20.txt"
urlretrieve(url, "elements1_20.txt")


elements_file = open("elements1_20.txt", "r", encoding="utf-8")

elements = []
line = elements_file.readline()

while line != "":
    elements.append(line.strip().lower())
    line = elements_file.readline()

elements_file.close()


print("Welcome Soraja Omanovic! List any 5 of the first 20 elements in the Periodic Table.")

responses = get_names()


correct = []
incorrect = []

for response in responses:
    if response in elements:
        correct.append(response.title())
    else:
        incorrect.append(response.title())


score = len(correct) * 20


print()
print(score, "% correct")
print("Found:", " ".join(correct))
print("Not Found:", " ".join(incorrect))

