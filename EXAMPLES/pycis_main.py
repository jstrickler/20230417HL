from pycis import CIS

cis = CIS()

# properties ##

# fetching lists
print(f"cis.ListOfContinentsByName: {cis.ListOfContinentsByName}\n")
print(f"cis.ListOfContinentsByCode: {cis.ListOfContinentsByCode}\n")
print(f"cis.ListOfCountryNamesByCode: {cis.ListOfCountryNamesByCode}\n")
print(f"cis.ListOfCountryNamesByName: {cis.ListOfCountryNamesByName}\n")
print(f"cis.ListOfCurrenciesByCode: {cis.ListOfCurrenciesByCode}\n")
print(f"cis.ListOfCurrenciesByName: {cis.ListOfCurrenciesByName}\n")
print(f"cis.ListOfLanguagesByCode: {cis.ListOfLanguagesByCode}\n")
print(f"cis.ListOfLanguagesByName: {cis.ListOfLanguagesByName}\n")
print('-' * 60)

countries_by_continent = cis.ListOfCountryNamesGroupedByContinent
for continent, countries in countries_by_continent.items():
    print(f"{continent.rstrip()}:")
    print(f"{countries}")
    print()
print('-' * 60)

# fetching full info for all countries
print(f"cis.FullCountryInfoAllCountries():")
for country in cis.FullCountryInfoAllCountries():
    print(country)
    print()
print()

## instance methods ##

# fetching languages by ISO language codes
for lang_code in 'eng', 'zh', 'hin', 'tam', 'sz', 'fr', 'kli':
    print(f"cis.LanguageName('{lang_code}'): {cis.LanguageName(lang_code)}")
print()

# fetching language codes by language names
for language in 'English', 'Tagalog', 'Swahili', 'Arabic', 'French':
    print(f"cis.LanguageISOCode('{language}'): {cis.LanguageISOCode(language)}")
print()

# fetching countries using currency by ISO currency codes
for currency_code in 'USD', 'CNY', 'GBP':
    print(f"cis.CountriesUsingCurrency('{currency_code}'): {cis.CountriesUsingCurrency(currency_code)}")
print()

# fetching currency name by ISO currency codes
for currency_code in 'USD', 'CNY', 'GBP':
    print(f"cis.CurrencyName('{currency_code}'): {cis.CurrencyName(currency_code)}")
print()

# fetching country info by ISO country code
for country_code in 'US', 'IN', 'CN', 'CA':
    print(f"cis.CountryName('{country_code}'): {cis.CountryName(country_code)}")
    print(f"cis.CapitalCity('{country_code}'): {cis.CapitalCity(country_code)}")
    print(f"cis.CountryCurrency('{country_code}'): {cis.CountryCurrency(country_code)}")
    print(f"cis.CountryIntPhoneCode('{country_code}'): {cis.CountryIntPhoneCode(country_code)}")
    print(f"cis.CountryFlag('{country_code}'): {cis.CountryFlag(country_code)}")
    print('=' * 20)
print()

# fetching ISO country codes by country name
for country_name in 'United States', 'Burkina Faso', 'United Arab Emirates', 'Canada':
    print(f"cis.CountryISOCode('{country_name}'): {cis.CountryISOCode(country_name)}")
print()

# fetching full country info by ISO country code
for country_code in 'US', 'IN', 'CN', 'AE', 'CA':
    print(f"cis.FullCountryInfo('{country_code}'): {cis.FullCountryInfo(country_code)}")
    print('=' * 20)
print()

