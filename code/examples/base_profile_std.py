#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:09:13 2024

@author: cghiaus

pELECTRE Tri-B (probabilistic ELECTRE Tri-B):
    - 3 alternatives, 2 criteria
    - 2 explicitely defined base profiles (for 3 categories).
The standard deviation of the values of performance matrix are in `S`.

"""

import electre_tri as et


# Problem statement
data_file = "../data/base_profile_std.csv"
credibility_threshold = 0.7

# Problem solving
A, S, B, T, w = et.read_pelectre_tri_base(data_file)

p_opti, p_pessi = et.pelectre_tri_b(
    A, S, B, T, w,
    credibility_threshold,
    n_simulations=100)

print("Probabilistic pELECTRE Tri-B")
print("Data file:", data_file)
# Results
print("\nProbabilistic optimistic ranking:")
print(p_opti.to_string(na_rep='0'))

print("\nProbabilistic pessimistic ranking:")
print(p_pessi.to_string(na_rep='0'))
