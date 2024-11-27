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

import sys
import os

# Get the path to the parent directory /../..
parent_dir = os.path.dirname(           # dir of dir of file
    os.path.dirname(                    # directory of current file
        os.path.abspath(__file__)))     # absolute path to current file

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from src import electre_tri as et


# Problem statement
data_file = "../data/bldg_retrofit_base_std.csv"

# Problem solving
A, S, B, T, w = et.read_pelectre_tri_data(data_file)

p_opti, p_pessi = et.pelectre_tri_b(
    A, S, B, T, w,
    credibility_threshold=0.7,
    n_simulations=100)

# Results
print("\nProbabilistic optimistic ranking:")
print(p_opti)

print("\nProbabilistic pessimistic ranking:")
print(p_pessi)