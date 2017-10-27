# StarSpaceのためのユーティリティツール
[StarSpace](https://github.com/facebookresearch/StarSpace)はtestモードを用いることで、未知のデータに対して、学習したEmbeddingに基づいて分類等を行うことができる。  
このとき、テストデータ中の事例が未知語のみで構成されていると、読み込みの段階でその事例はロードされず、分類結果がpredictionFile中にoutputされなくなってしまう（hit@nの計算にも使用されない）。  
この結果、predictionFile中の事例IDが、inputと対応しなくなるため、inputとpredictionFile中の事例の対応がとりづらい。  
また、predictionFileには、input中の各事例が記載されるが、事例中の未知語は飛ばして記載されるため、inputとpredictionFileの事例間のExact Matchを行うことができない。  
ので、inputとpredictionFileに含まれる事例の対応を取るユーティリティツールを作成する。

# Usage
```
$ python star_align.py test_file prediction_file vocab_file {RHS,LHS} > output
```
