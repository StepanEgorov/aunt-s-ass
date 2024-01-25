def fun(s : str)->str:
    while '555' in s or '888' in s:
        s = s.replace('555','8',1)
        s = s.replace('888','55',1)
    return s

s = '5'*101
s = fun(s)
print(s)