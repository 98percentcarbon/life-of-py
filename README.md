![Life Of Py Logo](https://i.nuuls.com/IHaEL.png)


# life-of-py
A sandbox of Conway's Game of Life on a toroidal 37x37 grid with support for 'importing'/'exporting' states of the board. 
Made with lots of help from AI like ChatGPT. Toroidal means that objects hitting the left will emerge from the right, and objects hitting the bottom edge will emerge from the top.


### Prerequisites
- Python (any version is probably fine)
- Pygame library
- Numpy library


## Inputs
- Fullscreen - HI
- Mouse (LMB) - Place tiles 
- Space - Pause/Resume
  
- V - Very fast mode (On/Off, regardless of pause state)
- G - Gets the hex code of the current state of the board. 
- H - Hex code input. 
- C - Clear the board (Only when paused)

## How to play 
- The state of each cell (tile) evolves in discrete board-wide steps (generations).
- The rules for a cell in the next generation are based on its current state and the state of its neighbors (the tiles around it in a 3x3 grid):
- Birth: A dead cell with exactly three live neighbors becomes alive in the next generation.
- Survival: A live cell with two or three live neighbors survives to the next generation.
- Death: In all other cases, a cell dies or remains dead in the next generation.

## What makes Conway's Game of Life interesting?
- Conway's Game of Life is extremely simple in rules, but in practice it has an extreme depth, being turing-complete on a larger board, infamously, the game of life was played in itself.
- The states of the board before the current one are irrelevant, and the ones after are only predictable by simulating them.
- patterns and structures have been categorised into different classes, such as still life, oscillators, spaceships, and more.
- An great model/example of Chaos Theory, where initial conditions are extremely sensitive to the end result, and the result of each generation is completely deterministic. 

### Installation
```bash
git clone https://github.com/lainflux/life-of-py.git
