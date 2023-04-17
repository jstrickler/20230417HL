"""
Provide client to SOAP-based Country Information Service

All SOAP services not requiring parameters are implemented as properties.
"""
import logging
from dataclasses import dataclass
from suds.client import Client # get suds SOAP client
from suds.sax.text import Text
from typing import List

logger = logging.getLogger(__name__)

CIS_WSDL_URL = (
        "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
)

@dataclass
class Country:
    """
    Represent full information for one country
    """
    iso_code: str
    name: str
    capital_city: str
    phone_code: str
    iso_continent_code: str
    iso_currency_code: str
    flag_url: str
    languages: List[tuple]

    def __init__(self, tcountry):
        """
        Constructor for Country class

        :param tcountry: A  sudsobject tCountry instance
        """
        self.iso_code = tcountry.sISOCode
        self.name = tcountry.sName
        self.capital_city = tcountry.sCapitalCity
        self.phone_code = tcountry.sPhoneCode
        self.iso_continent_code = tcountry.sContinentCode
        self.iso_currency_code = tcountry.sCurrencyISOCode
        self.flag_url = tcountry.sCountryFlag
        self.languages = []
        if not isinstance(tcountry.Languages, Text):
            for language in tcountry.Languages.tLanguage:
                self.languages.append((language.sISOCode, language.sName))

