import sys
import numpy as np # type: ignore

if len(sys.argv)==7:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2])
    p = int(sys.argv[3])
    ite = int(sys.argv[4])
    pc = float(sys.argv[5])/100
    pm = float(sys.argv[6])/100
    print(semilla, n, p, ite, pc, pm)

   
else:
    print("Error entrada de los parametros")
    print("Los parámetors son: semilla, tamaño del tablero, tamaño población iteraciones...")
    sys.exit(0)
if n>=8:
    np.random.seed(semilla)
    poblacion = np.zeros((p,n),int)
    print(poblacion)
    for i in range(p):
        # print(i+1,": ",np.random.randint(1,p))
        # print(i+1,": ",np.random.rand())
        poblacion[i]=np.arange(0,n)
        np.random.shuffle(poblacion[i])
    
    print("\n")
    print(poblacion)
    # fitness
    fitness = np.zeros(p,int)


    
    for k in range(p):
        for i in range(n-1):
            for j in range(i+1,n):
                if(np.absolute(poblacion[k][i]-poblacion[k][j])==np.absolute(i-j) or poblacion[k][i]==poblacion[k][j]):
                    fitness[k] +=1
  

    
    #ruleta
    prob=np.cumsum(fitness/fitness.sum())  
    print (prob)
    #Crusa
    ale = np.random.rand()
    for t in range (p):
        if ale< prob[t]:
            padre1 = poblacion[t]
            break
    ale2 = np.random.rand()

    for t in range(p):
        if ale2<prob[t]:
            padre2 = poblacion[t]

    
    print (padre1)
    print (padre2)
    corte = np.random.randint(1,n)
    print(corte)
    #hijo11 = padre1[:corte]
    #hijo12 = padre2[corte:]
    #hijo21 = padre2[:corte]
    #hijo22 = padre1[corte:]
    hijo1= np.concatenate((padre1[:corte],padre2[corte:]))
    hijo2= np.concatenate((padre2[:corte],padre1[corte:]))
    print ("Hijo 1:  \n",hijo1,"\nHijo 2: \n",hijo2)
    #Mutacion
    pto1=np.random.choice(n,size=2,replace=False)
    pto2=np.random.choice(n,size=2,replace=False)
    print(pto1,"\n",pto2)
    hijo1[pto1[0]] , hijo1[pto1[1]] = hijo1[pto1[1]] , hijo1[pto1[0]] 
    hijo1[pto2[0]] , hijo1[pto2[1]] = hijo1[pto2[1]] , hijo1[pto2[0]] 
    for i in range(n-1):
        for j in range(i+1,n):
            if hijo1[i]==hijo1[j]:
                hijo[j]=

    print(hijo1,"\n",hijo2)
    

    
        



    
else:
    print("Error, el tablero es demasiado pequeño.")
    print("Se devio de ingresar un tablero de al menos 8")
    sys.exit(0)
