def delta(a,b,c):
    return (pow(b,2) - 4*a*c)

def NombreRacine(d):
    if a == 0:
        return 1
    return 0 if d < 0 else ( 1 if d == 0 else 2 )


def AfficheNombreRacine():
    global a
    global b
    global c
    d = delta(a,b,c)
    print(f"Le nombre des solutions est : {NombreRacine(d)}")


def Racine1():
    pass

def Racine2():
    pass


a , b, c = (0, 4, 4)

AfficheNombreRacine()