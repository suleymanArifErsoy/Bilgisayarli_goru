import cv2
import numpy as np
import warnings
import math
from PIL import Image

kopek = cv2.imread('kopek.jpg') # görseli matrixe dönüştürmek için imraed fonksiyonu kullandık.
kopek2 = cv2.imread("kopek2.jpg")
 
print(kopek.shape) # görselin boyutlarını aldık (612,984,3) en sondaki 3 rgb renk kanallarından olan 3 boyutlu bir resim olduğunu söyler.

# yukarıda çözümlemiş olduğumuz görsel artık 612x984 boyuntlarında ve 3(RGB) kanallı bir matrixtir. Bu matrixi yazmak istersek eğer aşağıdaki iç içe for döngüsü kullanarak
# yazdırabiliriz. 
#for i in kopek:
#    for pixel in i :
#        print(pixel,end= " ")
#    print("\n")    

yukseklik = kopek.shape[0] # yukseklik değeri
genislik  = kopek.shape[1] # genişlik değeri 

# iki matrix arasındaki benzerliği hesaplamak için kesin benzerlik oranı tespit edeceğiz 
# Bunun için her bir pikselin , diğer görüntü matrisindeki karşılığı olan piksel ile arasındaki fark değerleri toplanılmalıdır .
# Bu fark toplamının tüm piksel değerlerine oranı bize iki resmin farklılık oranını verecektir. 

def pixel_fark(pixel1,pixel2):
    pixel_fark=0
    for i in range(3):
        pixel_fark = pixel_fark +abs(pixel1[i]-pixel2[i])/255 # pixel içerisindeki R G B değerleri arasındaki farkları toplamını alır.
        # abs fonksiyonu ise arasındaki farkın mutlak değerini alır.
    return pixel_fark    
# Eğer görseller farklı matris buyutlarında ise negatif dolgu tekniği ile boyutları daha küçük olan görsel doldurulur.
# Küçük boyutlu matrisin, buyuk boyutlu matriste olmayan kısımları , buyuk matristeki karşılığının tam tersi alınarak doldurulur .
def fark_matris(matris1,matris2): 
    yukseklik,genislik = matris1.shape[0],matris2.shape[1]
    matris = np.zeros(shape=(yukseklik,genislik,3),dtype=np.uint8)
    for i in range(yukseklik):
        for j in range(genislik):
            if pixel_fark(matris1[i][j],matris2[i][j])==0:
                matris[i,j,0]=255
                matris[i,j,1]=255
                matris[i,j,2]=255
            else:
                matris[i,j,0]=matris2[i][j][0]
                matris[i,j,1]=matris2[i][j][1]
                matris[i,j,2]=matris2[i][j][2]
    img = Image.fromarray(matris,'RGB')
    img.save("farkmatris.png")            




fark =0 
for i in range(yukseklik):
    for j in range(genislik):
        fark = fark + pixel_fark(kopek[i][j],kopek2[i][j]) # burada yaptığımız işlem görseldeki tüm piksel farklar toplamını tek bir değişkende topladık
        # pixel_fark fonksiyonu ise sadece bir piksel için bu fark toplamını hesaplıyor.

farklilik_orani =100*fark/(genislik*yukseklik*3) # fark oranını %'lik bir şekilde kullanıcıya gösetermek için 100 ile çarpıp tüm piksellerin sayisina oranladık
# eğer benzerlik oranını göstermek istersek farklıllık oranını 100'den çıkarırız. 
print("İki resim arasinda %"+str(int(farklilik_orani))+ " fark vardir")


