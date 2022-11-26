
def read():
    lista_Generada=[]
    
    with open("./palabras.txt", "r", encoding="utf-8") as f:
        lista_Generada=f.read()
    f.close()
    #for x in lista_Generada:
    #    print(x)
    #    if x=="\n":
    #        print("Validado")
    valoresBlancos=[x for x in lista_Generada if x==" "]
    print(valoresBlancos)
def separarPalabras():
    pass
        

def run():
    read()

if __name__== '__main__':
    run()
