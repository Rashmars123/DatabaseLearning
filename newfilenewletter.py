import string

x = string.ascii_lowercase
thelist = [ i for i in x]

for i in thelist:
        with open("{}.txt".format(i), 'w') as generator:
            generator.write(i)
