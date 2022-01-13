# 10 반복문

for i in range(10):
    print(i)
    
#0~9가 0 1 2 3 4 5 6 7 8 9 (옆으로 나오게) 출력
for i in range(10):
    print(i, end=' ')
    
print()#결과창 줄바꿈용

#0, 1, 2..., 8, 9 (마지막 , 안나오게)
for i in range(10):
    if i<9:
        print(i, end=', ')
    else:
        print(i)
        
# 4~21 홀수 합
sum = 0
for i in range(4, 22):
    if i%2 == 1:
        sum += i

print(sum)
    
    
#1~100 짝수만 출력
for i in range(1, 101):
    if i%2 == 0:
        print(i, end=' ')
      
print( )
  
for i in range(2, 101, 2):
    print(i, end=' ')
    
print()
#2단~9단 구구단 출력 
for i in range(2, 10):
    for j in range(1, 10):
        print(i, ' x ', j, ' = ', i*j)
# (옆으로)
for i in range(1, 10):
    for j in range(2, 10):
        print(j, ' x ', i, ' = ', j*i, end=' ')
    print()
    
print()

#리스트 요소 출력, 가로로
lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator']

for i in range(len(lst)):
    print(lst[i], end=' ')
    
print()

#리스트 거꾸로 출력
for i in lst[ : : -1]: #[ start : last : step] <- step = -1 이어서 거꾸로 한칸씩 (-2이면 거꾸로 2칸씩)
    #print(lst[i], end=' ') <- range() 를 쓴게 아닌 lst를 직접 사용했기 때문에 i에 배열 값이 직접 들어간다.
    print(i, end=' ')