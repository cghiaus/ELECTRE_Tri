#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:09:13 2024

@author: cghiaus

pELECTRE Tri-B (probabilistic ELECTRE Tri-B)
with 4 explicitely defined base profiles for 5 categories.
The standard deviation of the values of performance matrix are in `S`.

"""

import electre_tri as et

folder = '../data/'
file_std = 'base_profile_std.csv'
data_file = folder + file_std

A, S, B, T, w = et.read_pelectre_tri_data(data_file)
credibility_threshold = 0.7

p_opti, p_pessi = et.pelectre_tri_b(
    A, S, B, T, w,
    credibility_threshold,
    n_simulations=100)

print("\nProbabilistic optimistic ranking:")
print(p_opti)

print("\nProbabilistic pessimistic ranking:")
print(p_pessi)
