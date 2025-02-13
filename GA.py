import pygame
import random
import numpy as np
from Bird import Bird
from Pipe import Pipe
from Floor import Floor

class GA:
    def __init__(self, population_size, mutation_rate):
        self.image = pygame.image.load('assets/bluebird-midflap.png')
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = []
        self.generation = 1

    def create_population(self):
        self.population = []
        for i in range(self.population_size):
            self.population.append(Bird(50, 144, self.image)) 
    
    def fitness(self):
        fitnesses = np.array([bird.survival_time for bird in self.population])
        total_fitness = np.sum(fitnesses)
        if total_fitness == 0:
            return np.ones(self.population_size)
        return fitnesses 

    def selection(self):
        fitnesses = self.fitness()
        idx = np.random.choice(self.population_size, 2, p=fitnesses/fitnesses.sum())
        return self.population[idx[0]], self.population[idx[1]]


    def crossover(self, parent1, parent2):
        weights1_ih, bias1_h, weights1_ho, bias1_o = parent1.get_brain().get_weights()
        weights2_ih, bias2_h, weights2_ho, bias2_o = parent2.get_brain().get_weights()

        alpha = 0.5
        new_weights_ih = alpha * weights1_ih + (1 - alpha) * weights2_ih
        new_bias_h = alpha * bias1_h + (1 - alpha) * bias2_h
        new_weights_ho = alpha * weights1_ho + (1 - alpha) * weights2_ho
        new_bias_o = alpha * bias1_o + (1 - alpha) * bias2_o

        new_bird = Bird(50, 144, self.image)
        new_bird.get_brain().set_weights(new_weights_ih, new_bias_h, new_weights_ho, new_bias_o)

        return new_bird

    def mutation(self):
        for bird in self.population:
            if random.random() < self.mutation_rate:  
                weights_ih, bias_h, weights_ho, bias_o = bird.brain.get_weights()
                weights_ih += np.random.randn(*weights_ih.shape) * 0.1  
                bias_h += np.random.randn(*bias_h.shape) * 0.1
                weights_ho += np.random.randn(*weights_ho.shape) * 0.1
                bias_o += np.random.randn(*bias_o.shape) * 0.1
                bird.get_brain().set_weights(weights_ih, bias_h, weights_ho, bias_o)

    
    def evolve(self):
        print(f"Generation {self.generation}: Best Fitness = {max(self.fitness())}")
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = self.selection()
            new_population.append(self.crossover(parent1, parent2))
        self.population = new_population
        self.mutation()
        self.generation += 1
