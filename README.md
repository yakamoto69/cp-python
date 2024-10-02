## SetUp
- python3のinstall
- pypy3のinstall
- pipでいろいろinstall (これ以外で何はいっているのかわからない...)
  - atcoder-library
  - atcoder-tools
  - oj
  - sortedcontainers

#### コンテストのテンプレを生成 (例ABC296の場合)
```
cd atcoder
atcoder-tools gen abc296 --workspace . --lang python
```

#### テスト実行するには、problemのフォルダにcdして
```
atcoder-tools test
```

#### サブミットは、problemのフォルダにcdして
```
atcoder-tools submit
```
でもHTMLの構成が変わったのか、エラーがでる


#### AtCoderLibraryを使う時は、以下のコマンドで提出ようのコードを作ります
```
python -m atcoder main.py -o main_gen.py
```


#### AtCoderLibraryのコードのimport例[main.py](hackercup2023%2Fpractice_round%2FA1%2Fmain.py)
```
from atcoder.dsu import DSU
```