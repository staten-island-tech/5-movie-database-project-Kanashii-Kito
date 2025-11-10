import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)


'''----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----DO NOT TOUCH THINGS ABOVE----'''




# File One

# for index, item in enumerate(data):
#     print(index, ":", item["title"])



# File Two

# Year_input = int(input ("Would you like to see movies after a certain year? If yes, enter a certain year:  "))
# for i in data:
#     if i['year'] > Year_input:
#         print(i["title"])



# File Three
# Year_input = int(input ("Would you like to see movies after a certain year? If yes, enter a certain year:  "))
# for i in data:
#     if i['year'] > Year_input < i['year']:
#         print(i["title"])



# File Four
# Year_input = int(input ("Would you like to see movies after a certain year? If yes, enter a certain year:  "))
# for i in data:
#     if i['year'] == Year_input:
#         print(i["title"])



# File Five
# Choice_Input = (input ("Search:  "))
# Counter = 0
# for i in data:
#     if Choice_Input.lower() in i['title'].lower():
#         print(i["title"])
#         Counter += 1
# if Counter == 0:
#     print ("Sorry but not matches were found with that word.")



# File Six

# for index, item in enumerate(data):
#     print(index, ":", item["genres"])


# Choice_Input = (input ("Search:  "))
# Counter = 0
# for i in data:
#     if Choice_Input.capitalize() in i['genres']:
#         print(i["title"])
#         Counter += 1
# if Counter == 0:
#     print ("Sorry but not matches were found with that word.")