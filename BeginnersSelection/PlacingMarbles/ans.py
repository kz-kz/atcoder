def isOne(boxNum: int) -> bool:
    if (boxNum == 1):
        return True
    else:
        return False

def main() -> None:
    ans = 0
    boxes = list(map(int,input()))
    for i in range(len(boxes)):
        if (isOne(boxes[i]) == True):
            ans+=1
        else:
            pass
    print(f'{ans}')

main()
