import random
print("hola bienvenido al juego del dado ")
dado = random.randint(1, 20)
enter= input("hola oprime [y] para tirar el dadoo[x]para terminar:{}")

print(dado)
while enter == "y":

    enter = input("hola oprime [y] para tirar el dadoo[x]para terminar:{}")
    dado = random.randint(1, 20)
    print("tu numero es:{}".format(dado))

else:print("juego tterminado reinicia para empezar de nuevo")










