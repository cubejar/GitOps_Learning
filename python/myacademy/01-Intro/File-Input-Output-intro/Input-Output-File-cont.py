# Reading file

# Manually close it if you use open method
myfile = open("/Users/rajan/PyCharm/Introduction to Python/Jarkube-Python/Udemy-K/01-Intro/File-Input-Output-intro/test.txt")
myfile.close()

# If using with, you don't need to close it
with open("/Users/rajan/PyCharm/Introduction to Python/Jarkube-Python/Udemy-K/01-Intro/File-Input-Output-intro/test.txt") as myF:
    contents = myF.read()
    print(contents)

# Read a file
with open("test.txt", mode="r") as rF:
    cont = rF.read()

# Write file or overwrite on a file
# or if the file does not exist then it will create
with open("test.txt", mode="w") as wF:
    myF.write("Adding a new file content")

# Append on a file
with open("test.txt", mode="a") as aF:
    aF.write("\nABCD")

# Reading and Writing
with open("test.txt", mode="r+") as rP:
    cont = rP.read()

# Writing and reading (Overwrites existing files or create a new file!")
with open("test.txt", mode="w+") as rP:
   rP.write("GGGGG")
