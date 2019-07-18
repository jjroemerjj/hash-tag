from my_directory.hasch_table import *


if __name__ == '__main__':

    hsh1 = MultiHashSet()

    hsh1.add('Hello 1')
    hsh1.add('Hello 2')
    hsh1.add('Hello 3')

    print(str(hsh1))
    print('Hello 3')
    hsh1.remove('Hello 1')
    print(str(hsh1))
    print(hsh1.contains("Hello 1"))

    hsh1.clear()
    print(str(hsh1))


    # tutaj mamy koniec naszej zabawy