import re, math

with open("lol.txt") as f:
    birth_yr = [int(yr) for yr in re.findall(r'\d+', f.read())]
current_yr = [yr + 1 for yr in birth_yr]
upper_limit = round(math.sqrt(max(birth_yr)+50))

def find_gold_birthdays(current_yr, birth_yr, age_limit, counter):
    del_amount = 0
    for i in range(len(current_yr)):
        index = i - del_amount
        age = current_yr[index] - birth_yr[index]
        if age**2 == current_yr[index]:
            counter += 1
            del_amount += 1
            del birth_yr[index], current_yr[index]
        else:
            current_yr[index] += 1
    if age_limit < upper_limit:
        return find_gold_birthdays(current_yr,birth_yr,age_limit + 1,counter)
    return counter

print(find_gold_birthdays(current_yr,birth_yr,0,0))


    
        

