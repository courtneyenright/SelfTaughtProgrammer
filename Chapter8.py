#Make a file

with open ("helloworld.txt", "w") as f:
    f.write("Hi from Python!")

#Open the file & Print

with open("helloworld.txt", "r") as g:
    print(g.read())

import csv

#make a csv file

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=',')
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])


#print csv file

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
