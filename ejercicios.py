import os
from random import choice
#////////////Para leer el archivo txt\\\\\\\\\\\\\\\\\\
def read():
    with open("./palabras.txt", "r", encoding="utf-8") as f:  
        listaPalabras=f.read().split('\n')
    f.close()
    return listaPalabras
valoresHombreColgado=["|","|","|","O","/","|","\\","|","/"," \\|"]
iteradorValoresHombreColgado=[" " for x in range(10)]
hombreColgado=[["=" for x in range(10)],
               ["||","\t ","|"],
               ["||","\t ","|"],
               ["||","\t ","|"],
               ["||","\t ","O"],
               ["||","\t","/|\\"],
               ["||","\t ","|"],
               ["||","\t","/ \\"]]
print("".join(hombreColgado[1]))

def validacionLetra(letrasRepetidas):
    while True:
        letraIngresada=input("Ingrese letra: ")
        if len(letraIngresada)!=1:
            print("Letra ingresada tiene que ser de una sola letra")
        elif letraIngresada in letrasRepetidas:
            print("Letra ingresada anteriormente, trate otra distinta")
        elif letraIngresada.isdigit():
            print("Valor ingresado no es una letra")
        else:
            return letraIngresada

        '''try: #En caso de que la letra sea de un solo char, y de error al convertirla en int significa que es valida
            if len(letraIngresada)==1 and letraIngresada not in letrasRepetidas:
                letraIngresada=int(letraIngresada)  
        except:
            return letraIngresada
        else:
            #En el caso de que la conversion de la letra a int no de error
            print("No ingrese = (Numeros, no mas de dos letras)")
        '''    
def generar_Palabra(lista): #De la lista generada seleccionamos aleatoriamente una palabra
    return choice(lista)


def run():
    #os.system("cls")
    listaPalabras=read()
    dificultad=[2,5,10]
    letrasRepetidas=[]  
    print("|Bienvenido a el juego del ahorcado|")
    while True:

        print("------------Elija la dificultad: ---------------")


        palabraGenerada=generar_Palabra(listaPalabras)

        palabra_a_revelar=list("_"*len(palabraGenerada))
        
        print("Ayuda: ",palabraGenerada)

        print("1)Dificil (2 Intentos) \n2)Normal (5 Intentos) \n3)Facil (10 Intentos) \n4)Salir del juego")

        valorDificultad=input("Ingrese------->")

        while valorDificultad not in ["1","2","3","4"]:
            valorDificultad=input("Valor Dificultad incorrecto \nIngrese nuevamente valor de dificultad------->")
        if valorDificultad=="4":
            print("Juego cerrado correctamente")
            break

        valorDificultad=dificultad[int(valorDificultad)-1]

        print("Fuera Bucle")

    

        #print(" ".join(palabra_a_revelar))     
         
        letrasRepetidas.clear()
        while True: 
            print("len:",len(hombreColgado))
            for i in range(len(hombreColgado)):
                print("".join(hombreColgado[i]))
            print("~"*30)
            print(" ".join(palabra_a_revelar))

            

            letraIngresada=validacionLetra(letrasRepetidas)
            if letraIngresada not in palabraGenerada:
                print("Letra incorrecta")
                letrasRepetidas.append(letraIngresada)
                valorDificultad-=1
                #print(letrasRepetidas)
            letrasRepetidas.append(letraIngresada)



            for x ,y in enumerate(palabraGenerada): #Separamos la palabra en una lista de tipo>  [(0,h),(1,o),(2,l),(3,a)]
                #print(f"La posicion de x es={x} y el valor de y es {y}")
                if y==letraIngresada:
                    palabra_a_revelar[x]=y
            #print(" ".join(palabra_a_revelar))
            print(f"Intentos restantes -----> {valorDificultad}")

            #Cuando se completen todas las palabras restantes:
            if "_" not in palabra_a_revelar:
                print("Ganaste")
                break
            if 0==valorDificultad:
                print("Intentos maximos agotados")
                break
            
            

    
    
    
if __name__== '__main__':
    run()
