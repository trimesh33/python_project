# Pacman Game
1st iteration

This game was implemented as original Pacman game as a project for python course (2nd semester, MIPT).

# How to run
```
git clone git@github.com:trimesh33/python_project.git
cd python_project
pip3 install -r requirements.txt
python3 main.py [<player_name> [<map_name>]]
```
player_name: without spaces

current maps name: classic, edited

# Game logic
## Ghost behavior
The are two mode of ghost behavior: scatter and chase.
### Common behavior
Scatter behavior: going to the target corner and making circles around it.
Chase described in the next block.

The are severals rounds of scatter and chase behavior:
| round | scatter time | chase time |
| :---: | :---: | :---: |
| 1     | 7     | 20        |
| 2     | 7     | 20        |
| 3     | 5     | 20        |
| 4     | 5     | $\infty$  |

### Individual behavior

| ghost | color | scatter corner | behavior | target cell |
| :---: | :---: | :---: | :---: | :---:|
| Blinky | red    | top right  | following pacman | pacman position |
| Pinky  | pink   | top left | advanced following pacman | 4 steps ahead of pacman in his current direction |
| Inky   | blue   | bottom right | wait until will be eaten at least 30 points, then running in random direction | if Blinky near pacman then Inky runs toward |
| Clyde  | orange | bottom left | wait until tow third of point eaten | if pacman further than 8 cells, targeting for corner, else behaves as Blinky |



(more precise explanation https://habr.com/ru/post/109406/)