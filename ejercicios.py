from random import choice

def read():
    with open("./palabras.txt", "r", encoding="utf-8") as f:  
        listaPalabras=f.read().split('\n')
    f.close()
    return listaPalabras




def generar_Palabra(lista):
    palabraGenerada=choice(lista)
    return palabraGenerada



def run():
    listaPalabras=read()
    palabraGenerada=generar_Palabra(listaPalabras)
    palabraEscondidaList=list("_"*len(palabraGenerada))
    while True:
        letraIngresada=input("Ingrese letra")
        for x ,y in enumerate(palabraGenerada):
            print(f"La posicion de x es={x} y el valor de y es {y}")
            if y==letraIngresada:
                palabraEscondidaList[x]=y
                

        print(" ".join(palabraEscondidaList))
            
            

    
    
    
if __name__== '__main__':
    run()
