stall = input()
liter_milk = 0
for i in range(len(stall) - 1):
    if stall[i] == 'b':
        liter_milk += (i + 1) * 2
print(liter_milk)