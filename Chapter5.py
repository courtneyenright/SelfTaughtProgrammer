#Chapter 5 Challenges

#Challenge 1

my_fav_musicians = ["Ripe", "Tiesto", "Rebelution"]
print(my_fav_musicians)

#Challenge 2

my_fav_places = [("0023342", "-23434323"), ("23456323", "32343232"), ("234233", "23554354")]
print(my_fav_places)

#Challenge 3

my_attributes = {"height": "5'7", "fav color": "pink", "fav author": "Brandon Sanderson"}

#Challenge 4

question = input("""What do you want to know about Courtney?
Type height,
Type fav color,
or Type fav author: """)

if question in my_attributes:
    print(my_attributes[question])
else:
    print("Sorry did not understand question")


#Challenge 5
musician_song_dict = {my_fav_musicians[0]: "Noice in the Forest", my_fav_musicians[1]: "That one song", my_fav_musicians[2]: "Inhale Exhale"}

print(musician_song_dict)


#Challenge 6

"""
Python sets are used to store collections of data. A set is a collection which is unordered, unchangeable, and unindexed. But you can add new items and remove items.
Sets can be highly useful for unions, intersections, differences, and symmetric difference.

my_list = []
my_tuple = ()
my_dictionary = {}
"""
