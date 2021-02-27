def sumupDigits(num: int) -> int:
    array = list(map(int, str(num)))
    return sum(array)

def main() -> None:
    A,B,C = map(int,input().split())
    counter = 0

    l = list(range(A+1))
    for i in range(len(l)):
        digits = sumupDigits(l[i])
        if ((digits >= B) == True & (digits <= C) == True):
            counter = counter + l[i]

    print(f'{counter}')

main()
