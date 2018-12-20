nums_and_operators = []
def combine(terms, current_nums, nums):
    last = (len(terms) == 1)
    for i in range(len(terms[0])):
        item =  current_nums + terms[0][i]
        if not last:
            combine(terms[1:], item)
        else:
            nums_and_operators.append(item) 

a = [["1","2","3"],["+","-",""]]
nums = []
combine(a, '', nums)
print(nums_and_operators)