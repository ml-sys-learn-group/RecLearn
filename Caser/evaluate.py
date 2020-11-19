"""
Created on Nov 19, 2020

evaluate model

@author: Ziyao Geng
"""

import numpy as np


def getHit(pred_y, true_y):
    """
    calculate hit rate
    :return:
    """
    # reversed
    pred_index = np.argsort(-pred_y)[:, :_K]
    return sum([true_y[i] in pred_index[i] for i in range(len(pred_index))]) / len(pred_index)


def getNDCG(pred_y, true_y):
    """
    calculate NDCG
    :return:
    """
    pred_index = np.argsort(-pred_y)[:, :_K]
    return sum([1 / np.log(np.where(true_y[i] == pred_index[i])[0][0] + 2)
                for i in range(len(pred_index))
                if len(np.where(true_y[i] == pred_index[i])[0]) != 0]) / len(pred_index)


def getMRR(pred_y, true_y):
    """
    calculate MRR
    :return:
    """
    pred_index = np.argsort(-pred_y)
    return sum([1 / (np.where(true_y[i] == pred_index[i])[0][0] + 1)
                for i in range(len(pred_index))]) / len(pred_index)


def evaluate_model(model, test, K):
    """
    evaluate model
    :param model: model
    :param test: test set
    :param K: top K
    :return: hit rate, ndcg, mrr
    """
    global _K
    _K = K
    test_X, test_y = test
    pred_y = model.predict(test_X)
    hit_rate = getHit(pred_y, test_y)
    ndcg = getNDCG(pred_y, test_y)
    mrr = getMRR(pred_y, test_y)

    return hit_rate, ndcg, mrr