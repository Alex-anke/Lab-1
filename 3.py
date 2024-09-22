def draw_line(offset, step):

    line = " "
    print(" "*(offset-int(step)), "\x1b[48;5;124m ", "\x1b[m", "\b", " "*2*step, "\b"*2, "\x1b[48;5;124m ", "\x1b[m")

def ugol():
    height = 5
    offset = height*4
    step = 0
    print(" " * (offset - int(step)+2), "\x1b[48;5;124m", "\x1b[m")
    for center in range(height, 0, -1):
        draw_line(offset, step)
        if center==height:
            step=1
        step = step * 2
n=40
while n>0:
    if __name__ == "__main__":
        ugol()
    n-=1