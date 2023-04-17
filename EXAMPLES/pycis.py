"""
Provide client to SOAP-based Country Information Service

All SOAP services not requiring parameters are implemented as properties.
"""
import logging
from dataclasses import dataclass
from zeep import Client
from typing import List

# get a logger using default destination and levels (STDERR & WARNING)
logger = logging.getLogger(__name__)

# URL for SOAP service (AKA WSDL)
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
        if tcountry.Languages:
            for language in tcountry.Languages.tLanguage:
                self.languages.append((language.sISOCode, language.sName))

class CIS:
    """
    Provide interface to CIS SOAP service.

    Note -- violating PEP8 on purpose so CIS method names match
    the corresponding SOAP services.
    """
    def __init__(self):
        """
        Constructor
        """
        self._client = Client(
            wsdl=CIS_WSDL_URL,
            # Zeep defaults to first service and port
            # service_name="CountryInfoService",
            # port_name="CountryInfoServiceSoap12",
        )
        logger.info(f"self._client: %s", self._client)

    def CapitalCity(self, iso_code: str) -> str:
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
        return response


    def CountryCurrency(self, iso_code: str) -> str:
        """
        Fetch currency of a country given its ISO code

        :param iso_code: ISO country code
        :return: ISO currency code, currency name as a tuple
        """
        response = self._client.service.CountryCurrency(iso_code)
        return response

    def CountryFlag(self, iso_code: str) -> str:
        """
        Fetch link to country's flag given its ISO code

        :param iso_code: ISO country code
        :return: URL for flag image as a string
        """
        response = self._client.service.CountryFlag(iso_code)
        return response

    def CountryISOCode(self, country_name: str) -> str:
        """
        Fetch country ISO code given country's name

        :param country_name: country name as string
        :return: ISO code as string
        """
        response = self._client.service.CountryISOCode(country_name)
        return response

    def CountryIntPhoneCode(self, iso_code: str) -> str:
        """
        Fetch phone prefix of a country given its ISO code

        :param iso_code: ISO country code
        :return: phone code as a string
        """
        response = self._client.service.CountryIntPhoneCode(iso_code)
        return response

    def CountryName(self, iso_code: str) -> str:
        """
        Fetch name of a country given its ISO code

        :param iso_code: ISO country code
        :return: country name as a string
        """
        response = self._client.service.CountryName(iso_code)
        return response

    def CurrencyName(self, iso_currency_code: str) -> str:
        """
        Fetch name of currency given its ISO currency code

        :param iso_code: ISO currency code
        :return: currency name as a string
        """
        response = self._client.service.CurrencyName(iso_currency_code)
        return response

    def FullCountryInfo(self, iso_code: str) -> str:
        """
        Fetch all available information for one country via country ISO code

        :param iso_code: ISO Country code as string
        :return: Country instance
        """
        response = self._client.service.FullCountryInfo(iso_code)
        return Country(response)

    def FullCountryInfoAllCountries(self) -> list:
        """
        Fetch list of all available information for all countries

        :return: list of Country instances
        """
        response = self._client.service.FullCountryInfoAllCountries()

        # create list of Country objects initialized by CIS tCountry instances
        countries = [Country(c) for c in response]
        return countries

    def LanguageISOCode(self, language_name: str) -> str:
        """
        Fetch ISO language code from language name

        :param language_name: name of language as string
        :return: ISO language code as string
        """
        response = self._client.service.LanguageISOCode(language_name)
        return response

    def LanguageName(self, iso_code: str) -> str:
        """
        Fetch language name from ISO language code

        :param iso_code: ISO language code
        :return: language name as string
        """
        response = self._client.service.LanguageName(iso_code)
        return str(response)

    def _get_continents_list(self, service: callable) -> list:
        """
        Convenience function that returns a list of continents from
        a callable.

        This function avoids the duplication of pulling code and name
        out of each per-continent tuple.

        :param service: callable that returns list of continents
        :return: list of continents
        """
        response = service()  # call remote function
        list_of_continents = [(c.sCode, c.sName) for c in response]
        return list_of_continents

    @property
    def ListOfContinentsByCode(self) -> list:
        """
        Fetch list of continents, sorted by ISO continent code.

        :return: List of (iso-code, continent-name) tuples.
        """
        return self._get_continents_list(self._client.service.ListOfContinentsByCode)

    @property
    def ListOfContinentsByName(self) -> list:
        """
        Fetch list of continents, sorted by ISO continent code.

        :return: List of (iso-code, continent-name) tuples.
        """
        return self._get_continents_list(
            self._client.service.ListOfContinentsByName
        )

    def _get_countries_list(self, service) -> list:
        """
        helper function for fetching lists of countries

        :param service: SOAP service to be called
        :return: list of countries as (code, name) tuples
        """

        response = service()  # call remote function
        list_of_countries = [(c.sISOCode, c.sName) for c in response]
        return list_of_countries


    @property
    def ListOfCountryNamesByCode(self) -> list:
        """
        Fetch list of countries, sorted by ISO code.

        :return: List of (iso-code, country-name) tuples.
        """
        return self._get_countries_list(self._client.service.ListOfCountryNamesByCode)

    @property
    def ListOfCountryNamesByName(self) -> list:
        """
        Fetch list of countries, sorted by country name.

        :return: List of (iso-code, country-name) tuples.
        """
        return self._get_countries_list(self._client.service.ListOfCountryNamesByName)

    @property
    def ListOfCountryNamesGroupedByContinent(self) -> list:
        """
        Fetch list of countries grouped by continent

        :return: Dictionary where continent name is the key, and list of country names is the value
        """
        response = self._client.service.ListOfCountryNamesGroupedByContinent()
        continents = {}
        for continent in response:
            continent_name = continent.Continent.sName
            countries = [c.sName for c in continent.CountryCodeAndNames.tCountryCodeAndName]
            continents[continent_name] = countries  # list of countries for this continent
        return continents

    def _get_currencies_list(self, service: callable) -> list:
        """
        helper function for fetching lists of currencies

        :param service: SOAP service to be called
        :return: list of currencies as (code, name) tuples
        """
        response = service()  # call remote function
        list_of_currencies = [(c.sISOCode, c.sName) for c in response]
        return list_of_currencies

    @property
    def ListOfCurrenciesByCode(self) -> list:
        """
        Fetch list of currencies, sorted by ISO currency code.

        :return: List of (iso-code, currency) tuples
        """
        return self._get_currencies_list(self._client.service.ListOfCurrenciesByCode)

    @property
    def ListOfCurrenciesByName(self) -> list:
        """
        Fetch list of currencies, sorted by currency name.

        :return: List of (iso-code, currency) tuples
        """
        return self._get_currencies_list(self._client.service.ListOfCurrenciesByCode)

    def _get_languages_list(self, service: callable) -> list:
        response = service()  # call remote function
        list_of_languages = [(c.sISOCode, c.sName) for c in response]
        return list_of_languages

    @property
    def ListOfLanguagesByCode(self) -> list:
        """
        Fetch list of languages, sorted by ISO code.

        :return: List of (iso-code, language) tuples
        """
        return self._get_languages_list(self._client.service.ListOfLanguagesByCode)

    @property
    def ListOfLanguagesByName(self) -> list:
        """
        Fetch list of languages, sorted by language name.

        :return: List of (iso-code, language) tuples
        """
        return self._get_languages_list(self._client.service.ListOfLanguagesByName)
