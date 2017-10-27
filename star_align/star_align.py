# coding=utf-8

import argparse
from collections import defaultdict
import re

from lib.const import Case, Pred, predfile_patt
from lib.const import Const as C


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument(
            "test_file",
            type=str
    )
    parser.add_argument(
            "prediction_file",
            type=str
    )
    parser.add_argument(
            "vocab",
            type=str
    )
    parser.add_argument(
            "label_side",
            choices=["LHS", "RHS"]
    )

    args = parser.parse_args()

    return args


def fetch_vocab(vocab_path):

    vocab = defaultdict(lambda: len(vocab))
    with open(vocab_path) as f:
        [vocab[l.split(C.VOCAB_DLMTR)[0]] for l in f.read().strip().split(C.EOL)]

    return vocab


def fetch_testfile(testfile_path, label_side):

    tests = []
    with open(testfile_path) as f:
        for l in f.read().strip().split(C.EOL):
            both_side = l.split(C.LABEL_DLMTR)
            label = both_side[C.RHS] if label_side == "RHS" else both_side[C.LHS]
            words = both_side[C.LHS].split(C.WORD_DLMTR) if label_side == "RHS" else both_side[C.RHS].split(C.WORD_DLMTR)
            tests.append(
                    Case(label, words)
            )

    return tests


def fetch_predfile(predfile_path):

    preds = []
    with open(predfile_path) as f:
        predfile_text = f.read().strip()
        for m in predfile_patt.finditer(predfile_text):
            p = Pred(
                    int(m.group("exid").strip()),
                    m.group("lhs").strip(),
                    m.group("rhs").strip(),
                    float(m.group("conf1").strip()),
                    float(m.group("conf2").strip()),
                    m.group("label1").strip(),
                    m.group("label2").strip()
            )
            preds.append(p)

    return preds


def validation_testcase():
    vocab = fetch_vocab(args.vocab)
    tests = fetch_testfile(args.test_file, args.label_side)

    testcase_valid = [True if sum([1 for w in case.words if w in vocab]) != 0 else False for case in tests]

    return testcase_valid


def output_result(pred_idx, test_idx, test_case, pred_case, label_side):

    print "Example {}:".format(pred_idx)
    print "testID:{}".format(test_idx)
    print "RAW LHS:"
    print "{}".format(" ".join(test_case.words) if label_side == "RHS" else test_case.label)
    print "RAW RHS:"
    print "{}".format(" ".join(test_case.words) if label_side == "LHS" else test_case.label)
    print "LHS:"
    print "{}".format(pred_case.lhs)
    print "RHS:"
    print "{}".format(pred_case.rhs)
    print "Predictions:"
    print "[{}]\t{}".format(pred_case.conf1, pred_case.label1)
    print "[{}]\t{}".format(pred_case.conf2, pred_case.label2)
    print


def main(args):

    testcase_valid = validation_testcase()
    tests = fetch_testfile(args.test_file, args.label_side)
    preds = fetch_predfile(args.prediction_file)
    pred_idx = 0
    empty_pred = Pred("***", "***", "***", "***", "***", "***", "***")
    for test_idx, (case, valid) in enumerate(zip(tests, testcase_valid)):
        if valid:
            output_result(pred_idx, test_idx, case, preds[pred_idx], args.label_side)
            pred_idx += 1
        else:
            output_result("***", test_idx, case, empty_pred, args.label_side)


args = parse_args()
main(args)
