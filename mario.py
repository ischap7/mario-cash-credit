while(True):
    height = int(input("Height: "))
    if height <= 8 and height >= 1:
        break
    else:
        print("nope")

for block in range(height+1):
    print( (height-(block) )*" " + (block* "#") )
   
