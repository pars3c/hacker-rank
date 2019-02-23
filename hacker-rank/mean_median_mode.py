import statistics
from heapq import nsmallest
ammount = int(input())
n = ammount
x = str(input())
results = x.split(' ')
results = list(map(float, results))
result_dic = [0] * len(results)
def mean(results, ammount):
    res = 0
    for result in results:
        res += result
        
    return round(res/ammount, 1)
    
def median(results):
    return round(statistics.median(results), 1)
        
def mode(results) :
    dict_list = zip(results, result_dic)
    my_dict = dict(dict_list)
    res_count = 0
    for i, res in enumerate(set(results)):
        res_count = results.count(res)
        my_dict[res] = res_count
    ammount = my_dict.get(max(my_dict, key=my_dict.get))
    smallest = min(nsmallest(3, my_dict, key=my_dict.get))
    return smallest
    


print(mean(results, ammount))

print(median(results))

print(mode(results))

