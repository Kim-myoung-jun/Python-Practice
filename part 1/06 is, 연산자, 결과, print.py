#is, 연산자, 결과, print
a = "korea"
b = "korea"
print('a is b - ', a is b)

b += "!"
print('a is b - ', a is b)

c = b[:-1] #slice
print(c)
print('a is c - ', a is c)
'''
a is b -  True
a is b -  False
a is c -  False

문자열은 True
그 외에는 false가 맞다
'''
