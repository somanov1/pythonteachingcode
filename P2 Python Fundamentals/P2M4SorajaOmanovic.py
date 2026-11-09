# [] create The Weather

from urllib.request import urlretrieve

url = "https://raw.githubusercontent.com/MicrosoftLearning/IntroPython/master/world_temp_mean.csv"
urlretrieve(url, "mean_temp.txt")

mean_temps = open("mean_temp.txt", "a+", encoding="utf-8")
mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")

mean_temps.seek(0)
headings = mean_temps.readline().strip().split(",")

print("Soraja Omanovic")

city_temp = mean_temps.readline()
while city_temp != "":
    city_data = city_temp.strip().split(",")
    if len(city_data) >= 3:
        print(headings[0].capitalize(), "of", city_data[0],
              headings[2], "is", city_data[2], "Celsius")
    city_temp = mean_temps.readline()

mean_temps.close()