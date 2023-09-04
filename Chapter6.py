#Chapter 6 Challenged

#Challenge 1
Word = "Camus"
x = int(len(Word))
i = 0
for i in range(x):
    print(Word[i])
    x += 1

#Challenge 2
str1 = input("Please input a noun 1:")
str2 = input("Please input a noun 2:" )
newstr = "Yesterday I wrote a {}. I sent it to {}!".format(str1, str2)
print(newstr)

#Challenge 3
print("aldous Huxley was born in 1894".capitalize())

#Challenge 4
newlist = "Where now? Who now? When now?".split("? ")
newlist = [newlist[0] + "?", newlist[1] + "?", newlist[2]]
print(newlist)

#Challenge 5
list5 = ["The", "fox", "jumped", "over", "the","fence","."]
list5 = " ".join(list5)
list5 = list5.replace(" .", ".")
print(list5)

#Challenge 6
saying = "A screaming coes across the sky".replace("s", "$")
print(saying)

#Challenge 7
findm = "Hemingway".index("m")
print(findm)

#Challenge 8
str3 = 'Logan once said to me "Sometimes, things just work out for me."'
print(str3)

#Challenge 9
print("three "*3)
print("three " + "three " + "three")

#Challenge 10
str10 = "It was a bright cold day in April, and the clocks were striking thirteen."

print(str10[:33])
str10 = str10.split(",")
print(str10[0])



