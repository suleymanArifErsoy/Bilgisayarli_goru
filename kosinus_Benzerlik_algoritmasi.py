# İki kelime arasındaki benzerlik oranını hesaplamak için kullanılır genelde 
# bizim burada yapmış olduğumuz program biraz daha sade bir programdır 
# eğer makaleleler arası gibi büyük veri kümesiyle yapılması gereken bir proje yapacaksak hazır derlenmiş bir türkçe word2vec modeli kullanılması önerilir .
# cosinus benzerlik algoritması ile dökümandan anlamlı veri üretmek maksadıyla bir çok algoritma bulunmaktadır .
# TF - IDF (TF : Term frequency => Terim sıklığı .  -  IDF : Inverse Document Frequency => Ters Belge Sıklığı. )

def StopWords(kelime): # anlama ifade etmeyen kelimeleri filitrelememiz ve benzerlik dışı bırakmak gerekir. Başarı oranının artaması için genellikle bu bağlaç veya edat eklerinin kaldırılması ile başarı oranı artar.


    stopWords=["acaba","ama","ancak","artık","aslında","az","gene","gibi","da","de","en","daha","diğer","diye","dolayı"] # literatürde daha fazladır . istenilirse eklenebilir.
    
    bayrak = True 

    for i in range(len(stopWords)):
        if stopWords[i]==kelime:
             return True
        else :
            bayrak = False 
    return bayrak

def ara(dizi,kelime):

    kontrol = False 

    for eleman in dizi :
        if eleman == kelime:
            return True
        else :
            kontrol = False
    return kontrol 

def sozlukOku(cumle_dizisi): #benzerlik ilişkisinde yer alması gereken tüm cümleleri bir dizi olarak kabul eder . Her kelime yalnızca bir defa yazılmış olup StopWords kelimeleri buna dahil edilmedi .

# girilen cumle_dizi parametresi kaç tane cumle birleştirilecek isie parametre olarak [] işareti ile birleştirilerek alınır ve önceden stopWords dizisinde hazırlamış olduğumuz değerleri yazılan cumlede gorulurse bunları birleştirilmiş vectorde yazmaz 
# ve aynı zamanda birleştirmek istediğimiz cumlelerde aynı kelimeden bulunuyorsa bunları da almaz 
    sozluk= []

    for cumle in cumle_dizisi:
        kelimeler = cumle.split(" ")
        for kelime in kelimeler:             
            if(StopWords(kelime)):
                continue
            else :
                if len(sozluk) == 0:
                    sozluk.append(kelime)
                else :
                    if ara(sozluk,kelime):
                        continue
                    else :
                        sozluk.append(kelime)
    return sozluk

def cumle2Vec (cumle,sozluk): # paremetre olarak bir cümle ve önceden cümleler ile oluşturduğumuz sozluk dizisini almaktadır. 

# parametre olarak aldığı cumleyi parçalara boler ve onceden oluşturmuş olduğumuz sozluk dizisi ile karşılaştırarak kaç defa yer aldığını döner 

    vector=[]
    kelimeler=cumle.split(" ")
    for sozcuk in sozluk: # önceden oluşturduğumuz sozluk 
        sozcuk_sayisi=0
        for kelime in kelimeler:
            if kelime==sozcuk:
                sozcuk_sayisi+=1
        vector.append([sozcuk,sozcuk_sayisi])
    return vector    # cumleyi vectorlere donuşturen algoritmayı tamamladık         
    
def noktasalCarpim(vector1,vector2): # kosinus benzerliği algoritmasını uyugulamak için gerekli olan bir parametre
    if (len(vector1)!=len(vector2)):
        return -1
    
    toplam =0
    for i in range(len(vector1)):
        toplam += vector1[i][1] * vector2[i][1]
    return toplam    

def vectorBoyut(vector):
    toplam =0
    for i in range(len(vector)):
        toplam =toplam + (vector[i][1]*vector[i][1])
    return toplam **(1/2)
    

def cosinusBenzerligi(vector1,vector2):
    return noktasalCarpim(vector1,vector2) / (vectorBoyut(vector1)*vectorBoyut(vector2)) # cosinus benzerligi formulu 
        


cumle_bir = "gel bir saryım aşkın olayım"
cumle_iki= "gel aşkın olmak isterdim ama gel sarıl bana"

sozluk = sozlukOku([cumle_bir,cumle_iki])
print(sozluk)

cumle_1_vector = cumle2Vec(cumle_bir,sozluk)
print(cumle_1_vector)
cumle_2_vector = cumle2Vec(cumle_iki,sozluk)
print(cumle_2_vector)

benzerlik_orani = cosinusBenzerligi(cumle_1_vector,cumle_2_vector)
print("iki cumle arasindaki benzerlik orani :=>",str(benzerlik_orani))

