
with open("input-dools.txt","r") as f:
    thicc = []
    if (doll[0] != thicc[-1][0] and dollsize < thicc[-1][1]) else for doll in sorted(list(map(lambda x: [x.split(",")[0],int(x.split(",")[1])], f.read().split("\n"))), key = lambda x: x[1], reverse = True)

def findBiggestDoll(dolls):
    biggestDoll = [dolls[0]]
    for doll in dolls:
        dollColor, dollSize = doll
        if dollColor != biggestDoll[-1][0] and dollSize < biggestDoll[-1][1]:
            biggestDoll.append(doll)
    return biggestDoll

print(len(findBiggestDoll(data))+1)