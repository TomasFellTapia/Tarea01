# Tarea01
Tarea 1 AMIN.
Se desarolla un algoritmo genetico que resuelva el problema de las n-reinas mediante programacion modular en Python.
El algoritmo inicialmente genera una poblacion con los parametros enteros dados por sistema, siendo estos la semilla, el tamaño del tablero, este no aceptara valores menores a 8, el tamaño de la poblacion la cantidad de iteraciones que se realizaran, las probabilidad de cruza y la probabilidad de mutacion, en caso que fate uno de los parametros se mostrara un mensaje de error. Si no hay error se genera la poblacion inicial y se calculara el fitness inicial, luego se calcula el menor fitness y su posicion, luego se inicia el proceso de crusa mediante el cual se eligen al azar dos posibles padres y de aceptrce la cruza se eligira al azar un punto de cruza y se crearan dos hijos y se creara un arreglo con estos de dos en dos, en caso que la pobllacion sea impar se asignara aleatoriamente uno de los hijos al elemento final, luego se remplazara la poblacion inicial con la nueva y se repitira el proceso las veces que se especificaron en la cantidad de iteraciones, dando mensajes si se encontro una solucion satisfactoria o en caso contrario el que contenga el mejor fitness
Los parametros = "2 8 29 55 100 50" dieron una solución exitosa para un tablero de ajedrez real  