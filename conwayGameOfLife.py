import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import sys, argparse

ALIVE = 255
DEAD = 0
vals = [ALIVE, DEAD]

# add specfic pattern
def addGliderPattern(i, j, grid):
    glider = np.array([[0, 0, 255], 
                       [255, 0, 255], 
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
    
# add box pattern
def addBoxPattern(i,j,grid):
    box = np.array([[ALIVE, ALIVE],
                    [ALIVE, ALIVE]])
    grid[i:i+2, j:j+2] = box 

# add blinker pattern
def addBlinkerPattern(i,j,grid):
    blinker = np.array([[DEAD, ALIVE, DEAD],
                        [DEAD, ALIVE, DEAD],
                        [DEAD, ALIVE, DEAD]])
    grid[i:i+3, j:j+3] = blinker
    
# find total alive neighbors
def findTotalAliveNeighbors(i, j, grid, gridSize):
    totalAliveNeighbors = 0
    
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if( (x < 0 or  y < 0 or x >= gridSize or y >= gridSize) or ( x == i and y == j)):
                continue

            if(grid[x][y] == ALIVE):
                totalAliveNeighbors += 1
    
    return totalAliveNeighbors

# updating the grid
def updateGrid(frameNum, img, grid, gridSize):
    updatedGrid = grid.copy()
    
    for i in range(gridSize):
        for j in range(gridSize):
            aliveNeighbors = findTotalAliveNeighbors(i, j, grid, gridSize)
    
            if grid[i][j] == ALIVE:
                if aliveNeighbors < 2 or aliveNeighbors > 3:
                    updatedGrid[i][j] = DEAD
                else: 
                    updatedGrid[i][j] = ALIVE
            else:
                if aliveNeighbors == 3:
                    updatedGrid[i][j] = ALIVE
                else:
                    updatedGrid[i][j] = DEAD
    
    img.set_data(updatedGrid)
    grid[:] = updatedGrid[:]
    return img,    
            
    
def main():
    
    # will convert it into flags later on
    gridSize = 10
    probForAlive = 0.2
    updateInterval = 50
    
    # taking as input from flags
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--grid-size', dest='gridSize', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--prob-for-alive', dest='probForAlive', required=False)
    parser.add_argument('--pattern', dest='pattern', required=False)
    args = parser.parse_args()
    
    if args.gridSize and int(args.gridSize) > 4:
        gridSize = int(args.gridSize)
    
    if args.interval:
        updateInterval = int(args.interval)
    
    if args.probForAlive:
        probForAlive = float(args.probForAlive)
    
    # setting up the grid
    fig, ax = plt.subplots()
    grid = np.random.choice([0, 255], gridSize*gridSize, p= [ 1 - probForAlive, probForAlive ]).reshape( gridSize, gridSize )
    
    if args.pattern == 'glider':
        addGliderPattern(1, 1, grid)
    elif args.pattern == 'box':
        addBoxPattern(1, 1, grid)
    elif args.pattern == 'blinker':
        addBlinkerPattern(1, 1, grid)
    
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, updateGrid, fargs=(img, grid, gridSize, ), frames=10, interval=updateInterval, save_count=50)
    plt.show()    
        
if __name__ == '__main__':
    main()
    