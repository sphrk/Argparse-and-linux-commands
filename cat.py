# concatenate
from argparse import ArgumentParser
import os
from pathlib import Path

parser = ArgumentParser()

parser.add_argument('file', nargs='*')

args = parser.parse_args()

# print(args)
def read_file(file_name):
    if not os.path.exists(file_name):
        raise Exception(f'"{file_name}" file is not exists')

    if not os.path.isfile(file_name):
        raise Exception(f"{file_name} is not file name")
    
    with open(file_name, 'r') as fp:
        content = fp.read()
    return content


for fname in args.file:
    # print(file)
    if '*' in fname:
        for f in Path().glob(fname):
            print(read_file(f))
    else:
        print(read_file(fname))