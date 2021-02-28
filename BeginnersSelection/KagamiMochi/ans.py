def main() -> None:
    N = int(input())
    D = list(int(input()) for i in range(N))
    currentStepValue = 0
    currentStepNum = 0

    for i in range(len(D)):
        #print(f'現在の配列の状況{D}')
        #print(f'鏡餅の段数{currentStepNum}')
        #print(f'現在の餅の大きさ{currentStepValue}')
        if (currentStepValue == 0):
            currentStepValue = max(D)
            currentStepNum +=1
            D.pop(D.index(max(D)))
        elif (currentStepValue == max(D)):
            D.pop(D.index(max(D)))
        else:
            currentStepValue = max(D)
            D.pop(D.index(max(D)))
            currentStepNum +=1
    #print(f'最終的な鏡餅の段数{currentStepNum}')
    print(f'{currentStepNum}')

main()
