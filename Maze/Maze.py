'''
To generate a "hedgemaze" by first generating a correct path
then connecting the empty parts to the original path
'''
import random

size = 38,38 #x,y

start = 0
end = 0

maze_parts = ["_","_|","|", "|_"]

seen = []
seen_index = 0
maze = []

previous_move = (-1,0) #y,x
directions = [(1,0),(0,1),(-1,0),(0,-1)] #y,x

def move(location):
    #randomly select aa direction other than the previous
    global previous_move, seen

    valid = []
    for i in directions:
        if i != previous_move:
            print(location[0] + i[0],location[1] + i[1])
            if maze[location[0] + i[0]][location[1] + i[1]] != "BBB":
                if not [location[0] + i[0],location[1] + i[1]] in seen:
                    valid += [(i[0], i[1])]
    print(valid)
    if valid == []:
        return [0]
    
    temp = random.choice(valid)

    if temp[0] != 0:#offsets
        one_wall = (0,1)
        other_wall = (0,-1)
    else:
        one_wall = (1,0)
        other_wall = (-1,0)
    if not [location[0]+one_wall[0],location[1]+one_wall[1]] in seen:
        maze[location[0]+one_wall[0]][location[1]+one_wall[1]] = "BBB"
    if not [location[0]+other_wall[0],location[1]+other_wall[1]] in seen:
        maze[location[0]+other_wall[0]][location[1]+other_wall[1]] = "BBB"
    
    previous_move = (-temp[0],-temp[1])
    seen += [[location[0]+temp[0], location[1]+temp[1]]]
    return [location[0]+temp[0], location[1]+temp[1]]

def generate_path():
    global seen
    start = random.randrange(size[1])
    maze[0][start] = ""
    maze[1][start] = ""

    seen += [[0,start],[1,start]]
    
    location = [1,start] #y,x

    while location[0] < size[1] - 1 and location != [0]:
        location = move(location)
        
    return

def print_maze():
    for i in maze:
        for j in i:
            if len(j):
                print("["+str(j)+"]", end="")
            else:
                print("[   ]", end="")
        print()
    return

def reset_seen():
    seen = []
    return

def generate_maze():
    global maze
    reset_seen()
    for y in range(size[1]):
        maze += [[]]
        for x in range(size[0]):
            if y == 0 or x == 0 or x == size[0]-1 or y == size[1]-1:
                maze[y] += ["BBB"]
            else:
                maze[y] += [[]]
    return

def main():
    generate_maze()
    generate_path()
    print_maze()
    print(seen)
    return

main()
