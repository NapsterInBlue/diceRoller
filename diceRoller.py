'''
Upon rolling two 6-sided dice, we want to apply a function to determine the 
probability of meeting or exceeding the target, given a certain number
and an existing modifier
Ex: main(6, sum, 1)
    Pr(d1 + d2 + 1 >= 6)
>>> .833333333
Ex: main(7, max, 0)
    Pr(max(d1, d2) + 0 >= 7)
>>> 0.0
'''


def allCombos():
    comboList = []

    for x in range(1,7):
        die1 = x
        for y in range(1,7):
            die2 = y
            tup = (die1,die2)
            comboList.append(tup)

    return comboList


def vals(fn, combos):
    dict_of_vals = {}
    for combo in combos:
        result = fn(combo)
        if result in dict_of_vals:
            dict_of_vals[result] += 1
        else:
            dict_of_vals[result] = 1
    return dict_of_vals

	
def cdf(dist, target, mod):
    '''
    For a given dist and target, what percent of values fall below it
    '''
    total = sum(dist.values())
    leq = 0
    for key in dist:
        if key >= (target - mod):
            leq += dist[key]
    return leq / float(total) 
    

def main(target, fn, mod=0):
    combos = allCombos()
    values = vals(fn, combos)
    return cdf(values, target, mod)