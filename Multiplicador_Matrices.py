matrices={}

def ingreso_matrices():
    while True:
        matriz=[]
        respuesta=''
        nombre_Matriz=""
        filas=int(input("Ingrese el ancho del numero de filas: "))
        columnas=int(input("Ingrese el numero de columnas: ")) 
        for i in range(0,filas):
            matriz.append([])
            for j in range(0,columnas):
                print(i,j)
                matriz[i].append(int(input("Ingrese el valor de ["+str(i)+"]["+str(j)+"]: ")))
        while True:
            nombre_Matriz=input("Ingrese el nombre de la matriz: ")
            if str(matrices.get(nombre_Matriz)) !='None':
                print("Nombre ya existente, escoja otro.")
            else:
                matrices[nombre_Matriz]=matriz
                break
        respuesta=input("Crear mas matrices?: y o n: ---->")
        if respuesta=='n':
            break
    
def multiplicar_Matrices():
    
    print(matrices)
    new_matriz=[]
    nueva_matriz=[]
    suma=0
    for i in range(0,len(matrices["primer"])):
        #print("i=",i) #Controla filas
        nueva_matriz.append([])
        for h in range(0,len((matrices["segundo"][0]))):
            #print("h=",h)#Controla filas segunda matriz
            new_matriz=[matrices["segundo"][x][h] for x in range(0,len((matrices["segundo"])))]
            for x in range(len(new_matriz)):
                print(matrices["primer"][i][x],"x",new_matriz[x])
            suma=[matrices["primer"][i][x]*new_matriz[x] for x in range(len(new_matriz))]
            total=0
            for y in suma:
                total+=y
            nueva_matriz[i].append(total)
            #print("Suma ",suma,"Total",total)
    print("New Matriz: ",nueva_matriz)
    #determinante_matriz(nueva_matriz)

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
                
menu_Principal = {
	1: ingreso_matrices,
	2: multiplicar_Matrices,
    }
    
def run():
    while True:
        n=int(input("1)Agregar Matriz \n2)Con multiplicacion \n3)Matriz Ejemplo \n4)Salir\n5)Mostrar Matrices Creadas\n-------> "))
        try:
            menu_Principal.get(n)()
        except:
            if n==3:
                matriz_ejemplo=[[1,2,3],[4,5,6],[7,8,9]]
                determinante_matriz(matriz_ejemplo)
            elif n==4:
                print("Cerrando Aplicacion :p")
                break
            elif n==5:
                for i in matrices.keys():
                    print("---------",i,"--------\n")
                    for j in matrices[i]:
                        print(j,"\n")            
            else:
                print("Ingrese un valor valido")
if __name__ == '__main__':
    run()
