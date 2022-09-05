import os
import string

x = string.ascii_lowercase
for i in x:
    os.remove("{}.txt".format(i))

