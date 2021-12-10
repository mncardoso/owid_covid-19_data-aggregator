import matplotlib.pyplot as plt

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


iso_code = input(
    "What country do you want to agregate? " +
    "(use codes provided in country_codes.txt)\n")

while iso_code not in country_codes:
    iso_code = input(
        "Wrong code please use codes provided in country_codes.txt\n")

file_name = iso_code + ".txt"
data = []

with open(file_name, "r") as doc:
    for line in doc.readlines():
        line = eval(line)
        data.append(line)

data_date = []
data_new_cases_smoothed = []
data_new_deaths_smoothed = []

for day in data:
    for date in day:
        data_date.append(date)
        data_new_cases_smoothed.append(day[date]["new_cases_smoothed"])
        data_new_deaths_smoothed.append(day[date]["new_deaths_smoothed"])


plt.plot(data_date, data_new_cases_smoothed, label="New Cases Smoothed")
plt.plot(data_date, data_new_deaths_smoothed, label="New Deaths Smoothed")


plt.xlabel('date')
plt.ylabel('people')

plt.xticks(rotation=90)

plt.title('Covid-19')
plt.legend()

plt.show()
