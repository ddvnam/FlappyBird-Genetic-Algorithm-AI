# FlappyBird-Genetic-Algorithm-AI

## Overview

This project implements a genetic algorithm combined with a neural network to train an AI agent to play the game Flappy Bird. Inspired by a Flappy Bird game developed during an advanced programming course, this project aims to enable the bird to navigate through obstacles without any player input autonomously. By applying a genetic algorithm, the neural network controlling the bird evolves over generations to improve its performance.

## Features

- **Genetic Algorithm**: Evolves a population of birds using selection, crossover, and mutation to optimize gameplay performance.
- **Neural Network**: A simple feedforward neural network controls each bird’s decision to flap based on game state inputs (Distance to next pipe, height difference from gap center, velocity).
- **Real-Time Visualization**: Displays the Flappy Bird game with multiple AI-controlled birds using the Pygame library, allowing users to observe the learning process in real time.
- **Fitness Function**: Evaluates each bird based on its survival time, aiming to maximize it.

## Installation

### Prerequisites
- Python 3.x
- Pygame (`pip install pygame`)
- NumPy (`pip install numpy`) for matrix operations in the genetic algorithm

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ddvnam/FlappyBird-Genetic-Algorithm-AI.git
   cd FlappyBird-Genetic-Algorithm-AI
   ```

3. Run the training file Game.py to observe the training process::
   ```bash
   python Game.py
   ```

## Technical Details

### Genetic Algorithm
- **Population**: Initializes a set of birds (e.g., 20–100), each with random decision-making parameters or neural network weights.
- **Inputs**:
  - Horizontal distance to the next pipe
  - Vertical distance between the bird and the center of the pipe gap
  - Bird’s vertical velocity
- **Fitness Function**: The fitness of each bird is measured by its survival time in the game.
- **Evolution**:
  - **Selection**: Parents are selected using the roulette wheel method, where two birds are chosen randomly with probabilities based on their fitness compared to the total fitness.
  - **Crossover**: Average parameters of parent birds to create offspring.
  - **Mutation**: Introduces random changes to maintain diversity, preventing premature convergence.

