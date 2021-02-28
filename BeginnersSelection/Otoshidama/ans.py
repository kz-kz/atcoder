def main() -> None:
    N,Y = map(int,input().split())
    Y //=1000
    found = False

    for yukichi in range(N+1):
        for ichiyo in range(N+1 - yukichi):
            #print(yukichi,ichiyo,(N - (yukichi+ichiyo)))
            if (yukichi*10 + ichiyo*5 + (N - (yukichi+ichiyo)) == Y):
                print(yukichi,ichiyo,(N - (yukichi+ichiyo)))
                found = True
                exit()
    if (found == False):
        print(f'-1 -1 -1')

main()
