import urllib.request
import json

# -> country codes for verification
country_codes = ('AFG', 'OWID_AFR', 'ALB', 'DZA', 'AND', 'AGO', 'AIA', 'ATG',
                 'ARG', 'ARM', 'ABW', 'OWID_ASI', 'AUS', 'AUT', 'AZE', 'BHS',
                 'BHR', 'BGD', 'BRB', 'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN',
                 'BOL', 'BES', 'BIH', 'BWA', 'BRA', 'VGB', 'BRN', 'BGR', 'BFA',
                 'BDI', 'KHM', 'CMR', 'CAN', 'CPV', 'CYM', 'CAF', 'TCD', 'CHL',
                 'CHN', 'COL', 'COM', 'COG', 'COK', 'CRI', 'CIV', 'HRV', 'CUB',
                 'CUW', 'CYP', 'CZE', 'COD', 'DNK', 'DJI', 'DMA', 'DOM', 'ECU',
                 'EGY', 'SLV', 'OWID_ENG', 'GNQ', 'EST', 'SWZ', 'ETH',
                 'OWID_EUR', 'OWID_EUN', 'FRO', 'FLK', 'FJI', 'FIN', 'FRA',
                 'PYF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL',
                 'GRD', 'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'OWID_HIC',
                 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRQ', 'IRL',
                 'IMN', 'ISR', 'ITA', 'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 'KEN',
                 'KIR', 'OWID_KOS', 'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO',
                 'LBR', 'LBY', 'LIE', 'LTU', 'OWID_LIC', 'OWID_LMC', 'LUX',
                 'MAC', 'MDG', 'MWI', 'MYS', 'MDV', 'MLI', 'MLT', 'MRT', 'MUS',
                 'MEX', 'MDA', 'MCO', 'MNG', 'MNE', 'MSR', 'MAR', 'MOZ', 'MMR',
                 'NAM', 'NRU', 'NPL', 'NLD', 'NCL', 'NZL', 'NIC', 'NER', 'NGA',
                 'NIU', 'OWID_NAM', 'MKD', 'OWID_CYN', 'OWID_NIR', 'NOR',
                 'OWID_OCE', 'OMN', 'PAK', 'PSE', 'PAN', 'PNG', 'PRY', 'PER',
                 'PHL', 'PCN', 'POL', 'PRT', 'QAT', 'ROU', 'RUS', 'RWA', 'SHN',
                 'KNA', 'LCA', 'VCT', 'WSM', 'SMR', 'STP', 'SAU', 'OWID_SCT',
                 'SEN', 'SRB', 'SYC', 'SLE', 'SGP', 'SXM', 'SVK', 'SVN', 'SLB',
                 'SOM', 'ZAF', 'OWID_SAM', 'KOR', 'SSD', 'ESP', 'LKA', 'SDN',
                 'SUR', 'SWE', 'CHE', 'SYR', 'TWN', 'TJK', 'TZA', 'THA', 'TLS',
                 'TGO', 'TKL', 'TON', 'TTO', 'TUN', 'TUR', 'TKM', 'TCA', 'TUV',
                 'UGA', 'UKR', 'ARE', 'GBR', 'USA', 'OWID_UMC', 'URY', 'UZB',
                 'VUT', 'VEN', 'VNM', 'OWID_WLS', 'WLF', 'OWID_WRL', 'YEM',
                 'ZMB', 'ZWE')

# =========
#  Setings
# =========

# Confirmed cases
total_cases = False
new_cases = True  # <-
new_cases_smoothed = False
total_cases_per_million = False
new_cases_per_million = False
new_cases_smoothed_per_million = False

# Confirmed deaths
total_deaths = False
new_deaths = True  # <-
new_deaths_smoothed = False
total_deaths_per_million = False
new_deaths_per_million = False
new_deaths_smoothed_per_million = False

# Excess mortality -> Not working
excess_mortality = False
excess_mortality_cumulative = False
excess_mortality_cumulative_absolute = False
excess_mortality_cumulative_per_million = False

# Hospital & ICU -> Not working
icu_patients = False
icu_patients_per_million = False
hosp_patients = False
hosp_patients_per_million = False
weekly_icu_admissions = False
weekly_icu_admissions_per_million = False
weekly_hosp_admissions = False
weekly_hosp_admissions_per_million = False

# Policy responses -> Not working
stringency_index = False

# Reproduction rate -> Not working
reproduction_rate = False

# Tests & positivity -> Not working
total_tests = False
new_tests = False
total_tests_per_thousand = False
new_tests_per_thousand = False
new_tests_smoothed = False
new_tests_smoothed_per_thousand = False
positive_rate = False
tests_per_case = False
tests_units = False

