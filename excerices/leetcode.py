s = "abacabad"
dict = {}

def solution(string):
    for i in range(len(string)):
        dict[string[i]] = 1 + dict.get(string[i], 0)
    
    return "_"



print(solution(s))
print(dict)
