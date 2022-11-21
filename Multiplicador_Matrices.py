#------------------Clases-------------
class numeroNegativo(Exception):
    pass
#-----------------Variables Globales------------
diccionario_Matrices={}
matriz_ejemplo=[[1,2,3],[4,5,6],[7,8,9]]
#--------------------Metodos----------
#------------------Aqui se agregan cuantas matrices sean Necesarias---------------
def ingreso_matrices():
    while True:
        matriz=[] #Guarda los valores de la matriz antes de agregarla al diccionario
        while True:
            try:
                filas=int(input("Ingrese el ancho del numero de filas: "))
                columnas=int(input("Ingrese el numero de columnas: ")) 
                if ((filas or columnas)<=0):
                    raise numeroNegativo
                break
            except (ValueError):
                print("Valor Numerico Incorrecto")
            except numeroNegativo:
                print("No ingrese numeros negativos")
    
        for i in range(0,filas):
            matriz.append([])
            for j in range(0,columnas):
                while True:
                    try:   
                        valor_Matriz=int(input("Ingrese el valor de ["+str(i)+"]["+str(j)+"]: "))
                        break
                    except ValueError:
                        print("Valor Numerico Incorrecto")

                matriz[i].append(valor_Matriz)

        while True:
            nombre_Matriz=input("Ingrese el nombre de la matriz: ")
            if nombre_Matriz in diccionario_Matrices.keys():
                print("Nombre ya existente, escoja otro.")
            else:
                diccionario_Matrices[nombre_Matriz]=matriz
                break
        respuesta=input("Crear mas matrices?: y o n: ---->")
        if respuesta=='n':
            break
#------------Multiplicador Matrices(Alpha)--------------
def multiplicar_Matrices():
    
    print(diccionario_Matrices)
    new_matriz=[]
    nueva_matriz=[]
    suma=0
    for i in range(0,len(diccionario_Matrices["primer"])):
        #print("i=",i) #Controla filas
        nueva_matriz.append([])
        for h in range(0,len((diccionario_Matrices["segundo"][0]))):
            #print("h=",h)#Controla filas segunda matriz
            new_matriz=[diccionario_Matrices["segundo"][x][h] for x in range(0,len((diccionario_Matrices["segundo"])))]
            for x in range(len(new_matriz)):
                print(diccionario_Matrices["primer"][i][x],"x",new_matriz[x])
            suma=[diccionario_Matrices["primer"][i][x]*new_matriz[x] for x in range(len(new_matriz))]
            total=0
            for y in suma:
                total+=y
            nueva_matriz[i].append(total)
            #print("Suma ",suma,"Total",total)
    print("New Matriz: ",nueva_matriz)
    #determinante_matriz(nueva_matriz)
#--------Para encontrar la determinante de una matriz (Alpha)-------------------- 
def determinante_matriz(new_matriz):
    new_matriz2=new_matriz
    new_matriz2.append(new_matriz[0])
    new_matriz2.append(new_matriz[1])
    print(new_matriz2)
    for n in [1,2]:
        for i in range(0,3):
            positivo=1
            for j in range(0,3):
                positivo*=new_matriz2[j+i][j]
#----------------Metodos varios para el menu--------------
def matrices_Ejemplo():
    diccionario_Matrices["Primer"]=[[1,2,3],[4,5,6],[7,8,9]]
    diccionario_Matrices["Segundo"]=[[9,8,7],[6,5,4],[3,2,1]]
    
def cerrar_Aplicacion():
    exit()

def mostrar_Matrices():
    for i in diccionario_Matrices.keys():
        print("---------",i,"--------\n")
        for j in diccionario_Matrices[i]:
            print(j,"\n")

def Tests():
    while True:
        try:
            algo=int(input("Ingrese el ancho del numero de filas: "))
            if algo<=0:
                raise numeroNegativo
            break
        except (ValueError):
            print("Valor Incorrecto")
        except numeroNegativo:
            print("No ingrese numero negativos")
menu_Principal = {
	1: ingreso_matrices,
	2: multiplicar_Matrices,
    3: matrices_Ejemplo,
    4: cerrar_Aplicacion,
    5: mostrar_Matrices,
    6: Tests,
    }
    

#--------------Bucle Principal------------------------
def run():
    while True:
        while True:
            try:
                n=int(input("1)Agregar Matriz \n2)Con multiplicacion \n3)Matrices Ejemplo Llenado \n4)Salir\n5)Mostrar Matrices Creadas\n-------> "))
                break
            except ValueError:
                print("Ingrese un valor correcto")
        menu_Principal.get(n)()

if __name__ == '__main__':
    run()
