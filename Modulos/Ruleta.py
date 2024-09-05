def crearRuleta(p,fitnes):
    prob=fitness/fitness.sum()  
    #crear ruleta
    for i in range(1,p):
        prob[i]=prob[i]+prob[i-1]
        print(prob)