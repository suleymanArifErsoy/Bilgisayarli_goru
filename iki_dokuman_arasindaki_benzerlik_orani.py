import numpy as np 
from gensim.models import Word2Vec
from gensim.models import KeyedVectors 

model = KeyedVectors.load_word2vec_format('trmodel',binary=True) # Önceden derlenmiş veriseti modelimizi yükliyelim .

# Similarity fonksiyonu  :> Giridğimiz iki kelime arasındaki ilişkisel benzerlik değerlini hesaplar 

benzerlik = model.similarity("çay","kahve")
print(benzerlik) # Çalışma sırasında load_word2vec_format ile ilgili bir hata geliyor ona bi bak sonradan !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print()
