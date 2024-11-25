#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:05:50 2024

@author: cghiaus

ELECTRE Tri with extreme levels
4 default base profiles for 5 categories.
"""

import pandas as pd

import electre_tri as et

data_file = '../data/default_categories.csv'
print("Example of data file")
A = pd.read_csv(data_file, index_col=0)

A, L, w = et.read_electre_tri_extreme_base_profile(data_file)
B = et.base_profile(L)
T = et.threshold(B)

opti, pessi = et.electre_tri_b(A, B, T, w,
                               credibility_threshold=0.7)
print("\nOptimistic ranking:")
print(opti)

print("\nPessimistic ranking:")
print(pessi)

print('Optimistic sorting')
print(et.sort(opti).to_frame(name="alternatives").rename_axis("categories"))

print('Pessimistic sorting')
print(et.sort(pessi).to_frame(name="alternatives").rename_axis("categories"))
