def solution(v):
    answer, x, y = [], [], []
    removex, removey = 0,0
    v_len = len(v)
    
    for i in range(v_len):
        x.append(v[i][0])
        y.append(v[i][1])
        
    for j in range(v_len):
        if(x.count(x[j]) == 2): removex = x[j]
        if(y.count(y[j]) == 2): removey = y[j]
        
    for k in range(2):
        x.remove(removex)
        y.remove(removey)

    answer = [x[0], y[0]]
    return answer
