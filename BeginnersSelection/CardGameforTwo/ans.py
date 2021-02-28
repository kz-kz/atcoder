def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))

    pointsAlice = []
    pointsBob = []

    player = 'alice'

    for i in range(len(A)):
        if (player == 'alice'):
            pointsAlice.append(max(A))
            A.pop(A.index(max(A)))
        elif (player == 'bob'):
            pointsBob.append(max(A))
            A.pop(A.index(max(A)))

        if (player == 'alice'):
            player = 'bob'
        elif (player == 'bob'):
             player = 'alice'

    print(f'{sum(pointsAlice) - sum(pointsBob)}')

main()
