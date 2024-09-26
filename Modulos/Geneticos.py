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
    iter=0
    print(poblacion)
    for i in range(p):
        # print(i+1,": ",np.random.randint(1,p))
        # print(i+1,": ",np.random.rand())
        poblacion[i]=np.arange(0,n)
        np.random.shuffle(poblacion[i])
    
    for repi in range(1,ite+1):
        hijos=np.zeros((p,n),int)
        print("\n")
        print(poblacion)
        # fitness
        fitness = np.zeros(p,int)


        
        for k in range(p):
            for i in range(n-1):
                for j in range(i+1,n):
                    if(np.absolute(poblacion[k][i]-poblacion[k][j])==np.absolute(i-j) or poblacion[k][i]==poblacion[k][j]):
                        fitness[k] +=1
        if repi == 1:
            bestf=np.amin(fitness)
            bestfp=np.where(fitness==bestf)[0]
        else:
            if bestf>np.amin(fitness):
                bestf=np.amin(fitness)
                bestfp=np.where(fitness==bestf)[0]

        
        #ruleta
        prob=np.cumsum(fitness/fitness.sum())  
        print (prob)
        #Crusa
        rep = 0
        while rep<p :

            ale = np.random.rand()
            for t in range (p):
                if ale< prob[t]:
                    padre1 = poblacion[t]
                    break
            ale2 = np.random.rand()

            for t in range(p):
                if ale2<prob[t]:
                    padre2 = poblacion[t]

            if np.random.rand()<pc:
                print (padre1)
                print (padre2)
                corte = np.random.randint(1,n)
                print(corte)
                hijo1= np.concatenate((padre1[:corte],padre2[corte:]))
                hijo2= np.concatenate((padre2[:corte],padre1[corte:]))
                print ("Hijo 1:  \n",hijo1,"\nHijo 2: \n",hijo2)
                #Mutacion
                if np.random.rand()<pm:
                    pto1=np.random.choice(n,size=2,replace=False)
                    hijo1[pto1[0]] , hijo1[pto1[1]] = hijo1[pto1[1]] , hijo1[pto1[0]] 
                    
                if np.random.rand()<pm:
                    pto2=np.random.choice(n,size=2,replace=False)
                    hijo2[pto2[0]] , hijo2[pto2[1]] = hijo2[pto2[1]] , hijo2[pto2[0]] 

            
                for i in range(n-1):
                    for j in range(i+1,n):
                        if hijo1[i]==hijo1[j]:
                            for y in range (n):
                                if y not in hijo1:
                                    hijo1[j]=y
                        if hijo2[i]==hijo2[j]:
                            for ds in range (n):
                                if ds not in hijo2:
                                    hijo2[j]=ds
        
                print(hijo1,"\n",hijo2)
                if p-rep>1:
                    hijos[rep]=hijo1
                    hijos[rep+1]=hijo2
                    rep +=2
                else:
                    if np.random.rand()<0.5:
                        hijos[t]=hijo1
                    else:
                        hijos[t]=hijo2

                    rep +=1
        print (hijos)
      
        print("mejo fitness: ",bestf,"Posicion: ",bestfp)
        print("Tablero:\n",poblacion[bestfp])
        poblacion = hijos
        

       
 

    
        
else:
    print("Error, el tablero es demasiado pequeño.")
    print("Se devio de ingresar un tablero de al menos 8")
    sys.exit(0)
