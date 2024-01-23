def n_a_parole(n):
    unita = {
        0: "", 1:"Uno", 2:"Due", 3:"Tre", 4:"Quattro", 5:"Cinque", 6:"Sei", 7:"Sette", 8:"Otto", 9: "Nove",10: "Dieci",
        11: "Undici", 12:"Dodici", 13:"Tredici", 14:"Quattordici", 15:"Quindici", 16:"Sedici", 17: "Diciassette", 18:"Diciotto", 19:"Diciannove",
    }
    decine = {   
        0: "", 20:"Venti",30:"Trenta",40:"Quaranta",50:"Cinquanta",60:"Sessanta",70:"Settanta",80:"Ottanta",90:"Novanta",
    }
    altro = {
        0:"", 1: "cento", 2:"mila"
    }

    if n < 20:
        return unita[n]
    elif n < 100:
        return decine[n-n%10] + unita[n%10]
    elif n<1000:
        x = n//100
        y = n%100
        #print(n%10)
        return (unita[x] if x > 1 else "") + altro[1] + (decine[n%100-n%10] if y>19 else "") + (unita[n%10 if y>19 else n%100])
    elif n<10000:
        x = n//1000
        #print(n)
        r = n%1000
        #print(r)
        y = r//100
        #print(y)
        j = r%100
        #print(j)
        return(
              (unita[x] + altro[2] if x > 1 else "mille") 
            + (unita[y] if y > 1 else "") 
            + (altro[1] if y>=1 else "") 
            + (decine[n%100-n%10] if j>19 else "") 
            + (unita[n%10 if j>19 else n%100])
            )
    else:
        return "Sotto i 10.000!!!!"


def run():
    while True:
        print(n_a_parole(int(input("Inserisci: "))).title())

if __name__ == "__main__":
    run()