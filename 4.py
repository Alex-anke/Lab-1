f = open("sequence.txt")


def diagram():
    one = 0
    two = 0
    for element in f:
        element = float(element)
        if element < 0 or element==5:
            pass
        elif element > 5:
            one += 1
        else:
            two += 1
    print("больше пяти ", "\x1b[48;5;120m " * (one * 100 // (one + two)),
          "\x1b[m", round(one * 100 / (one + two), 2), "%")
    print()
    print("меньше пяти ", "\x1b[48;5;120m " * (two * 100 // (one + two)),
          "\x1b[m", round(two * 100 / (one + two), 2), "%")
    print()
    print("                       10", "20", '30', '40', '50', '60', '70', '80', '90', "100", sep=' '*8, end=" %")


if __name__ == "__main__":
    diagram()


f.close()
