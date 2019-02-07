# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    my_list = sorted(list(S))
    
    if len(my_list) <= 3:
            return int(len(S))
    else:
        for i in range(len(my_list)):
            try:
                del my_list[i+1]
            except:
                break
                
        S = (''.join(my_list))
        return int(len(S))
            
        