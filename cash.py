while(True):
    change_owed = float(input("change owed: "))
    if change_owed >= 0:
        break
    else:
        print("nope")

cents = round(change_owed * 100)
num_coins = 0
 
#num of quarters
while cents >= 25:
    cents -= 25
    num_coins += 1

while cents >= 10:
    cents -= 10
    num_coins += 1

while cents >= 5:
    cents -= 5
    num_coins += 1

while cents >= 1:
    cents -= 1
    num_coins += 1

print(num_coins)
        
