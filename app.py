import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)




# for index, item in enumerate(data):
#     print(index, ":", item["title"])

Year_input = int(input ("Would you like to see movies after a certain year? If yes, enter a certain year. If not please just enter. 'No'"))

for i in data:
    if i['year'] > Year_input:
        print(i["title"])

    