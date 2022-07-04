file = open("article.txt", "r")
print(file.read())  # read the entire file
print(file.read(64))  # read the first 64 characters
print(file.readline())  # read the first line
file.close()

with open("article.txt", "r") as same_file:  # open file using exception handling
    print(same_file.readline())
