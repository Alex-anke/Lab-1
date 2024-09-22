def draw_line(step):
    print(" "*int(step*50), "\x1b[48;5;124m ", "\x1b[m")


def graf():
    height = 50
    step = 0.2
    for koory in range(height, 0, -1):
        draw_line(step)
        step = 10/koory


if __name__ == "__main__":
    graf()
