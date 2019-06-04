import PIL.Image as Image
import os

#圖片壓縮批處理
def compressImage(srcPath,dstPath):
    for filename in os.listdir(srcPath):
        #如果不存在目的目錄則建立一個，保持層級結構
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)

        #拼接完整的檔案或資料夾路徑
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename)

        # 如果是檔案就處理
        if os.path.isfile(srcFile):
            try:
                #開啟原圖片縮小後儲存，可以用if srcFile.endswith(".jpg")或者split，splitext等函式等針對特定檔案壓縮
                sImg=Image.open(srcFile)
                w,h=sImg.size
                dImg=sImg.resize((int(w/2),int(h/2)),Image.ANTIALIAS)  #設定壓縮尺寸和選項，注意尺寸要用括號
                dImg.save(dstFile) #也可以用srcFile原路徑儲存,或者更改字尾儲存，save這個函式後面可以加壓縮編碼選項JPEG之類的
                print (dstFile+" 成功！")
            except Exception:
                print(dstFile+"失敗！")

        # 如果是資料夾就遞迴
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)

if __name__=='__main__':
    compressImage(r"C:\Users\kay.lee.IW3E\Pictures\20190412_live_show_dress_run_photo",r"V:\iW3 Events\2019\04Apr\190412-EM-TDB《書虫的少年時代》舞台劇\Photo")