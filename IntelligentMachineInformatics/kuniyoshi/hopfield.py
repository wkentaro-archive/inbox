#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class Hopfield(object):
    def __init__(self, mode='vector'):
        self.mode = mode
        self.weight_ = None

    def fit(self, X, y):
        n_sample = len(X)
        if self.mode == 'vector':
            self._fit_vector(X, y)

    def _fit_vector(self, X, y):
        W = np.zeros((X.shape[1], X.shape[1]))
        for x in X:
            x = np.atleast_2d(x).reshape((-1, 1))
            W += np.dot(x, x.T)
        self.weight_ = W

    def recall(self, x, n_times):
        x = np.atleast_2d(x).reshape((-1, 1))
        W = self.weight_
        for _ in xrange(n_times):
            x = np.dot(W, x)
            x = np.sign(x)
        return x
