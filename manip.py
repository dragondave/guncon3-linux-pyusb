print ("RELOAD SUCCESSFUL")

top = -10000
left = -10000
right = 10000
bottom = 10000

def trig(x, y, calibrate):
    global left, right, top, bottom
    if calibrate:
        if x < -200:
            left = x
        if x > 2000:
            right = x
        if y < 4000:
            top = y
        if y > 5000:
            bottom = y
        print ("Calibration: ", left, right, top, bottom, x, y)
    width = right - left
    height = bottom - top
    percent_x = (x-left)/width
    percent_y = (y-top)/height
    print (percent_x, percent_y)
    new_x = int(percent_x*20000) - 10000
    new_y = int(percent_y*20000) - 10000
    print (new_x, new_y)
    return (new_x, new_y)