# URL for SOAP service (AKA WSDL)
class CIS:
    """
    Provide interface to CIS SOAP service
    """
    def __init__(self):
        self._client = Client(CIS_WSDL_URL)
        logger.info(f"self._client: %s", self._client)

    def CapitalCity(self, iso_code):
        """
        Fetch capital of a country given its ISO code

        :param iso_code: ISO country code
        :return: Capital city as string
        """
        response = self._client.service.CapitalCity(iso_code)
        return str(response)



    def CountriesUsingCurrency(self, iso_currency_code):
        """
        Fetch list of countries using specified currency.

        :param iso_currency_code: ISO currency code
        :return: List of country codes
        """
        response = self._client.service.CountriesUsingCurrency(iso_currency_code)  # call remote function
        list_of_countries = [(c.sISOCode, c.sName) for c in response.tCountryCodeAndName]
        return list_of_countries


    def CountryCurrency(self, iso_code):
        """
        Fetch currency of a country given its ISO code

        :param iso_code: ISO country code
        :return: ISO currency code, currency name as a tuple
        """
        response = self._client.service.CountryCurrency(iso_code)
        return response.sISOCode, response.sName

    def CountryFlag(self, iso_code):
        """
        Fetch link to country's flag given its ISO code

        :param iso_code: ISO country code
        :return: URL for flag image as a string
        """
        response = self._client.service.CountryFlag(iso_code)
        return str(response)

    def CountryISOCode(self, country_name):
        """
        Fetch country ISO code given country's name

        :param country_name: country name as string
        :return: ISO code as string
        """
        response = self._client.service.CountryISOCode(country_name)
        return str(response)

    def CountryIntPhoneCode(self, iso_code):
        """
        Fetch phone prefix of a country given its ISO code

        :param iso_code: ISO country code
        :return: phone code as a string
        """
        response = self._client.service.CountryIntPhoneCode(iso_code)
        return str(response)

    def CountryName(self, iso_code):
        """
        Fetch name of a country given its ISO code

        :param iso_code: ISO country code
        :return: country name as a string
        """
        response = self._client.service.CountryName(iso_code)
        return str(response)

    def CurrencyName(self, iso_currency_code):
        """
        Fetch name of currency given its ISO currency code

        :param iso_code: ISO currency code
        :return: currency name as a string
        """
        response = self._client.service.CurrencyName(iso_currency_code)
        return str(response)

    def FullCountryInfo(self, iso_code):
        """
        Fetch all available information for one country via country ISO code

        :param iso_code: ISO Country code as string
        :return: Country instance
        """
        response = self._client.service.FullCountryInfo(iso_code)
        return Country(response)

    def FullCountryInfoAllCountries(self):
        """
        Fetch list of all available information for all countries

        :return: list of Country instances
        """
        response = self._client.service.FullCountryInfoAllCountries()

        # create list of Country objects initialized by CIS tCountry instances
        countries = [Country(c) for c in response.tCountryInfo]
        return countries

    def LanguageISOCode(self, language_name):
        """
        Fetch ISO language code from language name

        :param language_name: name of language as string
        :return: ISO language code as string
        """
        response = self._client.service.LanguageISOCode(language_name)
        return str(response)

    def LanguageName(self, iso_code):
        """
        Fetch language name from ISO language code

        :param iso_code: ISO language code
        :return: language name as string
        """
        response = self._client.service.LanguageName(iso_code)
        return str(response)

    def _get_continents_list(self, service):
        response = service()  # call remote function
        list_of_continents = [(c.sCode, c.sName) for c in response.tContinent]
        return list_of_continents

    @property
    def ListOfContinentsByCode(self):
        """
        Fetch list of continents, sorted by ISO continent code.

        :return: List of (iso-code, continent-name) tuples.
        """
        return self._get_continents_list(self._client.service.ListOfContinentsByCode)

    @property
    def ListOfContinentsByName(self):
        """
        Fetch list of continents, sorted by ISO continent code.

        :return: List of (iso-code, continent-name) tuples.
        """
        return self._get_continents_list(self._client.service.ListOfContinentsByName)

    def _get_countries_list(self, service):
        """
        helper function for fetching lists of countries

        :param service: SOAP service to be called
        :return: list of countries as (code, name) tuples
        """

        response = service()  # call remote function
        list_of_countries = [(c.sISOCode, c.sName) for c in response.tCountryCodeAndName]
        return list_of_countries


    @property
    def ListOfCountryNamesByCode(self):
        """
        Fetch list of countries, sorted by ISO code.

        :return: List of (iso-code, country-name) tuples.
        """
        return self._get_countries_list(self._client.service.ListOfCountryNamesByCode)

    @property
    def ListOfCountryNamesByName(self):
        """
        Fetch list of countries, sorted by country name.

        :return: List of (iso-code, country-name) tuples.
        """
        return self._get_countries_list(self._client.service.ListOfCountryNamesByName)

    @property
    def ListOfCountryNamesGroupedByContinent(self):
        """
        Fetch list of countries grouped by continent

        :return: Dictionary where continent name is the key, and list of country names is the value
        """
        response = self._client.service.ListOfCountryNamesGroupedByContinent()
        continents = {}
        for continent in response.tCountryCodeAndNameGroupedByContinent:
            continent_name = continent.Continent.sName
            countries = [c.sName for c in continent.CountryCodeAndNames.tCountryCodeAndName]
            continents[continent_name] = countries  # list of countries for this continent
        return continents

    def _get_currencies_list(self, service):
        """
        helper function for fetching lists of currencies

        :param service: SOAP service to be called
        :return: list of currencies as (code, name) tuples
        """
        response = service()  # call remote function
        list_of_currencies = [(c.sISOCode, c.sName) for c in response.tCurrency]
        return list_of_currencies

    @property
    def ListOfCurrenciesByCode(self):
        """
        Fetch list of currencies, sorted by ISO currency code.

        :return: List of (iso-code, currency) tuples
        """
        return self._get_currencies_list(self._client.service.ListOfCurrenciesByCode)

    @property
    def ListOfCurrenciesByName(self):
        """
        Fetch list of currencies, sorted by currency name.

        :return: List of (iso-code, currency) tuples
        """
        return self._get_currencies_list(self._client.service.ListOfCurrenciesByCode)

    def _get_languages_list(self, service):
        response = service()  # call remote function
        list_of_languages = [(c.sISOCode, c.sName) for c in response.tLanguage]
        return list_of_languages

    @property
    def ListOfLanguagesByCode(self):
        """
        Fetch list of languages, sorted by ISO code.

        :return: List of (iso-code, language) tuples
        """
        return self._get_languages_list(self._client.service.ListOfLanguagesByCode)

    @property
    def ListOfLanguagesByName(self):
        """
        Fetch list of languages, sorted by language name.

        :return: List of (iso-code, language) tuples
        """
        return self._get_languages_list(self._client.service.ListOfLanguagesByName)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # change to logging.CRITICAL to suppress messages
    cis = CIS()

    def by_name(country: Country) -> str:
        """
        Sort key function to sort by country name (default is ISO code)

        :param country: Country object
        :return: country name
        """
        return country.name

    for country in sorted(cis.FullCountryInfoAllCountries(), key=by_name):
        print(country)
        print()
