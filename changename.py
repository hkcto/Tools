import os

def rename(path, newname):
    os.chdir(path)
    filelist = os.listdir(path)

    i = 1
    for name in filelist:
        if name.endswith('.jpg'):
            number = str(i)
            os.rename(name, newname+'_'+number+'.jpg')
            i = i+1
        
        elif name.endswith('.png'):
            number = str(i)
            os.rename(name, newname+'_'+number+'.png')
            i = i+1






rename(r'V:\iW3 Events\2019\06June\190622-CP-TID-movie -九龍不敗\photo\32.九龍不敗\upload', r'九龍不敗')