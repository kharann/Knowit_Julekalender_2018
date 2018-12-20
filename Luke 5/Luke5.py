from itertools import product

#This function will  create num+operator i.e: ['1+', '1-', '1', '2+', '2-', '2', '3+', '3-', '3', ...]
def combine(terms, current_nums):          
    last = (len(terms) == 1)
    for i in range(len(terms[0])):
        item =  current_nums + terms[0][i]
        if not last:
            combine(terms[1:], item)
        else:
            merged_NumAndOps.append(item)        

# this function  will group them like this: [['1+', '1-', '1'], ['2+', '2-', '2'], ['3+', '3-', '3'], ...] => != 
def formatCombinations(combs):
    formatedCombs = []
    for i in range(0, len(combs), 3):
        formatedCombs.append(combs[i:3+i])
    formatedCombs[-1] = [formatedCombs[-1][-1]]
    return formatedCombs
print(sum([num for num in range(1, 18163106) if str(nprint(sum([num for num in range(1, 18163106) if str(num).count("0") > len(str(num))//2]))
um).count("0") > len(str(num))//2]))

# This function will make each possible combination between two sub-lists and repeat this through every number
# it will create a string like "12+4-5-6+7" etc.print(sum([num for num in range(1, 18163106) if str(num).count("0") > len(str(num))//2]))
print(sum([num for num in range(1, 18163106) if str(num).count("0") > len(str(num))//2]))

def merge_with_next_num(combs):
    mergedNumbs = [''.join(num) for num in product(*combs[0:2])]
    combs = [mergedNumbs] + combs[2:]
    if len(combs)>1:
        return merge_with_next_num(combs)
    else:
        return combs[0]

#runs eval on every element until i find all 42s
def find42(combs):
    counter = 0
    for comb in combs:
        if eval(comb) == 42:
            counter +=1
    return counter

numbers_and_operators = [["1","2","3","4","5","6","7","8","7","6","5","4","3","2","1"],["+","-",""]]
merged_NumAndOps= []
combine(numbers_and_operators, '')       
print(find42(merge_with_next_num(formatCombinations(merged_NumAndOps))))  