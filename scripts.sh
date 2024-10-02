# AtCoderのコンテスト情報をとってくる
atcoder-tools gen abc218 --workspace . --lang python

# ↑の後、問題の階層まで移動する
# > cd abc218
# > cd A

# テスト実行
atcoder-tools test

# atcoder-libraryを埋め込んだコードを生成する
python -m atcoder main.py -o main_gen.py


# AtCoder以外のコンテストの場合
# > mkdir contest-name
# > cd contest-name
# > mkdir round-name
# > cd round-name
# > mkdir A
# > cd A
# > touch main.py
# > mkdir tests
# > pbpaste > tests/1.in
# > pbpaste > tests/1.out

# テスト実行
oj t -c "python3 ./main.py" -d ./tests/

# Meta Hacker Cupの場合のアウトプット出力
cat input.txt | python3 main.py > out.txt

# TODO
- Hacker Cup対策でpypyで実行できるようにする
- その際にpypyの起動コマンドをこのドキュメントに記載する