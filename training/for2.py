# for文 リストを指定
# for 要素を入れる変数 in リスト:
#     繰り返す処理

scorelist = [64,100,78,80,72]
for i in scorelist:
    print(i)

# 出力結果
# 64
# 100
# 78
# 80
# 72

# リスト(scorelist)の中の合計を求める
scorelist = [64,100,78,80,72]
total = 0
for i in scorelist:
    total = total + i
print(total)

# 出力結果
# 394

# for文 (入れ子)  内側のfor文が全てくり返し終わるまでくり返す

# for カウント変数1 in range(回数):
#     for カウント変数2 in range(回数):
#         くり返す処理

for i in range(10):
    for j in range(10):
        print(j,"x",i,"=",j*i)