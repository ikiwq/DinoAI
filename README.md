# Dino-AI
This is a reacreation of the Chrome Dino game on python using pygame.
The game is played by an AI using the NEAT library.

The game is set to reset for each new generation, and the AI tries to maximize its fitness score through trial and error. The fitness is incremented by 0.1 in the update function for every frame the AI survives. If the AI collides with an obstacle, the fitness decreases by 10.

The neural network takes three inputs: the coordinates of the dinosaur, the coordinates of the nearest obstacle, and a Boolean indicating whether the dinosaur can jump or not. The output is a single value. If the value exceeds a previously set threshold, the dinosaur will jump.

### Screenshots
<img src="https://github.com/ikiwq/DinoAI/assets/110495658/9d28e663-cfbc-42d2-ad89-80554518fcbd" width=600>

## Requirements
- Python version 3.11 or higher. Download python from the official website [here](https://www.python.org/)https://www.python.org/.
- Pygame. Install pygame by running ```pip install pygame```
- NEAT. Install pygame by running ```pip install neat-python```

## Usage
Clone the repository in any directory by typing into your terminal

    https://github.com/ikiwq/DinoAI.git

After navigating into your chosen directory, run the main file:

    py main.py

## License

This project is licensed under the MIT License.
