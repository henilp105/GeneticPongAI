from game import Game
from geneticai import GeneticAlgorithm

# Initialize the game and genetic algorithm
game = Game()
genetic_algorithm = GeneticAlgorithm(population_size=20, mutation_rate=0.1)

# Training loop
for generation in range(100):  # Run for 100 generations
    scores = [genetic_algorithm.evaluate(game, net) for net in genetic_algorithm.population]
    print(f'Generation {generation}, Best Score: {max(scores)}')
    
    selected = genetic_algorithm.select(scores)
    genetic_algorithm.create_new_generation(selected)
