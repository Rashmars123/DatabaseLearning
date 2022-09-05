import string

x = string.ascii_lowercase
thelist = [i for i in x]

with open("alphabet.txt", 'w') as generator:
    for i in range(0, len(thelist) - 1, 3):
        if i == 24:
            generator.write(thelist[i] + thelist[i + 1] + "\n")
        else:
            generator.write(thelist[i] + thelist[i + 1] + thelist[i + 2] + "\n")

try:
    with open("alphabet.txt", 'r') as reader:
        t = reader.readlines()
        for i in t:
            print(i[0:3])
except FileNotFoundError:
    print("The file does not exist")