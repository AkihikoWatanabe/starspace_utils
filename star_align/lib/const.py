# coding=utf-8

from collections import namedtuple
import re


Case = namedtuple("Case", ["label", "words"])
Pred = namedtuple("Pred", ["exid", "lhs", "rhs", "conf1", "conf2", "label1", "label2"])

# patten for binary classification
example_patt = "Example (?P<exid>\d+):"
lhs_patt = "LHS:\n(?P<lhs>.*?)"
rhs_patt = "RHS: \n(?P<rhs>.*?)"
pred_patt1 = "Predictions: \n\([\+\-]{2}\) \[(?P<conf1>[\-\d\.e]+)\]\t(?P<label1>.*?)"
pred_patt2 = "\([\+\-]{2}\) \[(?P<conf2>[\-\d\.e]+)\]\t(?P<label2>.*?)"

predfile_patt = re.compile("{example}\n{lhs}\n{rhs}\n{pred1}\n{pred2}(?:\n|$)".format(
    example=example_patt,
    lhs=lhs_patt,
    rhs=rhs_patt,
    pred1=pred_patt1,
    pred2=pred_patt2)
)


class Const():

    # default parameter
    DEFAULT_PROCESSNUM = 4

    # delimiter
    VOCAB_DLMTR = "\t"
    LABEL_DLMTR = "\t"
    WORD_DLMTR = " "
    EOL = "\n"

    # list index
    RHS = 1
    LHS = 0
