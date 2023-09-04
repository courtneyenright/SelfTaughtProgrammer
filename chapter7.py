#Challenge 1

tvShows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for shows in tvShows:
    print(shows)

#Challenge 2

for i in range (25,51):
    print(i)


#Challenge 3

for i, shows in enumerate(tvShows):
    print(i)
    print(shows)

#Challenge 4


numList = [1, 2, 3, 4, 5]
while True:
    x = input("Type 'q' to quit, or guess a number: ")
    if x == "q":
        break
    try:
        y = int(x)
    except ValueError:
        print("please type a number")
        continue
    if y in numList:
        print("Nice!")
    else:
        print("Try Again!")

#Challenge 5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiplied = []

for x in list1:
    for y in list2:
        multiplied.append(x*y)

print (multiplied)
