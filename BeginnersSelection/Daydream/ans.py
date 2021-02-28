def main() -> None:
    S = input()
    T = ''
    keywords = ("eraser","erase","dreamer","dream")

    for keyword in keywords:
        S = S.replace(keyword,"")
    if (S == ''):
        print(f'YES')
    else:
        print(f'NO')


main()