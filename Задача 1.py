def dekor(yscor):
    def new(V,V0,t):
        try:
            yscor(V,V0,t)
        except (TypeError,ZeroDivisionError):
            print("Заново делай")
            exit
        finally:
            print(((V-V0)/2)*t)
    return new

@dekor
def yscor(V,V0,t):
    print((V-V0)/t)

V=float(input("Введите скорость"))
V0=float(input("Введите начальную скорость"))
t=float(input("Введите время"))
print(yscor(V,V0,t) )