print(1,2,3, end=' end__start ')
print(1,2,3, end='\n')
print(1,2,3, sep='|', end="\n")
print(1,2,3, sep='\n')

a = 1
b = 2
print('content', a,'content',b,'content')       # ,a,
print('content %s content %s content'%(a, b))   # %s
print(f'content {a} content {b} content')       # {a}

#enter symbol between elements
x=input()
print(1,2,3,4,5, sep=x)
print(input().join('12345'))
print(1, 2, 3, 4, 5, sep=input())
print(*range(1,5), sep=input())
print(f"1{x}2{x}3{x}4{x}5")



