from random import choice


def read():
    with open("./palabras.txt", "r", encoding="utf-8") as f:  
        listaPalabras=f.read().split('\n')
    f.close()
    return listaPalabras

def separarPalabras():
    pass
        
def generar_Palabra(lista):
    palabra=choice(lista)
    return palabra



def run():
    palabra=generar_Palabra(read())
    palabraEscondidaList=list("_"*len(palabra))
    while True:
        letraIngresada=input("Ingrese letra")
        for x ,y in enumerate(palabra):
            print(f"La posicion de x es={x} y el valor de y es {y}")
            if y==letraIngresada:
                palabraEscondidaList[x]=y
                

        print(" ".join(palabraEscondidaList))
            
            

    
    
    
if __name__== '__main__':
    run()
