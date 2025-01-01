#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 10:12:42 2025

@author: cghiaus
"""

import os
import subprocess

# Change the current working directory
os.chdir('./examples')

# List of scripts to run
scripts = [
    'base_profile.py',
    'base_profile_std.py',
    'bldg_retrofit_base.py',
    'bldg_retrofit_base_std.py',
    'bldg_retrofit_level.py'
]

# Run each script
for script in scripts:
    print(f"Running {script}...")
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")
    print(f"Finished running {script}\n")

print("All scripts have been executed.")
