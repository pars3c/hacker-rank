# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

similar = True
def solution(S, T):
    # write your code in Python 3.6
    for i, t in enumerate(T):
        try:
            if t == S[i]:
                continue
            
            elif t != S[i] and S[i+1] == t and len(S) != len(T):
                similar = False
                return ('INSERT ' + t)
            elif t != S[i] and S[i+1] != t:
                similar = False
                return ('REPLACE ' + S[i] + ' ' + t)
            elif t != S[i] and S[i+1] == t and S[i] == T[i+1]:
                similar = False
                return ('SWAP ' + S[i] + ' ' + t)
            
            else:
                similar = False
                return ('IMPOSSIBLE')
        except:
            similar = False
            return ('IMPOSSIBLE')
    if similar == True:
        return ('EQUAL')