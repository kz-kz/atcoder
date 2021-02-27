def hasOdd(arr: list) -> bool:
    if (len([i for i in arr if not i % 2 == 0]) == 0):
        return False
    else:
        return True


def hasZero(arr: list) -> bool:
    if (len([i for i in arr if i == 0]) == 0):
        return False
    else:
        return True


def main() -> None:
    num = int(input()) #1行目無視
    arrays = list(map(int, input().split()))
    counter = 0
    oddFlg = False

    while True:
        l_zero = [i for i in arrays if i == 0]
        if (hasOdd(arrays) == False & hasZero(arrays) == False):
            counter +=1
            arrays = [j//2 for j in arrays]
        else:
            break

    print(f'{counter}')


main()
