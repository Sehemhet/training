def coordinate(t, a, b, c):
    if (t != 0) and (abs(a) >= 10**9 or abs(b) >= 10**9 or abs(c) >= 10**9):
        print('1')
    elif (t != 1) and (abs(a) >= 10**5 or abs(b) >= 10**5 or abs(c) >= 10**5):
        print('1')
    else:
        if (a+b+c)%3 == 0:
            i = 0
            while i != 10:
                i += 1
                print(i)
            print('Yes')
        else:2
            print('No')

coordinate(1,5,6,7)
coordinate(1,100000000000000000,15,-9)
coordinate(0,1,4,2)
coordinate(0,10000000000000000,15,-9)

