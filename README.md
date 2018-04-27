# Guatemalawi
Generate amusing combinations of real-world country names.

## Command-line interface
```shell
$ python3 guatemalawi
Venezuelaos
$ python3 guatemalawi --combos=3 --overlap=3 --length=30
United Kingdominicaraguatemalawi
```

## Python interface
```python
>>> from guatemalawi import random_country, all_countries
>>> random_country()
'Surinamexicosta Ricambodia'
>>> all_countries(overlap=4)
('Dominicaragua', 'Dominican Republic of the Congo', 'Guatemalaysia', 'Guatemalawi', 'Central African Republic of the Congo', 'Equatorial Guinea-Bissau', 'Czech Republic of the Congo', 'Papua New Guinea-Bissau')
>>> random_country(min_combos=4, min_length=30)
'Burkina Fasouth Sudangolatvia'
```
