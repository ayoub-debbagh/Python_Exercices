print("1 : euro en mad", "2 : mad en euro", sep="\n")
conversion = input("Quel operation voullez vous effectuer?")

value = float(input("Entrer le montant : "))

match conversion:
    case 1:
        value *= 11
    case 2:
        value /= 11
    case _:
        pass


print(value)
