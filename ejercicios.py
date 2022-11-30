from random import choice
#////////////Para leer el archivo txt\\\\\\\\\\\\\\\\\\
def read():
    with open("./palabras.txt", "r", encoding="utf-8") as f:  
        listaPalabras=f.read().split('\n')
    f.close()
    return listaPalabras

def validacionLetra():
    while True:
        letraIngresada=input("Ingrese letra")
        try: #En caso de que la letra sea de un solo char, y de error al convertirla en int significa que es valida
            if len(letraIngresada)==1:
                letraIngresada=int(letraIngresada)  
        except:
            print("Letra correcta")
            return letraIngresada
        else:
            #En el caso de que la conversion de la letra a int no de error
            print("No ingrese = (Numeros, no mas de dos letras)")
            
def generar_Palabra(lista): #De la lista generada seleccionamos aleatoriamente una palabra
    return choice(lista)


def run():
    listaPalabras=read()
    dificultad=[2,5,10]
    
    print("|Bienvenido a el juego del ahorcado|")
    while True:

        intentos=0
        print("Elija la dificultad: ")


        palabraGenerada=generar_Palabra(listaPalabras)

        palabra_a_revelar=list("_"*len(palabraGenerada))
        
        print("Ayuda: ",palabraGenerada)

        print("1)Dificil (2 Intentos) \n2)Normal (5 Intentos) \n3)Facil (10 Intentos) \n4)Salir del juego")

        valorDificultad=input("Ingrese------->")

        while valorDificultad not in ["1","2","3","4"]:
            valorDificultad=input("Valor Dificultad incorrecto \n Ingrese nuevamente------->")
        if valorDificultad=="4":
            print("Juego cerrado correctamente")
            break

        valorDificultad=dificultad[int(valorDificultad)-1]

        print("Fuera Bucle")

    

                
        while True: 
            letraIngresada=validacionLetra()
            if letraIngresada in palabraGenerada:
                print("Letra si esta en palabra")



            for x ,y in enumerate(palabraGenerada): #Separamos la palabra en una lista de tipo>  [(0,h),(1,o),(2,l),(3,a)]
                #print(f"La posicion de x es={x} y el valor de y es {y}")
                if y==letraIngresada:
                    palabra_a_revelar[x]=y
            print(" ".join(palabra_a_revelar))
            print(f"Intentos restantes -----> {intentos}")

            #Cuando se completen todas las palabras restantes:
            if "_" not in palabra_a_revelar:
                print("Ganaste")
                break
            
            

    
    
    
if __name__== '__main__':
    run()
