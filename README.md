# Genetic Algorithm based Ping Pong AI

This repository contains a genetic algorithm implementation for training a neural network, `PaddleNet`, to play a simple paddle game. The code is written in Python and uses PyTorch for the neural network and numpy for state representation.

## Requirements

- Python 3.x
- PyTorch
- numpy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/henilp105/GeneticPongAI.git
   cd GeneticPongAI
   ```

2. Install the required packages:

   ```bash
   pip install torch numpy
   ```

## Usage

### Game Description

The game is a simple paddle game where a ball bounces around the screen, and the paddle must keep it from going off the screen. The paddle moves vertically, and the ball bounces off the walls and the paddle.

### Neural Network (PaddleNet)

The `PaddleNet` class defines a neural network with three fully connected layers. The input to the network is the current state of the game, and the output is the movement of the paddle.

### Genetic Algorithm

The `GeneticAlgorithm` class implements the genetic algorithm for training the `PaddleNet`. It includes methods for evaluation, selection, crossover, and mutation.

### Training Loop

The training loop initializes the game and the genetic algorithm and runs for a specified number of generations. Each generation evaluates the population, selects the best individuals, and creates a new generation through crossover and mutation.

