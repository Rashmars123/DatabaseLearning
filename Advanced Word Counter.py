import re


def counter(file: str) -> int :
    try:
        with open(file, 'r') as reader:
            thefile = reader.read()
            thelist = re.split(r'[,,\s]\s*', thefile)
            thelist.remove("")
            print(thelist)

    except FileNotFoundError:
        print("This file does not exist")
    finally:
        if 'thelist' in locals():
            return len(thelist)
        else:
            return 0


print(counter("words2.txt"))
