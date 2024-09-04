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





    