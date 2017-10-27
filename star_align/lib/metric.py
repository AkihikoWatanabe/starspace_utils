# coding=utf-8

"""
各種Metricを計算するモジュール
"""


def hit(golds, cands, n=1):
    """ hit@nを計算する関数

    Params:
        golds (list): 正解ラベルのリスト
        cands (list): top-kの推定ラベルを要素として持つリスト
        n (int): 上位何件までmetricの計算に考慮するか

    Returns:
        float: 算出したhit@nの値
    """

    return sum([1.0 if g in cands[i][:n] else 0.0 for i, g in enumerate(golds)]) / len(golds)
