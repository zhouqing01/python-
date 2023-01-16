def turtle(coord, direction):
    cur_direction = direction
    command = ""
    while True:
        command = yield coord
        #print(command)
        if command == 'f':
            if cur_direction == 0:
                coord = (coord[0]+1,coord[1])
            elif cur_direction == 1:
                coord = (coord[0],coord[1]+1)
            elif cur_direction == 2:
                coord = (coord[0]-1,coord[1])
            else:
                coord = (coord[0],coord[1]-1)
        elif command == 'l':
            cur_direction = (cur_direction + 1) % 4
        else:
            cur_direction = (cur_direction - 1) % 4
        # print(cur_direction)
        # print(cur_coord[0], cur_coord[1])
        # print(command)
        

# robo = turtle((0,0),0)
# start = next(robo)
# for c in "flfrffrffr":
#     print(*robo.send(c))


# x, a, c, m = 3, 1366, 1283, 6075 
# robo = turtle((0, 0), 0)
# next(robo)
# for cmd in ("ffflr"[(x:=(a*x+c)%m)//2%5] for i in range(200)):
#     res = robo.send(cmd)
# print(res)
