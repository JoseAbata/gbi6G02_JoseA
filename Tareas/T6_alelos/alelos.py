
# FUNCIÓN 1. Creación de la población
import scipy # for random numbers

def build_population(N, p):
    """ Para la construccion de la población se tiene las variables "N" que representa el numero de individuos que contentria la poblacion, mientas "p" es a probabilidad de obtener el alelo dominante.
    En este modulo, se llama a scipy para generar una probabilidad al azar, y servira para generar los pares de alelos de los individuos de forma aleatorio. 
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

# FUNCIÓN 2. Cuantificación de frecuencias de alelos
def compute_frequencies(population):
    """ En la funcion 2. se cuenta los fenotipos de individuos pertenecientes a la población, y regresa un diccionario de frecuencias genotípicas.
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

# FUNCIÓN 3. Creacion de la población hijo
def reproduce_population(population):
    """La funcion 3. Crea una funcion hijo, atravez de problabilidad, donde:
    - Se seleccionan los padres de forma aleatoria.
    - La descendencia tiene un cromosoma de cada uno de sus padres.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation