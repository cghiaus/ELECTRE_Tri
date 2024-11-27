#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:09:13 2024

@author: cghiaus

ELECTRE Tri-B:
    - 3 alternatives, 2 criteria
    - 2 explicitely defined base profiles (for 3 categories).
"""

import electre_tri as et

# Problem statement
data_file = "../data/base_profile.csv"
credibility_threshold = 0.7

# Problem solving
A, B, T, w = et.read_electre_tri_data(data_file)

opti, pessi = et.electre_tri_b(A, B, T, w,
                               credibility_threshold)

# Results
print("\nProbabilistic optimistic ranking:")
print(opti.to_string(na_rep='0'))

print("\nProbabilistic pessimistic ranking:")
print(pessi.to_string(na_rep='0'))
