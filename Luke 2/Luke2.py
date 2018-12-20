from ast import literal_eval

with open("input-rain.txt","r") as f:
    content = list(map(lambda x: x.replace(";",","), f.read().split("\n")))
cordinates = [literal_eval(i) for i in content]
slope_dict = {}
for cord in cordinates:
    x1, y1 = cord[0]
    x2, y2 = cord[1]
    slope = abs((y2-y1)/(x2-x1))
    slope_dict[slope] = slope_dict.get(slope,0)+1
print(cordinates)
print(max(slope_dict.values()))