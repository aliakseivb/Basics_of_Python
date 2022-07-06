from sys import argv
from os.path import join

if len(argv) == 1 \
        or len(argv) > 3 \
        or int(argv[1]) == 0 or argv[1].isnumeric() == False \
        or (len(argv) == 3 and argv[2].isnumeric() == False)\
        or (len(argv) == 3 and int(argv[2]) == 0):
    print('You have entered incorrect parameters. Please, choose:\n'
          '--> "show_sales.py x" to view from "x" to the end of the records; \n'
          '--> or "show_sales.py x y" to view in the range from x to y.')
else:
    show_path = join('.', 'bakery.csv')
    with open(file=show_path, mode='rt', encoding='utf-8') as f:
        if len(argv) == 2:
            for idx, record in enumerate(f):
                if idx > int(argv[1])-2:
                    print(record.strip())
        else:
            for idx, record in enumerate(f):
                if idx > int(argv[1])-2 and idx < int(argv[2]):
                    print(record.strip())
