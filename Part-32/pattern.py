
def star_pattern():
    for x in range(1, 6):
        for y in range(1, x+1):
            print("*", end="")
        print("")


star_pattern()
