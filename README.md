# ELECTRE Tri-B

by Christian Ghiaus

Researcher ID: [ORCID](https://orcid.org/0000-0001-5561-1245), [SciProfiles](https://sciprofiles.com/profile/2970335), [Scopus](https://www.scopus.com/authid/detail.uri?authorId=6603390490), [Web of Science](https://www.webofscience.com/wos/author/record/1651371), [HAL](https://cv.hal.science/cghiaus)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cghiaus/ELECTRE_Tri/HEAD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cghiaus/dm4bem_book/blob/main/LICENSE)

ELECTRE Tri-B is a Multiple-Criteria Decision-Making ([MCDM](https://en.m.wikipedia.org/wiki/Multiple-criteria_decision_analysis)) method for sorting alternatives into predefined categories defined by lower and upper boundaries. 

This repository contains a framework and a Python 3.11.7 implementation of ELECTRE Tri-B and of Simos' method for determining the weights of criteria, along with documentation and examples.

The crisp and probabilistic ELECTRE Tri-B method is implemented the module [electre_tri.py](./src/electre_tri.py) in four workflows, presented in [workflows.ipynb](./docs/how_to_guides/workflows.ipynb). 

## Installation

This software requires no installation. Simply copy the module files to your desired location.

For remote execution without any local setup, you can run this repository on MyBinder.org:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cghiaus/ELECTRE_Tri/HEAD)

Click the "Launch Binder" badge above to open the repository in a Jupyter environment. This allows you to interact with the software directly in your web browser (with no local installation).


## Contents

```
ELECTRE_Tri-main
├── code
│   └── examples
├── data
├── docs
│   ├── explanation
│   ├── how_to_guides
│   ├── reference
│   └── tutorials
├── figs
├── src
│   ├── __init__.py
│   ├── electre_tri.py
│   └── simos_revised.py
├── LICENSE
├── README.md
├── environment.yml
└── requirements.txt
```
## Summary

- `code/examples`: Python scripts that use the modules from `/src` and data from `/data`.

- `data`: .csv data files for ELECTRE Tri-B and Simos' revised method.

- `docs`: documentation
    - `explanation`: description of concepts; details on ELECTRE Tri-B and Simos' method for weights of criteria.
    - `how_to_guides`: directions for specific goals; useful to solve tasks when accustomed with the methods.
    - `reference`: documentation of functions implemented in the modules of `/src`.
    - `tutorials`: guided steps to solve a meaningful problem; starting point for those new to the methods.

- `figs`: modifiable figures in `.svg` format.

- `src`: source code of Python modules.
    - `electre-tri.py`: Multiple-Criteria Decision-Making.
    - `simos_revised`: Simos' method for determining weights of criteria in ELECTRE type methods.

## Usage

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cghiaus/ELECTRE_Tri/HEAD)

1. Launch binder.
2. Upload your data file (which describes the ELECTRE Tri or the weighing problem) in `/data` folder.
3. Modify and run the scripts from `code/examples` to get the results.

Read the documentation from `/docs`.
