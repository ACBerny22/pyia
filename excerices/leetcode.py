s = "abacabad"
dict = {}

def solution(string):
    for i in range(len(string)):
        dict[string[i]] = 1 + dict.get(string[i], 0)
    
    for pair in dict:
        if pair[1] == 1:
            return pair[0]
    return "_"



print(solution(s))
