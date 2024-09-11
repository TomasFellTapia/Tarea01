def crearRuleta(fitness):
    return np.cumsum(fitness/fitness.sum())