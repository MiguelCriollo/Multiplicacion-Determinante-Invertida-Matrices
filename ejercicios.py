import os
from random import choice

#////////////Para leer el archivo txt\\\\\\\\\\\\\\\\\\
def read():
    with open("./palabras.txt", "r", encoding="utf-8") as f:  
        listaPalabras=f.read().split('\n')
    f.close()
    return listaPalabras

#///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
caracteresHombreColgado="|||O/|\\|/\\"
#//////////////Se valida la letra leida, no sale de bucle hasta que sea correcta\\\\\\\\\
def validacionLetra(letrasRepetidas):
    while True:
        letraIngresada=input("Ingrese letra: ")
        if len(letraIngresada)!=1:#-----------------------------------------Si se ingresan mas de un valor
            print("Letra ingresada tiene que ser de una sola letra")
        elif letraIngresada in letrasRepetidas:#----------------------------Si la letra ingresada(Correcta o incorrecta) ya ha sido escrita anteriormente
            print("Letra ingresada anteriormente, trate otra distinta")
        elif letraIngresada.isdigit():#-------------------------------------Si es un numero
            print("Valor ingresado no es una letra")
        else:
            return letraIngresada #La letra es valida
#//////////////////////////--------------------------------\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#///////////////////////////Randomizacion de palabra\\\\\\\\\\\\\\\\\\\\\\\
def generar_Palabra(lista): #De la lista generada seleccionamos aleatoriamente una palabra
    return choice(lista)
