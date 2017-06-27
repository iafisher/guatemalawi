import operator
import random
from functools import reduce, lru_cache
from typing import List, Iterator


@lru_cache()
def all_countries(overlap=2, min_combos=2, min_length=0) -> tuple:
    return tuple(build_name('', COUNTRIES, overlap, min_combos, min_length))


def random_country(overlap=2, min_combos=2, min_length=0) -> str:
    try:
        return random.choice(all_countries(overlap, min_combos, min_length))
    except IndexError:
        return ''


# This dictionary is kept in case I ever decide to use regional information.
# For now it is only used to construct the actual COUNTRIES list.
COUNTRIES_BY_REGION = {
 'Europe': [
    'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus',
    'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
    'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia',
    'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta',
    'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland',
    'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia',
    'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom',
    'Vatican City',
  ],
 'Africa': [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
    'Democratic Republic of the Congo', 'Republic of the Congo',
    "Cote d'Ivoire", 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea',
    'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya',
    'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali',
    'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger',
    'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles',
    'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan',
    'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe',
 ],
 'North America': [
    'Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada',
    'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'El Salvador',
    'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico',
    'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States'
 ],
 'South America': [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana',
    'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela'
 ],
 'Asia': [
    'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan',
    'Brunei', 'Cambodia', 'China', 'Georgia', 'India', 'Indonesia', 'Iran',
    'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan',
    'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal',
    'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar',
    'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan',
    'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkey', 'Turkmenistan',
    'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'
 ],
 'Oceania': [
    'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru',
    'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands',
    'Tonga', 'Tuvalu', 'Vanuatu'
 ],
}

COUNTRIES = list(reduce(operator.add, COUNTRIES_BY_REGION.values()))


def combine(country1: str, country2: str, threshold=2) -> str:
    if not country1 or not country2:
        return country1 + country2
    if country1 != country2:
        country1_lower = country1.lower()
        country2_lower = country2.lower()
        for i in range(threshold, min(len(country1), len(country2))):
            if country1_lower[-i:] == country2_lower[:i]:
                return country1 + country2[i:]
    return ''


def build_name(so_far: str, names: List[str], overlap: int, 
               min_combos: int, min_length: int ,combos=0) -> Iterator[str]:
    for name in names:
        combined = combine(so_far, name, overlap)
        if combined:
            new_names = names[:]
            new_names.remove(name)
            yield from build_name(combined, new_names, overlap, min_combos,
                                  min_length, combos + 1)
    if combos >= min_combos and len(so_far) >= min_length:
        yield so_far
