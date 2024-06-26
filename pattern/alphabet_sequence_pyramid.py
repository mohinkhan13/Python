for i in range (10):    
    print(" "*(10-i),end="")
    for j in range(65,65+i):
        print((chr(j) + " "),end="")
    print()