# Vaccinations -> Not working
total_vaccinations = False
people_vaccinated = False
people_fully_vaccinated = False
total_boosters = False
new_vaccinations = False
new_vaccinations_smoothed = False
total_vaccinations_per_hundred = False
people_vaccinated_per_hundred = False
people_fully_vaccinated_per_hundred = False
new_vaccinations_smoothed_per_million = False
new_people_vaccinated_smoothed = False
new_people_vaccinated_smoothed_per_hundred = False


# date = True
# total_vaccinations = False
# people_vaccinated = False
# people_fully_vaccinated = False
# daily_vaccinations_raw = False
# daily_vaccinations = False
# total_vaccinations_per_hundred = False
# people_vaccinated_per_hundred = False
# people_fully_vaccinated_per_hundred = False
# daily_vaccinations_per_million = False
# daily_people_vaccinated = False
# daily_people_vaccinated_per_hundred = False

# =========
# functions
# =========


def new_case_data(country_code: str):  # ->
    output = {}
    with urllib.request.urlopen("https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.json") as url:
        data = eval(json.dumps(json.loads(url.read().decode())))
        for date in data[country_code]['data']:
            day_data = eval(str(date))
            output[day_data['date']] = {}

            # Confirmed cases
            if total_cases:
                if 'total_cases' in day_data:
                    output[day_data['date']][
                        'total_cases'
                    ] = eval(str(day_data[
                        'total_cases']))
                else:
                    output[day_data['date']][
                        'total_cases'] = 0
            if new_cases:
                if 'new_cases' in day_data:
                    output[day_data['date']][
                        'new_cases'
                    ] = eval(str(day_data[
                        'new_cases']))
                else:
                    output[day_data['date']][
                        'new_cases'] = 0
            if new_cases_smoothed:
                if 'new_cases_smoothed' in day_data:
                    output[day_data['date']][
                        'new_cases_smoothed'
                    ] = eval(str(day_data[
                        'new_cases_smoothed']))
                else:
                    output[day_data['date']][
                        'new_cases_smoothed'] = 0
            if total_cases_per_million:
                if 'total_cases_per_million' in day_data:
                    output[day_data['date']][
                        'total_cases_per_million'
                    ] = eval(str(day_data[
                        'total_cases_per_million']))
                else:
                    output[day_data['date']][
                        'total_cases_per_million'] = 0
            if new_cases_per_million:
                if 'new_cases_per_million' in day_data:
                    output[day_data['date']][
                        'new_cases_per_million'
                    ] = eval(str(day_data[
                        'new_cases_per_million']))
                else:
                    output[day_data['date']][
                        'new_cases_per_million'] = 0
            if new_cases_smoothed_per_million:
                if 'new_cases_smoothed_per_million' in day_data:
                    output[day_data['date']][
                        'new_cases_smoothed_per_million'
                    ] = eval(str(day_data[
                        'new_cases_smoothed_per_million']))
                else:
                    output[day_data['date']][
                        'new_cases_smoothed_per_million'] = 0

            # Confirmed deaths
            if total_deaths:
                if 'total_deaths' in day_data:
                    output[day_data['date']][
                        'total_deaths'
                    ] = eval(str(day_data[
                        'total_deaths']))
                else:
                    output[day_data['date']][
                        'total_deaths'] = 0
            if new_deaths:
                if 'new_deaths' in day_data:
                    output[day_data['date']][
                        'new_deaths'
                    ] = eval(str(day_data[
                        'new_deaths']))
                else:
                    output[day_data['date']][
                        'new_deaths'] = 0
            if new_deaths_smoothed:
                if 'new_deaths_smoothed' in day_data:
                    output[day_data['date']][
                        'new_deaths_smoothed'
                    ] = eval(str(day_data[
                        'new_deaths_smoothed']))
                else:
                    output[day_data['date']][
                        'new_deaths_smoothed'] = 0
            if total_deaths_per_million:
                if 'total_deaths_per_million' in day_data:
                    output[day_data['date']][
                        'total_deaths_per_million'
                    ] = eval(str(day_data[
                        'total_deaths_per_million'
                    ]))
                else:
                    output[day_data['date']][
                        'total_deaths_per_million'] = 0
            if new_deaths_per_million:
                if 'new_deaths_per_million' in day_data:
                    output[day_data['date']][
                        'new_deaths_per_million'
                    ] = eval(str(day_data[
                        'new_deaths_per_million']))
                else:
                    output[day_data['date']][
                        'new_deaths_per_million'] = 0
            if new_deaths_smoothed_per_million:
                if 'new_deaths_smoothed_per_million' in day_data:
                    output[day_data['date']][
                        'new_deaths_smoothed_per_million'
                    ] = eval(str(day_data[
                        'new_deaths_smoothed_per_million']))
                else:
                    output[day_data['date']][
                        'new_deaths_smoothed_per_million'] = 0

            # Vaccinations
            if total_vaccinations:
                if 'total_vaccinations' in day_data:
                    output[day_data['date']][
                        'total_vaccinations'
                    ] = eval(str(day_data[
                        'total_vaccinations']))
                else:
                    output[day_data['date']][
                        'total_vaccinations'] = 0
            if people_vaccinated:
                if 'people_vaccinated' in day_data:
                    output[day_data['date']][
                        'people_vaccinated'
                    ] = eval(str(day_data[
                        'people_vaccinated']))
                else:
                    output[day_data['date']][
                        'people_vaccinated'] = 0
            if people_fully_vaccinated:
                if 'people_fully_vaccinated' in day_data:
                    output[day_data['date']][
                        'people_fully_vaccinated'
                    ] = eval(str(day_data[
                        'people_fully_vaccinated']))
                else:
                    output[day_data['date']][
                        'people_fully_vaccinated'] = 0
            if total_boosters:
                if 'total_boosters' in day_data:
                    output[day_data['date']][
                        'total_boosters'
                    ] = eval(str(day_data[
                        'total_boosters']))
                else:
                    output[day_data['date']][
                        'total_boosters'] = 0
            if new_vaccinations:
                if 'new_vaccinations' in day_data:
                    output[day_data['date']][
                        'new_vaccinations'
                    ] = eval(str(day_data[
                        'new_vaccinations']))
                else:
                    output[day_data['date']][
                        'new_vaccinations'] = 0
            if new_vaccinations_smoothed:
                if 'new_vaccinations_smoothed' in day_data:
                    output[day_data['date']][
                        'new_vaccinations_smoothed'
                    ] = eval(str(day_data[
                        'new_vaccinations_smoothed']))
                else:
                    output[day_data['date']][
                        'new_vaccinations_smoothed'] = 0
            if total_vaccinations_per_hundred:
                if 'total_vaccinations_per_hundred' in day_data:
                    output[day_data['date']][
                        'total_vaccinations_per_hundred'
                    ] = eval(str(day_data[
                        'total_vaccinations_per_hundred']))
                else:
                    output[day_data['date']][
                        'total_vaccinations_per_hundred'] = 0
            if people_vaccinated_per_hundred:
                if 'people_vaccinated_per_hundred' in day_data:
                    output[day_data['date']][
                        'people_vaccinated_per_hundred'
                    ] = eval(str(day_data[
                        'people_vaccinated_per_hundred']))
                else:
                    output[day_data['date']][
                        'people_vaccinated_per_hundred'] = 0
            if people_fully_vaccinated_per_hundred:
                if 'people_fully_vaccinated_per_hundred' in day_data:
                    output[day_data['date']][
                        'people_fully_vaccinated_per_hundred'
                    ] = eval(str(day_data[
                        'people_fully_vaccinated_per_hundred']))
                else:
                    output[day_data['date']][
                        'people_fully_vaccinated_per_hundred'] = 0
            if new_vaccinations_smoothed_per_million:
                if 'new_vaccinations_smoothed_per_million' in day_data:
                    output[day_data['date']][
                        'new_vaccinations_smoothed_per_million'
                    ] = eval(str(day_data[
                        'new_vaccinations_smoothed_per_million']))
                else:
                    output[day_data['date']][
                        'new_vaccinations_smoothed_per_million'] = 0
            if new_people_vaccinated_smoothed:
                if 'new_people_vaccinated_smoothed' in day_data:
                    output[day_data['date']][
                        'new_people_vaccinated_smoothed'
                    ] = eval(str(day_data['new_people_vaccinated_smoothed']))
                else:
                    output[day_data['date']][
                        'new_people_vaccinated_smoothed'] = 0
            if new_people_vaccinated_smoothed_per_hundred:
                if 'new_people_vaccinated_smoothed_per_hundred' in day_data:
                    output[day_data['date']][
                        'new_people_vaccinated_smoothed_per_hundred'
                    ] = eval(str(day_data[
                        'new_people_vaccinated_smoothed_per_hundred'])
                    )
                else:
                    output[day_data['date']][
                        'new_people_vaccinated_smoothed_per_hundred'] = 0

        return output


def output(content: dict, country_code: str):  # ->
    file_name = country_code + ".txt"
    with open(file_name, "a") as doc:
        for key in content:
            doc.write("{'"+str(key) + "': "+str(content[key])+"}\n")


# =========
#   Start
# =========


iso_code = input(
    "What country do you want to agregate? " +
    "(use codes provided in country_codes.txt)\n")

while iso_code not in country_codes:
    iso_code = input(
        "Wrong code please use codes provided in country_codes.txt\n")


output(new_case_data(iso_code), iso_code)
