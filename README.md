# Guatemalawi

```python
>>> from guatemalawi import random_country, all_countries
>>> random_country()
'Surinamexicosta Ricambodia'
>>> all_countries(overlap=4)
('Dominicaragua', 'Dominican Republic of the Congo', 'Guatemalaysia', 'Guatemalawi', 'Central African Republic of the Congo', 'Equatorial Guinea-Bissau', 'Czech Republic of the Congo', 'Papua New Guinea-Bissau')
>>> random_country(min_combos=4, min_length=30)
'Burkina Fasouth Sudangolatvia'
```

The `guatemalawi.py` module exports two public functions: `random_country` and `all_countries`. Both accept the same keyword arguments: `overlap` to control how many characters must overlap for two country names to be combined, `min_combos` to control how many countries must be combined in each outputted name, and `min_length` to control the minimum length of each outputted name.