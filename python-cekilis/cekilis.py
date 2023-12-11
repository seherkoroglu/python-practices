import random

names = ["seher", "seda", "mustafa", "suzan", "selahattin", "eylül"]

def hediyeCekilisi():
    alanlar= names.copy()
    verenler = names.copy()
    print("Çekilişe hoşgeldiniz.")
    print("Çekilişe katılanlar: ", names[0], names[1], names[2], names[3], names[4], names[5])
    
    
    while len(alanlar) > 0:
     alici_index = random.randint(0, len(alanlar)-1)
     verici_index = random.randint(0, len(verenler)-1)
     while alanlar[alici_index] == verenler[verici_index]:
         print("Aynı kişiye hediye verilemez.")
         return hediyeCekilisi()
    
     print( "Hediye verecek kişi:", verenler[verici_index], ", Hediye alacak kişi:", alanlar[alici_index],"\n")
     
    
     del alanlar[alici_index]
     #del verenler[verici_index]
     verenler.remove(verenler[verici_index])
    
    
    
hediyeCekilisi()
    
