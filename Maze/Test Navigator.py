#Import all libraries we will use
import random
import numpy as np
import cv2
from time import process_time

png_input = "Maze220x220"
image = cv2.imread(png_input+".png")
size = len(image)
path = []

linked_dict={}

def pathfinder(location):
    while linked_dict[location]:
        image[linked_dict[location][0]][linked_dict[location][1]][1] = 0
        image[linked_dict[location][0]][linked_dict[location][1]][2] = 0
        location = linked_dict[location]
    return

def bfs(location, path):
    # generates a linked list using dictionaries of parents and ending once the exit is found
    # then back tracing from the exit to the start
    linked_dict[location] = []
    location = (location[0]+1, location[1])
    linked_dict[location] = (location[0]-1, location[1])
    queue = [location]
    while location[0] < size-1:
        adjacent = [(location[0], location[1] - 1),(location[0] + 1, location[1]),(location[0], location[1] + 1),(location[0] - 1, location[1])]
        for i in adjacent:
            if i[0] < size and i[1] < size:
                if i not in linked_dict and image[i[0]][i[1]][0] == 255 :
                    queue.append(i)
                    linked_dict[i] = location
        queue.pop(0)
        location = queue[0]

    pathfinder(location)
    
    return []

def draw(path):
    for i in path:
        image[i[0]][i[1]][1] = 0
        image[i[0]][i[1]][2] = 0
    return

def dfs(location, path):
    seen = {location: [(location[0]+1,location[1])]}
    path = [location]
    while location[0] < size-1:
        if location in seen:
            if len(seen[location]) > 0:
                if location != path[-1]:
                    path.append(location)
                location = seen[location].pop(0)
                path.append(location)
            else:
                location = path.pop()
        else:
            adjacent = [(location[0], location[1] - 1),(location[0] + 1, location[1]),(location[0], location[1] + 1),(location[0] - 1, location[1])]
            valid = []
            for i in adjacent:
                if i[0] < size and i[1] < size:
                    if i not in seen and image[i[0]][i[1]][0] == 255:
                        valid.append(i)
            seen[location] = valid.copy()
                        
    return path

def start(image):
    for i in range(len(image[1])):
        if image[0][i][0] == 255:
            return i

def main():
    global path
    location = (0,start(image)) #y,x
    print(location)
    
    #path = dfs(location, path)
    #draw(path)
   
    bfs(location, path)
    
    cv2.imwrite(png_input+"Solve.png",image)
    print(process_time())

main()
