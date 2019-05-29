import tinify
import sys
from glob import glob
from os import chdir

tinify.key='W0B0Lkz7mACIl6oaVbMzIJQiUlUAa9cF'

def tinc(source=None):
    while source :
        chdir(source)
        types = ['*.jpg', '*.jpeg', '*.png']
        files = []
        for file in types:
            files.extend(glob(file))
        
        for i in files:
            print(i)
        
        print('compressioning...')

        for i in files:
            source = tinify.from_file(i)
            source.to_file(i)
            print('compression done : ', i)

        break
    else:
        print('input folder path pls')


if __name__ == "__main__":
    try:
        tinc(sys.argv[1])
    except IndexError as n:
        print("路徑應使用隻引號")