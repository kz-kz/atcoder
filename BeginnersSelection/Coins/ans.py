A,B,C,X = [int(input()) for i in range(4)]
ans = 0
for i in range(A + 1):
    if i*500 > X: break
    for j in range(B + 1):
        if i*500 + j*100 > X: break
        for k in range(C + 1):
            if i*500+j*100+k*50 == X:
                ans+=1
print(f'{ans}')
