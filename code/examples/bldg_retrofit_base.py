#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:11:11 2024

@author: cghiaus

ELECTRE Tri-B with specified base profiles.

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

    Base profiles:
        - b1: bad
        - b2: good

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
data_file = "../../data/bldg_retrofit_base.csv"
credibility_threshold = 0.7

# Problem solving
A, B, T, w = et.read_electre_tri_base(data_file)

optimistic, pessimistic = et.electre_tri_b(A, B, T, w,
                                           credibility_threshold)

print("ELECTRE Tri-B with specified base profiles")
print("Data file:", data_file)

# Results
# Optimistic sorting
opti_sort = et.sort(optimistic)
print("\nOptimistic sorting")
print(opti_sort.to_frame(name="alternatives").rename_axis("categories"))


# Pessimistic sorting
pessi_sort = et.sort(pessimistic)
print("\nPessimistic sorting")
print(pessi_sort.to_frame(name="alternatives").rename_axis("categories"))
