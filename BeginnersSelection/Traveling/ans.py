# [可能]なパターンを考える
# パターン1.総移動量と移動時間が等しい場合(両方とも単位が1なので)
# パターン2.総移動量が移動時間より少ない
#              且つ、
#          総移動時間からゴール地点の総移動量を差し引いた余分な移動時間を使ってゴール地点に戻れる場合
#          ※進む/戻るを繰り返し(つまり2回移動を繰り返す)ゴールの地点に戻れる ≒　余分な移動時間が偶数である
# それ以外のパターンは[不可能]
# 日本語を数式化
#          総移動量          = abs(x - startX) + abs(y - startY)
#          移動時間          = t - startT
#               移動を開始した時間と場所からの差分をとる(初期はすべて0、2回目以降は直前ののゴール地点/時間となる)
#               移動量はマイナスパターンがあるので絶対値(abs)にて計算
#
#          余分な移動時間を使ってゴール地点に戻れる ≒　余分な移動時間が偶数である
#                           = ((t - startT) - (abs(x -startX) + abs(y -startY))) % 2 == 0
#
# よって条件式は:
#   パターン1
#       abs(x - startX) + abs(y - startY) == (t - startT)
#   パターン2
#       t - startT > abs(x - startX) + abs(y - startY)
#           and
#       ((t - startT) - (abs(x -startX) + abs(y -startY))) % 2 == 0


def main() -> None:
    startT = 0
    startX = 0
    startY = 0
    for i in range(int(input())):
        t,x,y = map(int,input().split())
        if (abs(x - startX) + abs(y - startY) == (t - startT) or (t - startT > abs(x - startX) + abs(y - startY) and ((t - startT) - (abs(x -startX) + abs(y -startY))) % 2 == 0)):
            #print(f't:{t} x:{x}y :{y}')
            #print(f'移動時間:{t - startT} 移動距離(X):{abs(x - startX)} y :移動距離(Y){abs(y - startY)}')
            startX = x
            startY = y
            startT = t
            pass
        else:
            print(f'No')
            exit()
    print(f'Yes')
 
 
main()
