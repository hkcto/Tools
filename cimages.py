import PIL.Image as Image
import os
from sys import argv

#圖片壓縮批處理
def compressImage(srcPath, width = 2880):
    os.chdir(srcPath) # 進入到指定目錄
    srcFiles = os.listdir(srcPath)  # os.listdir 列出所有目錄中的檔案

    # images list 得到 jpeg jpg png 圖片
    images = [name for name in srcFiles if name.endswith('.jpeg') or name.endswith('.jpg') or name.endswith('.png')]
    for image in images:
        try:
            #開啟原圖片縮小後儲存，可以用if srcFile.endswith(".jpg")或者split，splitext等函式等針對特定檔案壓縮
            sImg=Image.open(image)
            w,h=sImg.size

            # 設定壓縮尺寸(scale 按比例)和選項，注意尺寸要用括號
            scale = float(w/h) # 寛除高,得出比例
            dImg=sImg.resize((int(width),int(width/scale)), Image.ANTIALIAS)
            dImg.save(image)
            print (image+" 成功！")
        except Exception:
            print(image+"失敗！")
            
if __name__=='__main__':
    src = input(r"input patch : ")
    try:
        iwidth = int(input(r"input width (default 2880): "))
        compressImage(src, iwidth)
    except:
        compressImage(src)