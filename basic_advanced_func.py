#ADVANCED-factorial,combination and etc(not finished yet)
#BASIC-multiplication,addition,subtraction,division
import math

def faktorial_komb():
    print("1-Faktorial\n2-Kombinasiya")
    sec=int(input("Secim: "))
    if sec==1:
        n=int(input("Ədəd: "))
        print("Faktorial:",math.factorial(n))
    elif sec==2:
        n=int(input("n: "))
        k=int(input("k: "))
        c=math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
        print("C(n,k):",c)

        def emeliyyatlar():
            print('1-Toplama''\n''2-Bolme''\n''3-Cixma''\n''4-Vurma')
            sec8 = input("Secim: ")
            if sec8 in ['topla', 'Topla', 'Toplama', 'toplama']:
                ededler = []

            for i in range(15):
                daxil = input("Eded daxil et (dayan yaz bitsin): ")

                if daxil in ['dayan', 'break', 'bəsdir', 'besdir']:
                    break

                try:
                    ededler.append(float(daxil))
                except ValueError:
                    print("Yanlis daxil etdiniz")
            if ededler:
                print("Cəm:", round(sum(ededler, 2)))
            else:
                print("Eded daxil etmediniz")
            if sec8 in ['bolme', 'Bolme', 'BOLME', 'bol']:
                bolunen_ededler = []
                for i in range(15):
                    daxil = input("Eded daxil et (dayan yaz bitsin): ")

                    if daxil in ['dayan', 'break', 'bəsdir', 'besdir']:
                        break

                    try:
                        bolunen_ededler.append(float(daxil))
                    except ValueError:
                        print("Yanlis daxil etdiniz")
                if bolunen_ededler:
                    pass
                else:
                    print("Eded daxil etmediniz")
def faktorial_komb():
    print("1-Faktorial\n2-Kombinasiya")
    sec=int(input("Secim: "))
    if sec==1:
        n=int(input("Ədəd: "))
        print("Faktorial:",math.factorial(n))
    elif sec==2:
        n=int(input("n: "))
        k=int(input("k: "))
        c=math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
        print("C(n,k):",c)