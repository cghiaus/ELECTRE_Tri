#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:09:13 2024

@author: cghiaus

ELECTRE Tri-B
with 4 explicitely defined base profiles (for 5 categories).
"""

import electre_tri as et

folder = '../data/'
file = 'base_profile.csv'
data_file = folder + file

A, B, T, w = et.read_electre_tri_data(data_file)

opti, pessi = et.electre_tri_b(A, B, T, w,
                               credibility_threshold=0.7)

print("\nProbabilistic optimistic ranking:")
print(opti)

print("\nProbabilistic pessimistic ranking:")
print(pessi)
