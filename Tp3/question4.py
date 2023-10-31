import question3

h = int(input("nombre des heures : "))
m = int(input("nombre des minutes : "))
s = int(input("nombre des secondes : "))

print("{}h {}m {}s en secondes est {}s".format(h, m, s, question3.conversion_temps(h, m, s)))


