# Guatemalawi

Generate amusing combinations of real-world country names.

## Usage

```python
>>> from guatemalawi import random_country
>>> random_country()
'Surinamexicosta Ricambodia'
>>> random_country(min_combos=4)
'Panamaltaiwangola'
>>> random_country(overlap=4)
'Guatemalawi'
```

## API

The `guatemalawi` module exports two public functions:

```python
def all_countries(overlap=2, min_combos=2, min_length=0) -> tuple:
    ...

def random_country(overlap=2, min_combos=2, min_length=0) -> str:
    ...
```

The keyword arguments are used to filter the output:

- `overlap`: how many characters two country names must overlap by
- `min_combos`: the minimum number of country names per combination
- `min_length`: the minimum length of outputted names

