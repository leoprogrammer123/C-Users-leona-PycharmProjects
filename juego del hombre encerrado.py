import random

def main():

    vida = 100
    continuar_juego= True

    def restart(deseas_reiniciar):
        deseas_reiniciar=input("deseas reiniciar? [s/n]")
        if deseas_reiniciar =="s":
            main()
        if deseas_reiniciar == "n":
            print("juego finalizado")
            exit()
        return

    # aqui empieza el juego y la primer pregunta

    print ("ea games awrichiriguen")

    pregunta_1=input("hola y bienvenido al juego de la vida tienes 100 de vida por cada decision mal tomada \n"
          "pierdes 20 tienes 2 vidas \n"
          "estas en un cuarto obscuro y lo unico que se ve es unos botones con numeros y a mano tienes una mechera que haces? \n"
                     "a - prendes la mechera \n"
                     "b - oprimes uno de los numeros\n")

    if pregunta_1 == "a":
         print("en el cuarto hay gasolina y explosivos y genersa \n"
               "una gran explosion pierdes 20 de vida \n"
               "selecciona un numero del uno al 5")
         vida = vida - 30
    elif pregunta_1 != "a":

            print("selecciona un numero del uno al 5 mucha suerte")

    print("tienes esto de vida", format(vida))


        #aqui va la segunda pregunta

    pregunta_2 = random.randint(1, 5)

    numero = int(input( "1 ,2 ,3 ,4 ,5 = "  ))

    if numero == pregunta_2:
        print("felicidades sigues a la siguiente habitacion intacto")
    elif pregunta_2 != numero:
        vida = vida - 30
        print("numero erroneo pierdes 20 de vida te queda")
        if vida == 0:
            print(f"has perdido totda tu vida{main()}")
            return main()

    print (vida)



#aqui va la la tercera pregunta

    pregunta_3= input(" en la siguiente habitacion  estas solo con un leon y hay dos armas en la pared ???\n"
                      " que escojes?\n"
                      "A - ak 47\n"
                      "B - escopeta\n")

    if  pregunta_3 == "a":
        print("matas al leon de un solo disparo")
    elif pregunta_3 != "a":
        vida = vida - 30
        print("matas al leon pero no sin antes ser herido por que se te atasca el arma")

    print ("tienes esto de vida",format(vida))
    if vida <0:
        print(f"has perdido totda tu vida{main()}")
        return main()



    #aqui va la pregunta 4
    pregunta_4= input("en el siguiente cuarto hay dos cajas de colores\n"
                      " uno contiene la llave  para el ultimo cuarto cual "
                      "escoges\n"
                      "A - rojol\n"
                      "B - azul\n")
    if  pregunta_4 == "a":
        print("felicidades encuetras la llave y pasas al ultimo cuarto")
    elif pregunta_4== "b":
        vida = vida - 20
        if vida < 0:
            print("has perdido")
            restart(deseas_reiniciar="s")


        print("hay un escorpion y te quita 20 de vida")

    print(vida)




    #aqui  va una pregunta conectada a la 4

    pregunta_5= input("en este cuarto hay un serrucho ydebes tomar una dificil decision  \n"
                      "te quitas una mano o un pie en cualquiera de las dos perderas vida pero sera\n"
                      "decisivo para el ultimo cuarto que te cortas\n"
                      "A- mano\n"
                      "B- pie \n")
    if pregunta_5 == "a":
        print(f"pasas a la siguiente habitacion {vida-20}")
    elif pregunta_5 =="b":
        print(f"pasas a la siguiente habitacion {vida-20}")



    while continuar_juego:

        pregunta_final = input("en este ultimo cuarto hay un lector de huellas\n"
                               "donde debes poner tus dos manos\n"
                               "que haces?\n"
                               "A- pones las manos \n"
                               "B- hay una pistola en el suelo te suicidas")
        if pregunta_5 == "b" and pregunta_final == "a":
            print("felicidades has ganado")
        elif pregunta_final =="b":
            print("has muerto")
            restart(deseas_reiniciar="b")

        elif pregunta_5 == "b" and pregunta_final == "b":
            print("tenias las dos manos para ganar pero decides matarte juego finalizad")
            exit()

        if pregunta_5 =="a"and pregunta_final=="a":
            print("no tienes manos")

            continuar_juego=True








if __name__ == '__main__':
    main()


#



















