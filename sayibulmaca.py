import random


print("\n\nMerhaba 10 Deneme Hakkınız bulunmaktadır.\n")
print("Başarılar\n\n")

numara=0
dogruyanlis= []

    
while True:
    try:
        liste = ["+","-","*","/"]
        sayi1 = random.randint(1,9)
        sayi2 = random.randint(0,9)
        if sayi1 < sayi2 :
            continue

        numara += 1 

        
        islem = random.choice(liste)
        metin = "{} {} {} = ? -> ".format(str(sayi1),islem,str(sayi2))

            
        if (islem == "+") :
            sonuc = sayi1 + sayi2
            giris = int(input(metin))
            if (str(sonuc) == str(giris)) :
                print("Tebrikler Sonuc Doğru :)")
                dogruyanlis.append("D")
            else :
                print("Yanlış !! --> Sonuc Doğru {} {} {} = {} olmalıydı".format(str(sayi1),str(islem),str(sayi2),str(sonuc)))
                dogruyanlis.append("Y")
                  

        elif (islem == "-") :
            sonuc = sayi1 - sayi2
            giris = int(input(metin))
            if (str(sonuc) == str(giris)) :
                print("Tebrikler Sonuc Doğru :)")
                dogruyanlis.append("D")
            else :
                print("Yanlış !! --> Sonuc Doğru {} {} {} = {} olmalıydı".format(str(sayi1),str(islem),str(sayi2),str(sonuc)))
                dogruyanlis.append("Y")
                  
        elif (islem == "*") :
                sonuc = sayi1 * sayi2
                giris = int(input(metin))
                if (str(sonuc) == str(giris)) :
                    print("Tebrikler Sonuc Doğru :)")
                    dogruyanlis.append("D")

                else :
                    print("Yanlış !! --> Sonuc Doğru {} {} {} = {} olmalıydı".format(str(sayi1),str(islem),str(sayi2),str(sonuc)))
                    dogruyanlis.append("Y")

                      
        elif (islem == "/") :
            sonuc = sayi1 / sayi2
            giris = int(input(metin))
            if (str(round(sonuc,2)) == str(giris)) :
                print("Tebrikler Sonuc Doğru :)")
                dogruyanlis.append("D")
            else :
                print("Yanlış !! --> Sonuc Doğru {} {} {} = {} olmalıydı".format(str(sayi1),str(islem),str(sayi2),str(round(sonuc,2))))
                dogruyanlis.append("Y")

        if (str(numara) == "10") :
            print("\n\n")
            print("--- Skor Tablosu ---")
            print("--"*10)
            print("Dogru sonuc --> ", dogruyanlis.count("D"))
            print("Yanlış sonuc --> ", dogruyanlis.count("Y"))
            print("--"*10)
            print("\n\n")
            break 

    except(KeyboardInterrupt):
        print("Rakam dışında karakter girişi yapıldı")
        break
        #KeyboardInterruptError Klavye girdi hatası
    except(NameError) :
        print("Rakam dışında karakter girişi yapıldı")
        break
    except(ValueError) :
        print("Rakam dışında karakter girişi yapıldı")
        break
    except (ZeroDivisionError):
        pass
