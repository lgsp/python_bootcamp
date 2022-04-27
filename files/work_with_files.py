import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("A long time ago in a galaxy far, far away...\n")
    my_file.write("It is a period of civil war.\n")
    my_file.write("Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.\n")
    my_file.write("During the battle, Rebel spies managed to steal secret plans to the Empire ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.\n")

print("=" * 50)

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print("=" * 50)

print(my_file.closed)

print(my_file.name)
print(my_file.mode)
os.rename("mydata.txt", "mydata2.txt")
#os.remove("mydata2.txt")
#os.mkdir("mydir")
#os.chdir("mydir")
print("Current Directory:", os.getcwd())

with open("mydata2.txt", encoding="utf-8") as my_file:
    line_num  = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print("Line: ", line_num, " : ", line, end="")
        line_num += 1

print("=" * 50)

with open("mydata2.txt", encoding="utf-8") as my_file:
    line_num  = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print("Line: ", line_num, " : ", line, end="")
        word_list = line.split()
        nb_word = len(word_list)
        avg_word_len = sum([len(word) for word in word_list]) / nb_word
        print("Number of Words:", nb_word)
        print("Avg Word Length:", round(avg_word_len, 2))
        print('-' * 25)
        line_num += 1        

        
