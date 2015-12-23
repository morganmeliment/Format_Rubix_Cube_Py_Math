rubix = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
miniface = 0
for x in range(0,54):
    side = (x - (x % 9)) / 9
    num = ((x - (x % 21))/21 - (x - (x % 42))/42 + (x - (x % 33))/33 - ((x - (x % 45))/45) * 2) * -33
    twonum = 0
    if x >= 9 and x < 45:
        twonum = ((x - (x % 3))/3 - 3) * 6
    indent = False
    if (x + 1) % 3 == 0 and (x < 9 or x > 44) and x != 8:
        print(rubix[(int(x + num + twonum) - (int(x + num + twonum) % 9)) / 9][int(x + num + twonum) % 9])
    elif x == 20 or x == 32:
        print(rubix[(int(x + num + twonum) - (int(x + num + twonum) % 9)) / 9][int(x + num + twonum) % 9])
    elif x == 8 or x == 44:
        print(rubix[(int(x + num + twonum) - (int(x + num + twonum) % 9)) / 9][int(x + num + twonum) % 9])
        print("")
    elif x % 3 == 0 and (x < 9 or x > 44):
        print("       " + str(rubix[(int(x + num + twonum) - (int(x + num + twonum) % 9)) / 9][int(x + num + twonum) % 9]), end = " ")
    elif (x + 1) % 3 == 0 and x > 8 and x < 45:
        print(rubix[(int(x + num + twonum) - (int(x + num + twonum) % 9)) / 9][int(x + num + twonum) % 9], end = "  ")
    else:
        print(rubix[(int(x + num + twonum) - (int(x + num + twonum) % 9)) / 9][int(x + num + twonum) % 9], end = " ")