#//////////////////////////------------------------------------\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#/////////////////////////////------Main-----------\\\\\\\\\\\\\\
def run():
    os.system("cls") #--------------------------------------------------------------------Para limpiar datos en consola
    listaPalabras=read() #---------------------------------------------------------------Lectura del archivo txt de las palabras posibles
    dificultad=[2,5,10] #----------------------------------------------------------------Guarda valor de se elije facil, norma o dificil
    letrasRepetidas=[] #-----------------------------------------------------------------Lista donde se guardan letras correcta o incorrectas que ya han sido ingresadas
    print("|Bienvenido a el juego del ahorcado|")
    while True:#-------------------------------------------------------------------------Bucle principal, sale solamente si se ingresa desde el menu
        seIngresa=True
        modoCompetitivo=False
        contadorCompetitivo=3
        auxContadorCompetitivo=contadorCompetitivo
        nombreJugador=""
        print("------------Elija la dificultad: ---------------")
        
        print("1)Dificil (2 Intentos) \n2)Normal (5 Intentos) \n3)Facil (10 Intentos) \n4)Salir del juego \n5)Modo Competitivo")
        valorMenu=input("Ingrese------->")
        while valorMenu not in ["1","2","3","4","5"]:
            valorMenu=input("Valor Dificultad incorrecto \nIngrese nuevamente valor de dificultad------->")

        if valorMenu=="4":
            print("Juego Cerrado correctamente")
            break

        if valorMenu=="5":
            nombreJugador=input("Has elegido el modo Competitivo\nIngresa tu nombre para comenzar (Escribe ""exit"" si deseas cancelar esta accion.)\n------->")
            if nombreJugador=="exit":
                seIngresa=False
                modoCompetitivo=False
            else:
                modoCompetitivo=True
            valorMenu="2"

        if seIngresa==True:
            valorMenu=dificultad[int(valorMenu)-1] #---------------------------------Guardamos cuantos intentos tenermos
            nivelDificultad=10/valorMenu #-------------------------------------------Valor de cuantos caracteres mostramos dependiendo de la dificultad
            caracteres=list(" "*10) #------------------------------------------------Elimino la lista de caractes a vacios, este muestra al ahorcado
            letrasRepetidas.clear() #------------------------------------------------Borramos las letras ya ingresadas
            value=0 #----------------------------------------------------------------Value sirve para saber que valores strings agrego a la lista vacia de caracteres
            os.system("cls")
            palabraGenerada=generar_Palabra(listaPalabras)#----------------------------------Generamos la palabra a usar en esta ronda
            palabra_a_revelar=list("_"*len(palabraGenerada))#--------------------------------Creamos una lista de _ dependiendo la longitud de la palabra
            print("Ayuda: ",palabraGenerada)

            print("Nombre: ",nombreJugador)
        while seIngresa==True and contadorCompetitivo!=0: 

        
                




            #------------------------------------------------------------------------Forma hombre colgado
    
            hombreColgado=[["=" *10],
               ["||","\t ",caracteres[0]],
               ["||","\t ",caracteres[1]],
               ["||","\t ",caracteres[2]],
               ["||","\t ",caracteres[3]],
               ["||","\t",caracteres[4],caracteres[5],caracteres[6]],
               ["||","\t ",caracteres[7]],
               ["||","\t",caracteres[8]," "+caracteres[9]]]
            for i in range(len(hombreColgado)): #------------------------------------Mostramos el hombre colgado
                print("".join(hombreColgado[i]))

            print("~"*30) #----------------------------------------------------------Imprimimos secuencia d signos
            print(" ".join(palabra_a_revelar)) #-------------------------------------Mostramos el estado de la palabra a revelar

            if "_" not in palabra_a_revelar: #---------------------------------------Si se ha completado la palabra a reverlar se gana el juego
                print("!!!!!!!!!!!!!Palabra Correcta!!!!!!!!!!!!!!!")
                if modoCompetitivo==False:
                    break
                else:
                    contadorCompetitivo-=1
            if 0==valorMenu: #-------------------------------------------------------Si los intentos se acabaron
                print("Intentos maximos agotados")
                print("\nPalabra correcta: \n",palabraGenerada)
                if modoCompetitivo==False:
                    break
                else:
                    contadorCompetitivo-=1
                
            if contadorCompetitivo!=auxContadorCompetitivo:
                palabraGenerada=generar_Palabra(listaPalabras)#----------------------------------Generamos la palabra a usar en esta ronda
                palabra_a_revelar=list("_"*len(palabraGenerada))#--------------------------------Creamos una lista de _ dependiendo la longitud de la palabra
                caracteres=list(" "*10) #------------------------------------------------Elimino la lista de caractes a vacios, este muestra al ahorcado
                letrasRepetidas.clear() #------------------------------------------------Borramos las letras ya ingresadas
                os.system("cls")
                print("Ayuda: ",palabraGenerada)
                auxContadorCompetitivo=contadorCompetitivo
                
            else:
                letraIngresada=validacionLetra(letrasRepetidas)#-------------------------Validamos que la letra ingresada sea valida
                os.system("cls")
                if letraIngresada not in palabraGenerada: #------------------------------Si damos una letra incorrecta esta se agrega a las repetidas
                    print("X"*30,"\n!Letra ingresada es Incorrecta! \n","X"*30)
                    for j in range(int(nivelDificultad)): #------------------------------Si la palabra ingresada es incorrecta
                        caracteres[value]=caracteresHombreColgado[value] #---------------Convertimos a los caracteres de la posicion que los toca del string, se repite depende el nivel de dificultad
                        value+=1 
                    valorMenu-=1 #-------------------------------------------------------Se reduce las intentos restantes
                letrasRepetidas.append(letraIngresada) #---------------------------------Ingresados letra sea correcta o incorrecta a las letras ingresadas

                for x ,y in enumerate(palabraGenerada): #--------------------------------Separamos la palabra en una lista de tipo>  [(0,h),(1,o),(2,l),(3,a)]
                    if y==letraIngresada: #----------------------------------------------Si la letra ingresada esta en palabra generada
                        print("✓"*30,"\n!Letra ingresada es Correcta! \n","✓"*30)
                        palabra_a_revelar[x]=y #-----------------------------------------Colocamos la letra resuelta 
                print(f"Intentos restantes -----> {valorMenu}")
            #------------------------------------------------------------------------Este bucle sirve para colocar las partes del ahorcado dependiendo de su dificultad
            
if __name__== '__main__':
    run()
