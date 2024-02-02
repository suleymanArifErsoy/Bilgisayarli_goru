# renk değerleri arasında benzerlik oranı hesaplama 

# renk uzaylarını normalize eder 
def arrange(item,dim,min,max): #Sıkıştırma (renk uzayı , boyutu , renk skalası en düşük değer , renk skalası en büyük değer  )

    item_count,i=len(item),0

    for i in range(dim):
        if i <=item_count:
            item[i] = item[i] / ( ( max - min ) / 100 )
        else:
            item[i] = 50 / ((max - min)/100)
    return item

def kokAl(sayi):
    return sayi**(1/2)

def usAl(sayi,derece):
    return sayi**derece

def vectorSimilarity(A,B): # Vektor benzerlik hesaplama A ve B parametreleri renk skalasının boyut değeridir 

    if len(A) != len(B):
        return -1
    else:
        total = 0
        
        for i in range(len(A)):
            total += usAl(A[i]-B[i],2) # analitik uzaklık hesaplaması yapılır uzaklık = kokAl( (x1-x2)karesi + (y1-y2)karesi + ....)
        distance = kokAl(total) # makine ögrenmesi için veri kümeleme işlemi burada bitirilir Benzerlik oranını bulmaya gerek yoktur aslında ama biz aşagıda 0 ile 1 arasında bir oran hesaplaması yapacaz 
        max_dist = 0
        for i in range(len(A)):
            max_dist += usAl(100,2) # 0 ile 1 arasında bir oran elde etmek için max uzaklık arasındaki farkı 100 olarak aldık  
        max_dist = kokAl(max_dist)    
        return 1 - (distance/max_dist)

gri_normalized = arrange( [82,82,82] , 3 , 0 , 255 )
koyu_kirmizi_normalized = arrange( [181,25,25] , 3 , 0 , 255 )
benzerlik_orani = vectorSimilarity(gri_normalized,koyu_kirmizi_normalized)
print(benzerlik_orani)