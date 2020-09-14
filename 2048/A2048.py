'''
Text Based 2048
with a gimmick being that if the direction you are moving does not move the edge in the direction you are moving
it will swap with the opposing edge if the move is a valid standard 2048 move
'''


import random
import math
import time
from pynput import keyboard

size = 8 #will at some point support more than 4x4
tiles = []
previous_tiles = []
empty = []

def set_empty():
    global empty
    empty = []
    for y in range(size):
        for x in range(size):
            if tiles[y][x] == []:
                empty += [(y,x)]

def print_tiles():
    for i in tiles:
        for j in i:
            if j == []:
                print("|" + 8 * " " + "|", end = "")
            else:
                print(("|") + (4 - math.floor(len(str(j[0]))/2)) * " " + str(j[0]) + (4 - math.ceil(len(str(j[0]))/2)) * " " + "|", end = "")
        print()

def on_release(key):
    if key == keyboard.Key.esc:
        print("Stopped")
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        move(k)
        print()
        print("_"*10*size)
        print_tiles()         
        print('Key pressed: ' + k)
        time.sleep(0.1)
        #return False  # stop listener; remove this if want more keys

#listener = keyboard.Listener(on_press=on_press)
#listener.start()  # start to listen on a separate thread
#listener.join()  # remove if main thread is polling self.keys

def check_state(): #checks for valid moves
    for i in range(size):
        for j in range(size):
            if i != size-1:
                if tiles[i][j][0] == tiles[i+1][j][0]:
                    return
            if j != size-1:
                if tiles[i][j][0] == tiles[i][j+1][0]:
                    return
    reset()
    print("No More Valid Positions")
    return

def flip(direction):
    copy_tiles() #update previous_tiles to be copied from
    if direction[0] != 0: #Set order (should probably be hardcoded in at some point)
        one_side = (0,0)
        other_side = (size-1,0)
        increment = (0,1)
    else:
        one_side = (0,0)
        other_side = (0, size-1)
        increment = (1,0)

    print(other_side)
    
    return

def merge(direction):
    if direction[0] != 0:
        other_axis = (0,1)
        if direction[0] > 0:
            offset = (3,0)
        else:
            offset = (0,0)
    else:
        other_axis = (1,0)
        if direction[1] > 0:
            offset = (0,3)
        else:
            offset = (0,0)
            
    for i in range(1,size):
        for j in range(size):
            select_tiles = offset[0] - i * direction[0] + j * other_axis[0] , offset[1] - i * direction[1] + j * other_axis[1]
            destination = offset[0] - (i-1) * direction[0] + j * other_axis[0] , offset[1] - (i-1) * direction[1] + j * other_axis[1]
            if tiles[select_tiles[0]][select_tiles[1]] != [] and tiles[select_tiles[0]][select_tiles[1]] == tiles[destination[0]][destination[1]]:
                tiles[destination[0]][destination[1]][0] += tiles[destination[0]][destination[1]][0]
                tiles[select_tiles[0]][select_tiles[1]] = []
            
    return    

def add_tiles():
    try:
        set_empty()
        y,x = random.choice(empty)
        tiles[y][x] += random.choices([2,4],[9,1])
    except:
        print("No more valid positions")
        reset()

def calc_destination(direction, coordinate):
    destination = coordinate
    while destination[0] >= 0 and destination[1] >= 0 and destination[0] <= size-1 and destination[1] <= size-1: #limits edges
        if tiles[destination[0]][destination[1]] != [] and destination != coordinate: #test if destination is empty or not
            break
        else:
            destination = destination[0] + direction[0], destination[1] + direction[1]
    return destination[0] - direction[0], destination[1] - direction[1]

def move_tiles(direction):
    if direction[0] != 0: #Set order (should probably be hardcoded in at some point)
        other_axis = (0,1)
        if direction[0] > 0:
            offset = (size-1,0)
        else:
            offset = (0,0)
    else:
        other_axis = (1,0)
        if direction[1] > 0:
            offset = (0,size-1)
        else:
            offset = (0,0)
            
    for i in range(size):
        for j in range(size):
            select_tiles = offset[0] - i * direction[0] + j * other_axis[0] , offset[1] - i * direction[1] + j * other_axis[1]
            if tiles[select_tiles[0]][select_tiles[1]] != []:
                destination = calc_destination(direction, select_tiles)
                if destination != select_tiles:
                    tiles[destination[0]][destination[1]] += tiles[select_tiles[0]][select_tiles[1]]
                    tiles[select_tiles[0]][select_tiles[1]] = []
            
    return

def copy_tiles():
    for i in range(size):
        for j in range(size):
            previous_tiles[i][j] = tiles[i][j].copy() 
    return

def move(k):
    direction = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)} #(y,x)
    copy_tiles()
    move_tiles(direction[k])
    merge(direction[k])
    move_tiles(direction[k])
    if previous_tiles != tiles:
        add_tiles()
        flip(direction[k])
    else:
        set_empty()
        if empty == []:
            check_state()
    return

def reset():
    tiles_consturctor()
    add_tiles()
    add_tiles()

def tiles_consturctor():
    global tiles
    global previous_tiles
    for x in [tiles,previous_tiles]:
        for i in range(size):
            x += [[]]
            for j in range(size):
                x[i] += [[]]
    return

def main():
    reset()
    listener = keyboard.Listener(on_release=on_release)
    listener.start()  # start to listen on a separate thread
    print_tiles()
    return

def addNewTile(tiles, filled):
    
    return tiles

main()
