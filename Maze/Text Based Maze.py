'''
To generate a "hedgemaze" by first generating a correct path
then connecting the empty parts to the original path currently uses text representation
'''
import random
import time

size = 220,220 #x,y

start = 0
end = 0

seen = []
turns = []
seen_index = 0
maze = []

previous_move = (-1,0) #y,x
directions = [(1,0),(0,1),(-1,0),(0,-1)] #y,x

def move(location):
    #randomly select aa direction other than the previous
    global previous_move, seen, turns

    valid = []
    for i in directions:
        #if i != previous_move:
        #print(location[0] + i[0],location[1] + i[1])
        if location[0] + i[0] < size[1] and location[1] + i[1] < size[0]:
            if maze[location[0] + i[0]][location[1] + i[1]] != "BB":
                if not [location[0] + i[0],location[1] + i[1]] in seen:
                    valid += [(i[0], i[1])]
        else:
            seen += [[location[0],location[1]]]
            #print(seen)
            for x in range(size[0]):
                if not [size[1]-1,x] in seen:
                    #print([size[1]-1,x])
                    maze[size[1]-1][x] = "BB"
                else:
                    maze[size[1]-1][x] = ""
    #print(valid)
    
    if valid == []:
        if len(turns) > 0:
            return turns.pop()
        else:
            return [0]
    
    temp = random.choice(valid)

    if temp != [previous_move[0], previous_move[0]]:
        turns += [[location[0],location[1]]]
        
    if temp[0] != 0:#offsets
        one_wall = (0,1)
        other_wall = (0,-1)
    else:
        one_wall = (1,0)
        other_wall = (-1,0)
    if not [location[0]+one_wall[0],location[1]+one_wall[1]] in seen:
        maze[location[0]+one_wall[0]][location[1]+one_wall[1]] = "BB"
    if not [location[0]+other_wall[0],location[1]+other_wall[1]] in seen:
        maze[location[0]+other_wall[0]][location[1]+other_wall[1]] = "BB"
    
    #previous_move = (-temp[0],-temp[1])
    seen += [[location[0]+temp[0], location[1]+temp[1]]]
    return [location[0]+temp[0], location[1]+temp[1]]

def generate_path():
    global seen
    start = random.randrange(1,size[0]-2)

    maze[0][start] = ["  "]
    maze[1][start] = ["  "]
    
    seen += [[0,start],[1,start]]
    
    location = [1,start] #y,x

    while location != [0]:
        location = move(location)
        
    return

def print_maze():
    for i in maze:
        print(i)
    return

def reset_seen():
    seen = []
    return

def generate_edges():
    for i in range(size[0]):
        maze[i][0] = ["BB"]
        maze[i][-1] = ["BB"]
        seen.append([i,0])
        seen.append([i,size[1]])
    for j in range(size[1]):
        maze[0][j] = ["BB"]
        maze[-1][j] = ["BB"]
        seen.append([0,j])
        seen.append([size[0],j])
    return

def generate_maze():
    global maze
    reset_seen()

    for i in range(size[0]):
        maze.append(["  "])
        for j in range(size[1]):
            maze[i].append(["  "])
    generate_edges()
    return

def main():
    generate_maze()
    generate_path()
    #print_maze()
    print(time.process_time())
    print("done")
    return

main()
