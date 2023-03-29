# Dino-AI
This is a reacreation of the Chrome Dino game on python using pygame.
The game is played by an AI using the NEAT library.

The game is set to reset for each new generation, and the AI tries to maximize its fitness score through trial and error. The fitness is incremented by 0.1 in the update function for every frame the AI survives. If the AI collides with an obstacle, the fitness decreases by 10.

The neural network takes three inputs: the coordinates of the dinosaur, the coordinates of the nearest obstacle, and a Boolean indicating whether the dinosaur can jump or not. The output is a single value. If the value exceeds a previously set threshold, the dinosaur will jump.
