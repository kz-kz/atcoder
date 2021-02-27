def isEven(product :int) -> bool:
    if (product % 2 == 0):
        return True
    else:
        return False

def main() -> None:
    a,b = map(int, (input().split()))
    if (isEven(a*b) == True):
        print('Even')
    else:
        print('Odd')

main()
