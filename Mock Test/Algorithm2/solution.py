def solution(arr):
    lst = []
    arr_len = len(arr)
    for i in range(1, arr_len + 1):
        lst.append(i)
    arr.sort()
    if(lst == arr) : return True
    else: return False

T =  [4,1,3,2]
F = [4,1,3]

print('Testing T List : {}'.format(solution(T)))
print('Testing F List : {}'.format(solution(F)))

