from random import choice

def read():
    with open("./palabras.txt", "r", encoding="utf-8") as f:  
        listaPalabras=f.read().split('\n')
    f.close()
    return listaPalabras

def validacionLetra(palabraEscondidaList):
    while True:
        letraIngresada=input("Ingrese letra")
        #mostrarPuzzle(palabraEscondidaList)
        try:
            if len(letraIngresada)==1:
                letraIngresada=int(letraIngresada)  
        except:
            print("Letra correcta")
            return letraIngresada
        else:
            print("No ingrese = (Numeros, no mas de dos letras)")
            
    




def generar_Palabra(lista):
    return choice(lista)

def mostrarPuzzle(palabraEscondidaList):
    print(" ".join(palabraEscondidaList))


def run():
    listaPalabras=read()

    palabraGenerada=generar_Palabra(listaPalabras)
    palabraEscondidaList=list("_"*len(palabraGenerada))
    print(palabraGenerada)

    

                
    while True: 
        letraIngresada=validacionLetra(palabraEscondidaList)
        for x ,y in enumerate(palabraGenerada):
            print(f"La posicion de x es={x} y el valor de y es {y}")
            if y==letraIngresada:
                palabraEscondidaList[x]=y
                
        #mostrarPuzzle(palabraEscondidaList)        

        print(" ".join(palabraEscondidaList))
        #Cuando se completen todas las palabras restantes:
        if "_" not in palabraEscondidaList:
            print("Acabado")
            break
            
            

    
    
    
if __name__== '__main__':
    run()
