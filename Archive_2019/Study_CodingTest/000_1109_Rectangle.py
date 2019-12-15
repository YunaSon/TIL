inputdata = [[1,1], [4,8], [4,1]]
expected_result = [1,8]

def solution(inputdata):
    xs =[]
    ys =[]
    result = []

    for i in range(len(inputdata)):
        xs.append(inputdatgia[i][0])
    for i in range(len(inputdata)):
        ys.append(inputdata[i][1])
    
    if xs[0] != xs[1]:
        if xs[0] == xs[2]:
            result.append(xs[1])
        else:
            result.append(xs[0])
    else:
        result.append(xs[2])
    
    if ys[0] != ys[1]:
        if ys[0] == ys[2]:
            result.append(ys[1])
        else:
            result.append(ys[0])
    else:
        result.append(ys[2])    

    return result

print(solution(inputdata))
