# Examples of ELECTRE Tri-B

Examples of applications implemented in Python scripts. The examples assume that the module `electre_tri.py` is in the curent folder and that the data files are in the folder `../data/`.

__Contents__

- `base_profiles.py` and `base_profiles_pelectre.py`: Examples of ELECTRE Tri-B and pELECTRE Tri-B analysis, respectively, with 3-alternatives, 2-criteria decision matrix, 2-base profiles.
> - See: ../docs/tutorials/base_profile.ipynb
> - See: ../docs/tutorials/base_profile_pelectre.ipynb

- `bldg_retrofit_base.py` and `bldg_retrofit_base_pelectre.py`: Examples of ELECTRE Tri-B and pELECTRE Tri-B analysis, respectively, of energy retrofit of a building. Classify three alternatives into three categories defined by base profiles.
> - See: ../docs/tutorials/bldg_retrofit_base.ipynb
> - See: ../docs/tutorials/bldg_retrofit_base_pelectre.ipynb

- `bldg_retrofit_level.py`: Example of ELECTRE Tri-B applied to energy retrofit of a building. Sort three alternatives in three equidistant categories obtained from extreme (i.e., worst and best) profile levels. 
> - See: ../docs/tutorials/bldg_retrofit_level.ipynb

- `extrm_levels_electre.py`: Example of ELECTRE Tri-B analysis with extreme profile levels.
*****

- `electre_tri.py`: ELECTRE Tri module (copy of `../src/electre_tri.py`). Used to simply `ìmport` of module `electre_tri.py`.