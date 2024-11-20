def draw_flag():
    width = int(input("введите ширину "))
    height = int(input("введите высоту (кратную 6) "))
    for i in range(height//6):
        print("\x1b[48;5;124m  " * width, "\x1b[m")
    for i in range(height // 6):
        print("\x1b[48;5;255m  " * width, "\x1b[m")
    for i in range(height // 3):
        print("\x1b[48;5;18m  " * width, "\x1b[m")
    for i in range(height // 6):
        print("\x1b[48;5;255m  " * width, "\x1b[m")
    for i in range(height//6):
        print("\x1b[48;5;124m  " * width, "\x1b[m")



if __name__ == "__main__":
    draw_flag()
