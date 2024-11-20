def draw_line(step, height):
    print(" "*int(step*height), "\x1b[48;5;124m ", "\x1b[m")


def graph():
    height = 50
    step = 0.2
    for coord in range(height, 0, -1):
        draw_line(step, height)
        step = 10/coord


if __name__ == "__main__":
    graph()
