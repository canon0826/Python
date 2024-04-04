# データ型を変換
# int(文字列)  文字列型を整数型に変換
# float(文字列)  文字列型を浮動小数点型に変換
# str(数値)  数値型や浮動小数点数型を文字列型の変換

a = "100"
print(int(a)+23)

# 出力結果
# 123

# int()を使用して文字列を整数に変換

a = "100"
b = "こんにちは"
print(a.isdigit())
print(b.isdigit())

# チェックしたい変数.isdigit()

# 出力結果
# True
# False

b = "こんにちは"
if b.isdigit():
    print(int(b)+23)
else:
    print("数値ではない")

# 出力結果
# 数値ではない
# if文は条件によって異なる処理を行う際使用する