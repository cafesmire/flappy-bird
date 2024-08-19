# Flappy Bird Game

This is a Python implementation of the classic Flappy Bird game using the Pygame library.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [File Structure](#file-structure)
- [Game Logic](#game-logic)
- [Acknowledgments](#acknowledgments)

## Features

- Classic Flappy Bird gameplay.
- Simple yet engaging graphics.
- Collision detection with pipes and the ground.
- Score tracking and display.
- Game Over and Start screens.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/cafesmire/flappy-bird.git
   ```

2. **Navigate to the Project Directory:**

   ```sh
   cd flappy-bird
   ```

3. **Install Dependencies:**

   Make sure you have Python and Pygame installed. You can install Pygame using pip:

   ```sh
   pip install pygame
   ```

4. **Run the Game:**

   ```sh
   python main.py
   ```

## How to Play

- Press the `SPACE` key to start the game.
- Press the `SPACE` key to flap the bird's wings and keep it in the air.
- Avoid the pipes and the ground to keep the bird alive.
- Press `ESC` during the game over screen to restart the game.

## File Structure

The project consists of the following files:

- **`assets.py`**: Handles loading and retrieving game assets like images.
- **`background.py`**: Manages the background scrolling.
- **`bird.py`**: Contains the Bird class, handling bird animation, movement, and collision detection.
- **`config.py`**: Holds game configuration values like screen dimensions, gravity, and FPS.
- **`floor.py`**: Manages the floor scrolling and collision detection.
- **`gamemessage.py`**: Displays the game start/game over message.
- **`layer.py`**: Defines the layers for sprite rendering order.
- **`main.py`**: The main entry point of the game, handling game logic, events, and rendering.
- **`pipe.py`**: Manages the pipe obstacles, their movement, and collision detection.
- **`score.py`**: Handles the score display and updating.

## Game Logic

- **Bird Movement:** The bird falls with gravity and can be made to rise by pressing the `SPACE` key.
- **Pipes:** Pipes move from right to left, and the bird must pass through the gaps without colliding.
- **Collision Detection:** The game checks for collisions between the bird and pipes or the ground.
- **Score:** The score increases each time the bird successfully passes through a set of pipes.

## Acknowledgments

- **Pygame**: The game was developed using the Pygame library.
- **Flappy Bird**: This game is inspired by the original Flappy Bird game created by Dong Nguyen.

---
