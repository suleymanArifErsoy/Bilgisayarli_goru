dosya = open("evrensel_renkeler.txt","r",encoding="utf-8")
kontrol =True
yeni_dosya=open("evrensel.txt","a")

while kontrol:
    sayac=0
    sayac_kontrol = 1
    try:
        satir=dosya.readline()
    except EOFError:
        kontrol = False

   
    satir=satir.split("-")
    yeni_dosya.write(satir[0]+" -> ")

    if satir != "":
        for i in range(len(satir[1])):
                
                if  satir[1][i] == " ":
                    sayac +=1
                    if sayac >=2:
                        sayac_kontrol = 0
                if sayac_kontrol == 0:
                    not kontrol
                    break  
                yeni_dosya.write(satir[1][i])
        yeni_dosya.write("\n")
    

        



    