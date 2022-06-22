#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: UTF-8 -*-
import pandas as pd
import chemparse


def get_formula() -> str:
    """Get formula of semiconductor from user input and return it"""
    return input("Please, enter a semiconductor formula: ")


def parse_formula(formula: str) -> dict:
    """Parse semiconductor formula and return chemical composition as dictionary {'element': index, etc.}"""
    return chemparse.parse_formula(formula)


# In[12]:


charge_state = {
        "O": -2,
        "Li": 1,
        "Na": 1,
        "Mg": 2,
        "Al": 3,
        "K":  1,
        "Ca": 2,
        "Sc": 3,
        "Ti": 4,
        "V":  5,
        "Cr": 3,
        "Mn": 2, # Check oxidate state according to experimental data
        "Fe": 3,
        "Co": 2,
        "Ni": 2,
        "Cu": 2,
        "Zn": 2,
        "Y":  3,
        "Zr": 4,
        "Nb": 5,
        "Mo": 6,
        "Ag": 1,
        "Cd": 2,
        "In": 3,
        "Ba": 2,
        "La": 3,
        "Ce": 3,
        "Pr": 3,
        "Nd": 3,
        "Pm": 3,
        "Sm": 3,
        "Eu": 3,
        "Gd": 3,
        "Tb": 3,
        "Dy": 3,
        "Ho": 3,
        "Er": 3,
        "Tm": 3,
        "Yb": 3,
        "Bi": 3,
        "Ga": 3,        
                }


# In[54]:


if __name__ == "__main__":
    df = pd.read_excel('to_calculate.xlsx')
    pd.options.display.max_columns = 12

    for semiconductor in df['Initial composition']:
        positive_charge = 0
        new_composition = ''
        formula_as_dict = parse_formula(semiconductor)
        for el, ind in formula_as_dict.items():
            if el != 'O':
                positive_charge += ind*charge_state[el]
                new_composition += f'{el}{ind}'
        new_composition = new_composition + 'O' + f'{round(positive_charge/2, 3)}'
        print(new_composition, sep='\n')
        # df['Revised composition'] = new_composition
    print(df.head(30))


# In[43]:


semiconductor = get_formula()
formula_as_dict = parse_formula(semiconductor)
print(formula_as_dict)
positive_charge = 0
new_composition = ''
for el, ind in formula_as_dict.items():
    if el != 'O':
        positive_charge += ind*charge_state[el]
        new_composition += f'{el}{ind}'
new_composition = new_composition + 'O' + f'{round(positive_charge/2, 3)}'

print(new_composition)


# In[ ]:




