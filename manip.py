print ("RELOAD SUCCESSFUL")

reset = True
dx = 0
dy = 0

def trig(x, y, rx, ry, hat0x, hat0y):
    global reset, dx, dy
    if reset:
        if rx < 50:
            dx = dx + 100
            reset = False
        if rx > 200:
            dx = dx - 100
            reset = False
        if ry < 50:
            dy = dy + 100
            reset = False
        if ry > 200:
            dy = dy - 100
            reset = False
    else:
        if rx > 100 and rx < 150 and ry > 100 and ry < 150:
            reset = True
    print (dx, dy, reset)
    return (int(x+dx),int(y+dy))
