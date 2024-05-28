import random
from model import PaddleNet
import torch

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = [PaddleNet() for _ in range(population_size)]

    def evaluate(self, game, net):
        game.reset()
        state = game.get_state()
        done = False
        while not done:
            state_tensor = torch.FloatTensor(state)
            with torch.no_grad():
                move = net(state_tensor).item()
            move = move * 10  # Scale movement
            done = game.update(move)
            state = game.get_state()
        return game.score

    def select(self, scores):
        # print(self.population)
        sorted_population = [x for _, x in sorted(zip(scores, self.population),key=lambda x: x[0], reverse=True)]
        return sorted_population[:self.population_size//2]

    def crossover(self, parent1, parent2):
        child = PaddleNet()
        for child_param, param1, param2 in zip(child.parameters(), parent1.parameters(), parent2.parameters()):
            mask = torch.bernoulli(torch.full_like(param1, 0.5))
            child_param.data.copy_(mask * param1 + (1 - mask) * param2)
        return child

    def mutate(self, net):
        for param in net.parameters():
            mutation_mask = torch.bernoulli(torch.full_like(param, self.mutation_rate))
            param.data.add_(mutation_mask * torch.randn_like(param))

    def create_new_generation(self, selected):
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = random.sample(selected, 2)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        self.population = new_population
