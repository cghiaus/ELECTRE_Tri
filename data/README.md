# Data files

## Files for Simos' revised method
- `cards_subsets_*.csv`:  
   Criteria in ascending order. Ex-equo criteria on the same row. The `white` cards are used for larger differences between criteria.
*****

## Files for ELECTRE Tri-B method
*****

- `base_profile.csv` and `base_profile_std.csv`:
  3-alternatives, 2-criteria decision matrix, 2-base profiles for ELECTRE Tri and pELECTRE Tri, respectiely.
*****

- `bldg_retrofit_base.csv` and `bldg_retrofit_base_std.csv`: 3-alternatives, 2-criteria decision matrix, 2-base profiles for ELECTRE Tri and pELECTRE Tri, respectiely, applied to building energy retrofit. Note the negative values for criteria to be minimized.
*****

- `bldg_retrofit_level.csv`: same as for `bldg_retrofit_base.csv` but with the definition of categories as a number of equal ranges between the lowest possible and the highest possible level. Note the negative values for criteria to be minimized.
*****
  
- `default_categories.csv`:
  Data file for default parameters (base profiles and thresholds).
*****

- `Isfaki_T10_1_T10_13.csv`:  
  5 criteria, 7 alternatives, 2 base profiles

  Iskafi, K. (2022). Recherche opérationnelle. Mathématique pour aide à la décision. Génie réseux et télécomunication. ENSA, Maroc https://fr.scribd.com/document/627158131/R-O-Pr-Khalid-ISKAFI

  performance matrix: Table 10.1, page 94
  base profiles: Table 10.13, page 101
  ELECTRE Tri optimistic and pessimistic sorting: Table 10.31, page 107
*****

- `mous3docl99_2.csv`:  
   5 criteria, 3 alternatives, 1 base profile

   Mousseau, V., Slowinski, R., & Zielniewicz, P. (1999). ELECTRE TRI 2.0 Methodological guide and user’s manual. Universite Paris Dauphine, Document du LAMSADE, 111, 263-275. https://www.lamsade.dauphine.fr/mcda/biblio/PDF/mous3docl99.pdf

   performance matrix: Table 1, page 15  
   thresholds and weights: Table 2, page 16  
   base profile: 1st paragraph, page 16
*****

- `mous3docl99_3.csv`:  
   5 criteria, 3 alternatives, 2 base profiles

   Mousseau, V., Slowinski, R., & Zielniewicz, P. (1999). ELECTRE TRI 2.0 Methodological guide and user’s manual. Universite Paris Dauphine, Document du LAMSADE, 111, 263-275. https://www.lamsade.dauphine.fr/mcda/biblio/PDF/mous3docl99.pdf

   performance matrix: Table 1, page 15
   thresholds and weights: Table 2, page 16
   base profile: Table 9, page 19
*****

- `performance_matrix.csv`:  
   2 criteria, 3 alternatives (no base profiles)
*****