import ita
#ライフゲーム

def count_neighbor(data, i, j):
    #i行目j列の周囲の8マスの生命数をカウント！
    count = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if (0 <= k < len(data) and 0 <= l < len(data[k])):
                count = count + data[k][l]

    return count - data[i][j]


def lifegame_rule(cur, neighbor):
    #次の世代のi行目j列が生存か否か。
    #cur:セルの現在状態　　neighbor:周囲の生命数
    if cur == 0:
        if neighbor == 3:
            return 1
        else:
            return 0
    else:
        if neighbor == 2 or neighbor == 3:
            return 1
        else:
            return 0


def lifegame_step(data):
    new_data = ita.array.make2d(len(data), len(data[0]))
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            n = count_neighbor(data, i, j)
            new_data[i][j] = lifegame_rule(data[i][j], n)
            #ルールにのっとり次世代を計算
    return new_data


def lifegame(data, steps):
    results = ita.array.make1d(steps)
    for i in range(0, steps):
        results[i] = data
        data = lifegame_step(data)
    return results

x = [[0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,0,0,0,0],[1,1,0,1,0,0,0,0,1,0,0,0],[1,1,0,1,0,0,1,0,1,0,0,0],[0,0,0,1,0,0,1,0,1,0,1,1],[0,0,0,1,0,1,0,0,1,0,1,1],[0,0,0,0,1,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0]]
ani = lifegame(x, 10)
ita.plot.animation_show(ani)
