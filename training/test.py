print("Hello World!")

# printとは出力関数であり表示したい文字列や数値などの値を画面に表示させる
# ()の中に値を入れると、その値を表示する

print(100-1)

# 出力結果
# 99

# 演算子の種類
# + 足し算
# * 掛け算
# - 引き算
# / 割り算
# // 割り算(少数部分を切り捨て)
# % 割り算の余り

print("答えは", 10+20)
# 出力結果
# 答えは 30

# 2文字以上は文字列という
# 「,(カンマ)」で区切ると複数の値を並べて表示できる

print("こんにちは、太郎さん。 ")
print("今日はいい天気ですね。 ")

# 出力結果
# こんにちは、太郎さん。
# 今日はいい天気ですね。

import random
kuji = ["大吉", "中吉","小吉","凶"]
print(random.choice(kuji))

# 出力結果(実行するたびに違った結果が表示される)
# 中吉・大吉・小吉・凶

# importとは、Pythonで使えるようにあらかじめ作られたモジュールを、自分のプログラムで使うために取り込む命令のこと。
# モジュールとは.pyで書かれたファイル。