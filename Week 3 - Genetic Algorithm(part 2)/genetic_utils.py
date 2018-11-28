import numpy as np
from matplotlib.pyplot import pie
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

class Item:
    def __init__(self, value, weight) :
        self.value = value
        self.weight = weight

class Bag:
    def __init__(self, capacity) :
        self.capacity = capacity

class Chromosome :
    def __init__(self, length) :
        self.genes = np.random.rand(length) > .5
        self.fitness = float('-inf')
        
    def __len__(self) :
        return len(self.genes)
    
    def reset(self) :
        self.fitness = float('-inf')
        
def get_fake_knapsack(seed=0, max_value=30, max_weight=40, items_number=30):
    """
    Items & Bag capacity of fake knapsack problem will be generated and returned
    """
    np.random.seed(seed)
#     items_number = np.random.randint(items_number)
    # List Comprehensions, for more details see : https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
    items = np.array([Item(np.random.rand()*max_value, np.random.rand()*max_weight) for _ in range(items_number)])
    bag = Bag(np.random.rand()*(max_weight*len(items)) + max_weight)
    print('We have {} items with weight and values of :'.format(len(items)))
    for i,item in enumerate(items) :
        print('item {}: Weight=>{} Value=>{}'.format(i, item.weight, item.value))
    print('We have a bag with capacity of {}'.format(bag.capacity))
    return items, bag

# Population Initialization Method
population_init = lambda size, chrom_size : np.array([Chromosome(chrom_size) for _ in range(size)])


def fitness_eval(chrom, items, bag, epsilon=2) :
    selected_items = items[chrom.genes]
    capacity_full = 0
    fitness = 0
    for item in selected_items :
        capacity_full += item.weight
        if capacity_full > bag.capacity :
            fitness = epsilon
            break
        fitness += item.value
    return fitness

def roulette_selection(chromosomes, show_plot = False) :
    i = 0
    fitnesses = np.array(list(map(lambda c: c.fitness, chromosomes)))
    sum_of_fitnesses = np.sum(fitnesses)
    sel_prob = fitnesses/sum_of_fitnesses
    if show_plot:
        pie(sel_prob) # Ploting pie chart of probablity of each individual
    sum_prob = sel_prob[i]
    pointer = np.random.rand()
    while sum_prob < pointer :
        i += 1
        sum_prob += sel_prob[i]            
    return chromosomes[i]

tournament_selection = lambda chromosomes, sel_pressure: max(np.random.choice(chromosomes, sel_pressure),key=lambda c: c.fitness)

# First set up the figure, the axis, and the plot element we want to animate
def plot_generations(generations, fitnesses) :
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

    X = generations[:, :, 0]
    Y = generations[:, :, 1]

    # animation function.  This is called sequentially
    def animate(i):
        x = X[i]
        y = Y[i]
        ax.clear()
        scat = ax.scatter(x, y, s=fitnesses[i])
        ax.set_title('Generation {}'.format(i))
        return scat, ax

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, frames=generations.shape[0], interval=200)
    plt.close()
    # call our new function to display the animation
    return HTML(anim.to_jshtml())