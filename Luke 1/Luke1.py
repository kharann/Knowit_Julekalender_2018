def vekkSort():
    with open("input-vekksort.txt","r") as f:
        data = list(map(lambda x: int(x), f.read().split("\n")))
    del_amount = 0
    for old_i in range(len(data)-1):
        new_i = old_i-del_amount
        if data[new_i] > data[new_i+1]:
            del data[new_i+1]
            del_amount += 1
    return sum(data)
print(vekkSort())