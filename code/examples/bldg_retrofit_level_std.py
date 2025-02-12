#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:24:13 2024

@author: cghiaus

Probabilistic pELECTRE Tri-B with specified extreme level profiles.

Energy retrofit of a building.

Problem statement:

Given:

    Criteria with weights:
        - c1: Saving (in kWh/m²/year) with weight w = 0.7
        - c2: Cost (in €/m²) with weight w = 0.3

    Alternatives:
        - a1: Basic renovation,
        - a2: Moderate renovation,
        - a3: Extensive renovation.

    Standard deviatiions for the values of performance matrix:
        - s1: Basic renovation for all criteria,
        - s2: Moderate renovation for all criteria,
        - s3: Extensive renovation for all criteria.

    Level profiles:
        - l1: worst (worst possible base profile)
        - l2: best (best possible base profile)

Do:
    Sort the alternatives into
    Categories:
        - bad >: alteratives worse than b1 (bad) base profile.
        - (bad, good): alternatives between base profiles bad and good.
        - good <: alternatives better than b2 (good) base profile.
    defined by base profiles.

----
See:
    - docs/tutorials/bldg_retrofit_base.ipynb
    - docs/explanation/electre_tri-b_explained.ipynb
"""

import electre_tri as et

# Problem statement
data_file = "../../data/bldg_retrofit_level_std.csv"

# Problem solving
A, S, L, w = et.read_pelectre_tri_level(data_file)
B = et.base_profile(L, n_base_profile=2)
T = et.threshold(B, threshold_percent=[0.10, 0.25, 0.50])

p_opti, p_pessi = et.pelectre_tri_b(
    A, S, B, T, w,
    credibility_threshold=0.7,
    n_simulations=100)

print("Probabilistic pELECTRE Tri-B with specified extreme level profiles")
print("Data file:", data_file)

# Results
print("\nProbabilistic optimistic ranking:")
print(p_opti.to_string(na_rep='0'))

print("\nProbabilistic pessimistic ranking:")
print(p_pessi.to_string(na_rep='0'))
