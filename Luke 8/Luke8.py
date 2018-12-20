def initDollList():
    with open("input-dools.txt","r") as f:
        data = [doll.split(",") for doll in f.read().split("\n")] 
    dolls = list(map(lambda x: [x[0], int(x[1])] ,data))
    return sorted(data,key = lambda x: x[1], reverse = True)

def findBiggestDoll(dolls):
    biggestDoll = [dolls[0]]
    for doll in dolls:
        dollColor, dollSize = doll
        isEmpty = len(biggestDoll) == 0
        if not isEmpty and dollColor != biggestDoll[-1][0] and dollSize < biggestDoll[-1][1]:
            biggestDoll.append(doll)
    return biggestDoll

doll_list = initDollList()
print(len(findBiggestDoll(doll_list))+1)