# word count
import os
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', action='store_true', help='prints number of lines')
parser.add_argument('-w', action='store_true', help='prints number of words')
parser.add_argument('-m', action='store_true', help='prints the count of characters from a file')
parser.add_argument('-c', action='store_true', help='prints the count of bytes in a file')


args = parser.parse_args()
# print(args)

for file in args.filenames:
    if not os.path.exists(file):
        raise Exception(f'"{file}" file is not exists')

    if not os.path.isfile(file):
        raise Exception(f"{file} is not file name")
    
    with open(file, 'r') as fp:
        text = fp.read()
    
    temp = text.count('\n')
    n_lines = 0 if temp == 0 else temp + 1
    n_words = len(text.strip().replace('\n', ' ').split(' '))
    n_bytes = len(text)
    # n_chars = n_bytes # len(text.replace('\r', '').replace('\n', ''))

    flag = False
    if (args.l == False) and (args.w == False) and (args.c == False):
        flag = True

    template = "{:<5}"
    if args.l or flag:
        print(template.format(n_lines), end='')
    if args.w or flag:
        print(template.format(n_words), end='')
    if args.m or args.c or flag:
        print(template.format(n_bytes), end='')
    print(file)
    


