#lab2
#nowy_tekst=int(input("wpisz tekst "))
#print(nowy_tekst)

def zad1():
    równanie=(512-282)/(47*48+5)
    print(równanie)
def zad2():
    x =int(input("wpisz liczbę "))
    a=x*2
    b=x*3
    c=x*4
    d=x*5
    print(str(a)+"---" + str(b) +  "---"+str(c)+ "---"+str(d) )
def zad3():
    x = float(input("wpisz liczbę "))
    y = float(input("wpisz 2 liczbę "))
    print(x*y)


def zad4():
    x = float(input("wpisz wagę "))
    print(x*2.2)

def zad5():
    suma=sum(range(1,11))
    print(suma)


def zad6():
    iloczyn = 1
    for i in range(1,11):
        iloczyn*=i
    print(iloczyn)

def zad7():
    rok = int(input("podaj rok   "))
    rokk = 31 + 28 + 31
    if(rok%4==0 and rok%100!=0 or rok%400==0):

       print("suma pierwszych 3 miesięcy: "+str(rokk))
    else:
        print("nieprawidłowy rok")

def zad8():
    kap_poczatkowy=1000
    oprocentowanie=0.06
    p_rok=kap_poczatkowy*(1+oprocentowanie)
    d_rok = p_rok * (1 + oprocentowanie)
    t_rok = d_rok * (1 + oprocentowanie)
    print(p_rok)
    print(d_rok)
    print(t_rok)






def main():
    zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    zad6()
    #zad7()
    zad8()

main()



