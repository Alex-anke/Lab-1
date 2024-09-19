def draw_line(offset, step, color = 7):

    line = " "
    print(f'{' ' * (offset-2*int(step))} \x1b[48;5;{color}m{line}\x1b[0m', f'{' ' * (2*int(step))} \x1b[48;5;{color}m{line}\x1b[0m')

def ugol():
    height = 7
    center = height
    offset = height*4
    step = 0
    for line in range(height):
        draw_line(offset, step, color=7)
        offset+=int(step)
        step= step+(step+2)/2






if __name__ == "__main__":
    ugol()
