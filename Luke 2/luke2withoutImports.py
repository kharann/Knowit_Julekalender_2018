with open("input-rain.txt","r") as f:
    content = list(map(lambda x: x.replace("(","").replace(")","").split(";"), f.read().split("\n")))
slope_dict = {}
for cord in content:
    x1, y1 = [int(i) for i in cord[0].split(",")]
    x2, y2 = [int(i) for i in cord[1].split(",")]
    slope = ((y2-y1)/(x2-x1))
    slope_dict[slope] = slope_dict.get(slope,0)+1
print(max(slope_dict.values()))