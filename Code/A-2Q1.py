
# when running give 0/1 as param
# 0 random population size
# 1 random bits length

from random import seed
from random import randint
from datetime import datetime
import sys
def generatePopulation(pop_size,chromo_len):
    population = []
    seed(datetime.now())
    for _ in range(pop_size):
        value = randint(1,(2**chromo_len) -1)
        population.append(value)
    return population
        
def fitness(population):
    population.pop(population.index(min(population)))
    population.append(max(population))
    population.sort()
    return population

def convert_to_binary(population,chromo_len):
    binary_pop = []
    for x in population:
        value    = bin(x)[2:]
        add_zero = chromo_len - len(value) 
        zero     = ['0' for x in range(add_zero)]
        zero     = ''.join(zero)
        value    = zero + value
        binary_pop.append(value)
        
    return binary_pop
    
def crossOver(population,chromo_len):
    binary_pop   = convert_to_binary(population,chromo_len)
    cross_point  = int(chromo_len/ 2)
    
    aftr_cross   = []
    right_cross  = []
    left_cross   = []
    for x in binary_pop:
        value = list(x)
        right = value[cross_point:]
        left  = value[:cross_point]
        right = ''.join(right)
        left = ''.join(left)
        right_cross.append(right)
        left_cross.append(left)
    
    for ind in range(len(right_cross)):
        value  = left_cross[ind] + right_cross[len(left_cross)-ind-1] 
        aftr_cross.append(value)

    return aftr_cross



def mutation(Population,chromo_len):
    mutat_pop = []
    seed(datetime.now())
    for x in population:
        ind = randint(0,chromo_len-1)
        value = list(x)
        value[ind] = str(int(not bool(int(value[ind]))))
        value = ''.join(value)
        mutat_pop.append(value)
    return mutat_pop

    
def convert_to_int(population):
    binary = '0b'
    for ind in range(len(population)):
        population[ind] = binary + population[ind]
        population[ind] = int(population[ind],2)

        
    return population

def stop(population,chromo_len):
    population  = convert_to_int(population)
    try:
        population.index((2**chromo_len)-1)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    argv = sys.argv[1:]
    X = []
    Y = []
    for i in range(4,13,2):
        if argv[0] is '0':
            pop_size   = i
            chromo_len = 8
            print('Population Size : ',pop_size)
            print('Chromosome Length : ',chromo_len)
        else:
            pop_size   = 4
            chromo_len = i*2
            print('Population Size : ',pop_size)
            print('Chromosome Length : ',chromo_len)
        population = generatePopulation(pop_size,chromo_len)
        
        print('Initial Population',convert_to_binary(population,chromo_len))
        
        iteration  = 0
        while True:
            iteration += 1
            population = fitness(population)
            population = crossOver(population,chromo_len)
            population = mutation(population,chromo_len)
            if stop(population,chromo_len):
                break
        print('Final Population : ',convert_to_binary(population,chromo_len))
        print('Iteration : ',iteration)
        print('Fitness : ',((2**chromo_len) -1))
        print('\n************************************************************************************************************************************\n')

