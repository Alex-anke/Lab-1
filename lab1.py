# print("\x1b[31m hello")
#
# print("\x1b[35m hello")
#
# print("\x1b[31;1m hello") #жирный красный
#
# print("\x1b[38;5;157m hello") #жирный зеленый
#
# print("\x1b[48;5;157m   ") # все зеленое
#
# print("\x1b[48;5;200;38;5;2m hello  \x1b[48;5;56m fkgk  \x1b[m") # все зеленое
#
# # \x1b[48;5;0m все черное
#
# print("First line")
# print("second line\x1b[1A")
# print("3rst line")

'''def draw_line(offset=0, lenght=1):
    line = " " * lenght
    print(f'{' ' * offset} \x1b[48;5;222m{line}\x1b[0m')

def romb():
    height = 15
    center =height//2
    offset = height//2
    step = 1
    lenght = 1

    for line in range(height):
        draw_line(offset, lenght=lenght)
        if line < center:
            offset -= step
            lenght += step *2
        else:
            offset += step
            lenght -= step *2





if __name__ == "__main__":
    romb()'''

# import time
# def draw_line(offset=0, lenght=1, color = 222):
#
#     line = " " * lenght
#     print(f'{' ' * offset} \x1b[48;5;{color}m{line}\x1b[0m')
#
# def romb():
#     height = 15
#     center =height//2
#     offset = height//2
#     step = 1
#     lenght = 1
#     print(height, center, offset)
#     colors = [222, 157]
#     while True:
#         for color in colors:
#             for line in range(height):
#                 draw_line(offset, lenght, color)
#                 if line < center:
#                     offset -= step
#                     lenght += step *2
#                 else:
#                     offset += step
#                     lenght -= step *2
#             print(f'\x1b[{height}A')
#             print(f'\x1b[{offset}D')
#             lenght =1
#             offset = height//2
#             time.sleep(2)
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#     romb()

import time


def draw_line(offset=0, length=1, color=222):
    line = ' ' * length
    print(f'{" " * offset}\x1b[48;5;{color}m{line}\x1b[0m')


def romb():
    height = 15
    center = height//2
    offset = height//2
    step = 1
    length = 1
    print(height, center, offset)
    colors = [222, 157, 45,228, 134, 69]
    while True:
        for color in colors:
            for line in range(height):
                draw_line(offset, length, color)
                if line < center:
                    offset -= step
                    length += step*2
                else:
                    offset += step
                    length -= step*2
            print(f'\x1b[{height+2}A')
            print(f'\x1b[{offset}D')
            length = 1
            offset = height//2
            time.sleep(0.2)




if __name__ == '__main__':
    romb()