from constants.country_config import COUNTRY_CODE

SINGAPORE_LABEL = 'Singapore'
GLOBAL_LABEL = 'Global'

ALT_GEO_NOT_FOUND = "Unknown"

DEFAULT_DB_NAME = 'COVID_VACCINE'

GEOCODER_AGENT_NAME = 'pulse-monitoring'

FLAG_FIX_USA = 'united-states-of-america'
FLAG_URL = 'https://cdn.countryflags.com/thumbs/{}/flag-400.png'

TWITTER_BASE_URL = 'https://twitter.com/'
TWITTER_STATUS_PATH = TWITTER_BASE_URL + '{}/status/{}'

# Dates
DATE_FORMAT = '%Y-%m-%d'

# from pycountry package
COUNTRY_TO_ALPHA2 = {'Aruba': 'AW',
                     'Afghanistan': 'AF',
                     'Angola': 'AO',
                     'Anguilla': 'AI',
                     'Åland Islands': 'AX',
                     'Albania': 'AL',
                     'Andorra': 'AD',
                     'United Arab Emirates': 'AE',
                     'Argentina': 'AR',
                     'Armenia': 'AM',
                     'American Samoa': 'AS',
                     'Antarctica': 'AQ',
                     'French Southern Territories': 'TF',
                     'Antigua and Barbuda': 'AG',
                     'Australia': 'AU',
                     'Austria': 'AT',
                     'Azerbaijan': 'AZ',
                     'Burundi': 'BI',
                     'Belgium': 'BE',
                     'Benin': 'BJ',
                     'Bonaire, Sint Eustatius and Saba': 'BQ',
                     'Burkina Faso': 'BF',
                     'Bangladesh': 'BD',
                     'Bulgaria': 'BG',
                     'Bahrain': 'BH',
                     'Bahamas': 'BS',
                     'Bosnia and Herzegovina': 'BA',
                     'Saint Barthélemy': 'BL',
                     'Belarus': 'BY',
                     'Belize': 'BZ',
                     'Bermuda': 'BM',
                     'Bolivia, Plurinational State of': 'BO',
                     'Brazil': 'BR',
                     'Barbados': 'BB',
                     'Brunei Darussalam': 'BN',
                     'Bhutan': 'BT',
                     'Bouvet Island': 'BV',
                     'Botswana': 'BW',
                     'Central African Republic': 'CF',
                     'Canada': 'CA',
                     'Cocos (Keeling) Islands': 'CC',
                     'Switzerland': 'CH',
                     'Chile': 'CL',
                     'China': 'CN',
                     "Côte d'Ivoire": 'CI',
                     'Cameroon': 'CM',
                     'Congo, The Democratic Republic of the': 'CD',
                     'Congo': 'CG',
                     'Cook Islands': 'CK',
                     'Colombia': 'CO',
                     'Comoros': 'KM',
                     'Cabo Verde': 'CV',
                     'Costa Rica': 'CR',
                     'Cuba': 'CU',
                     'Curaçao': 'CW',
                     'Christmas Island': 'CX',
                     'Cayman Islands': 'KY',
                     'Cyprus': 'CY',
                     'Czechia': 'CZ',
                     'Germany': 'DE',
                     'Djibouti': 'DJ',
                     'Dominica': 'DM',
                     'Denmark': 'DK',
                     'Dominican Republic': 'DO',
                     'Algeria': 'DZ',
                     'Ecuador': 'EC',
                     'Egypt': 'EG',
                     'Eritrea': 'ER',
                     'Western Sahara': 'EH',
                     'Spain': 'ES',
                     'Estonia': 'EE',
                     'Ethiopia': 'ET',
                     'Finland': 'FI',
                     'Fiji': 'FJ',
                     'Falkland Islands (Malvinas)': 'FK',
                     'France': 'FR',
                     'Faroe Islands': 'FO',
                     'Micronesia, Federated States of': 'FM',
                     'Gabon': 'GA',
                     'United Kingdom': 'GB',
                     'Georgia': 'GE',
                     'Guernsey': 'GG',
                     'Ghana': 'GH',
                     'Gibraltar': 'GI',
                     'Guinea': 'GN',
                     'Guadeloupe': 'GP',
                     'Gambia': 'GM',
                     'Guinea-Bissau': 'GW',
                     'Equatorial Guinea': 'GQ',
                     'Greece': 'GR',
                     'Grenada': 'GD',
                     'Greenland': 'GL',
                     'Guatemala': 'GT',
                     'French Guiana': 'GF',
                     'Guam': 'GU',
                     'Guyana': 'GY',
                     'Hong Kong': 'HK',
                     'Heard Island and McDonald Islands': 'HM',
                     'Honduras': 'HN',
                     'Croatia': 'HR',
                     'Haiti': 'HT',
                     'Hungary': 'HU',
                     'Indonesia': 'ID',
                     'Isle of Man': 'IM',
                     'India': 'IN',
                     'British Indian Ocean Territory': 'IO',
                     'Ireland': 'IE',
                     'Iran, Islamic Republic of': 'IR',
                     'Iraq': 'IQ',
                     'Iceland': 'IS',
                     'Israel': 'IL',
                     'Italy': 'IT',
                     'Jamaica': 'JM',
                     'Jersey': 'JE',
                     'Jordan': 'JO',
                     'Japan': 'JP',
                     'Kazakhstan': 'KZ',
                     'Kenya': 'KE',
                     'Kyrgyzstan': 'KG',
                     'Cambodia': 'KH',
                     'Kiribati': 'KI',
                     'Saint Kitts and Nevis': 'KN',
                     'Korea, Republic of': 'KR',
                     'Kuwait': 'KW',
                     "Lao People's Democratic Republic": 'LA',
                     'Lebanon': 'LB',
                     'Liberia': 'LR',
                     'Libya': 'LY',
                     'Saint Lucia': 'LC',
                     'Liechtenstein': 'LI',
                     'Sri Lanka': 'LK',
                     'Lesotho': 'LS',
                     'Lithuania': 'LT',
                     'Luxembourg': 'LU',
                     'Latvia': 'LV',
                     'Macao': 'MO',
                     'Saint Martin (French part)': 'MF',
                     'Morocco': 'MA',
                     'Monaco': 'MC',
                     'Moldova, Republic of': 'MD',
                     'Madagascar': 'MG',
                     'Maldives': 'MV',
                     'Mexico': 'MX',
                     'Marshall Islands': 'MH',
                     'North Macedonia': 'MK',
                     'Mali': 'ML',
                     'Malta': 'MT',
                     'Myanmar': 'MM',
                     'Montenegro': 'ME',
                     'Mongolia': 'MN',
                     'Northern Mariana Islands': 'MP',
                     'Mozambique': 'MZ',
                     'Mauritania': 'MR',
                     'Montserrat': 'MS',
                     'Martinique': 'MQ',
                     'Mauritius': 'MU',
                     'Malawi': 'MW',
                     'Malaysia': 'MY',
                     'Mayotte': 'YT',
                     'Namibia': 'NA',
                     'New Caledonia': 'NC',
                     'Niger': 'NE',
                     'Norfolk Island': 'NF',
                     'Nigeria': 'NG',
                     'Nicaragua': 'NI',
                     'Niue': 'NU',
                     'Netherlands': 'NL',
                     'Norway': 'NO',
                     'Nepal': 'NP',
                     'Nauru': 'NR',
                     'New Zealand': 'NZ',
                     'Oman': 'OM',
                     'Pakistan': 'PK',
                     'Panama': 'PA',
                     'Pitcairn': 'PN',
                     'Peru': 'PE',
                     'Philippines': 'PH',
                     'Palau': 'PW',
                     'Papua New Guinea': 'PG',
                     'Poland': 'PL',
                     'Puerto Rico': 'PR',
                     "Korea, Democratic People's Republic of": 'KP',
                     'Portugal': 'PT',
                     'Paraguay': 'PY',
                     'Palestine, State of': 'PS',
                     'French Polynesia': 'PF',
                     'Qatar': 'QA',
                     'Réunion': 'RE',
                     'Romania': 'RO',
                     'Russian Federation': 'RU',
                     'Rwanda': 'RW',
                     'Saudi Arabia': 'SA',
                     'Sudan': 'SD',
                     'Senegal': 'SN',
                     'Singapore': 'SG',
                     'South Georgia and the South Sandwich Islands': 'GS',
                     'Saint Helena, Ascension and Tristan da Cunha': 'SH',
                     'Svalbard and Jan Mayen': 'SJ',
                     'Solomon Islands': 'SB',
                     'Sierra Leone': 'SL',
                     'El Salvador': 'SV',
                     'San Marino': 'SM',
                     'Somalia': 'SO',
                     'Saint Pierre and Miquelon': 'PM',
                     'Serbia': 'RS',
                     'South Sudan': 'SS',
                     'Sao Tome and Principe': 'ST',
                     'Suriname': 'SR',
                     'Slovakia': 'SK',
                     'Slovenia': 'SI',
                     'Sweden': 'SE',
                     'Eswatini': 'SZ',
                     'Sint Maarten (Dutch part)': 'SX',
                     'Seychelles': 'SC',
                     'Syrian Arab Republic': 'SY',
                     'Turks and Caicos Islands': 'TC',
                     'Chad': 'TD',
                     'Togo': 'TG',
                     'Thailand': 'TH',
                     'Tajikistan': 'TJ',
                     'Tokelau': 'TK',
                     'Turkmenistan': 'TM',
                     'Timor-Leste': 'TL',
                     'Tonga': 'TO',
                     'Trinidad and Tobago': 'TT',
                     'Tunisia': 'TN',
                     'Turkey': 'TR',
                     'Tuvalu': 'TV',
                     'Taiwan, Province of China': 'TW',
                     'Tanzania, United Republic of': 'TZ',
                     'Uganda': 'UG',
                     'Ukraine': 'UA',
                     'United States Minor Outlying Islands': 'UM',
                     'Uruguay': 'UY',
                     'United States': 'US',
                     'Uzbekistan': 'UZ',
                     'Holy See (Vatican City State)': 'VA',
                     'Saint Vincent and the Grenadines': 'VC',
                     'Venezuela, Bolivarian Republic of': 'VE',
                     'Virgin Islands, British': 'VG',
                     'Virgin Islands, U.S.': 'VI',
                     'Viet Nam': 'VN',
                     'Vanuatu': 'VU',
                     'Wallis and Futuna': 'WF',
                     'Samoa': 'WS',
                     'Yemen': 'YE',
                     'South Africa': 'ZA',
                     'Zambia': 'ZM',
                     'Zimbabwe': 'ZW'}

ALPHA2_TO_COUNTRY = {'AW': 'Aruba',
                     'AF': 'Afghanistan',
                     'AO': 'Angola',
                     'AI': 'Anguilla',
                     'AX': 'Åland Islands',
                     'AL': 'Albania',
                     'AD': 'Andorra',
                     'AE': 'United Arab Emirates',
                     'AR': 'Argentina',
                     'AM': 'Armenia',
                     'AS': 'American Samoa',
                     'AQ': 'Antarctica',
                     'TF': 'French Southern Territories',
                     'AG': 'Antigua and Barbuda',
                     'AU': 'Australia',
                     'AT': 'Austria',
                     'AZ': 'Azerbaijan',
                     'BI': 'Burundi',
                     'BE': 'Belgium',
                     'BJ': 'Benin',
                     'BQ': 'Bonaire, Sint Eustatius and Saba',
                     'BF': 'Burkina Faso',
                     'BD': 'Bangladesh',
                     'BG': 'Bulgaria',
                     'BH': 'Bahrain',
                     'BS': 'Bahamas',
                     'BA': 'Bosnia and Herzegovina',
                     'BL': 'Saint Barthélemy',
                     'BY': 'Belarus',
                     'BZ': 'Belize',
                     'BM': 'Bermuda',
                     'BO': 'Bolivia, Plurinational State of',
                     'BR': 'Brazil',
                     'BB': 'Barbados',
                     'BN': 'Brunei Darussalam',
                     'BT': 'Bhutan',
                     'BV': 'Bouvet Island',
                     'BW': 'Botswana',
                     'CF': 'Central African Republic',
                     'CA': 'Canada',
                     'CC': 'Cocos (Keeling) Islands',
                     'CH': 'Switzerland',
                     'CL': 'Chile',
                     'CN': 'China',
                     'CI': "Côte d'Ivoire",
                     'CM': 'Cameroon',
                     'CD': 'Congo, The Democratic Republic of the',
                     'CG': 'Congo',
                     'CK': 'Cook Islands',
                     'CO': 'Colombia',
                     'KM': 'Comoros',
                     'CV': 'Cabo Verde',
                     'CR': 'Costa Rica',
                     'CU': 'Cuba',
                     'CW': 'Curaçao',
                     'CX': 'Christmas Island',
                     'KY': 'Cayman Islands',
                     'CY': 'Cyprus',
                     'CZ': 'Czechia',
                     'DE': 'Germany',
                     'DJ': 'Djibouti',
                     'DM': 'Dominica',
                     'DK': 'Denmark',
                     'DO': 'Dominican Republic',
                     'DZ': 'Algeria',
                     'EC': 'Ecuador',
                     'EG': 'Egypt',
                     'ER': 'Eritrea',
                     'EH': 'Western Sahara',
                     'ES': 'Spain',
                     'EE': 'Estonia',
                     'ET': 'Ethiopia',
                     'FI': 'Finland',
                     'FJ': 'Fiji',
                     'FK': 'Falkland Islands (Malvinas)',
                     'FR': 'France',
                     'FO': 'Faroe Islands',
                     'FM': 'Micronesia, Federated States of',
                     'GA': 'Gabon',
                     'GB': 'United Kingdom',
                     'GE': 'Georgia',
                     'GG': 'Guernsey',
                     'GH': 'Ghana',
                     'GI': 'Gibraltar',
                     'GN': 'Guinea',
                     'GP': 'Guadeloupe',
                     'GM': 'Gambia',
                     'GW': 'Guinea-Bissau',
                     'GQ': 'Equatorial Guinea',
                     'GR': 'Greece',
                     'GD': 'Grenada',
                     'GL': 'Greenland',
                     'GT': 'Guatemala',
                     'GF': 'French Guiana',
                     'GU': 'Guam',
                     'GY': 'Guyana',
                     'HK': 'Hong Kong',
                     'HM': 'Heard Island and McDonald Islands',
                     'HN': 'Honduras',
                     'HR': 'Croatia',
                     'HT': 'Haiti',
                     'HU': 'Hungary',
                     'ID': 'Indonesia',
                     'IM': 'Isle of Man',
                     'IN': 'India',
                     'IO': 'British Indian Ocean Territory',
                     'IE': 'Ireland',
                     'IR': 'Iran, Islamic Republic of',
                     'IQ': 'Iraq',
                     'IS': 'Iceland',
                     'IL': 'Israel',
                     'IT': 'Italy',
                     'JM': 'Jamaica',
                     'JE': 'Jersey',
                     'JO': 'Jordan',
                     'JP': 'Japan',
                     'KZ': 'Kazakhstan',
                     'KE': 'Kenya',
                     'KG': 'Kyrgyzstan',
                     'KH': 'Cambodia',
                     'KI': 'Kiribati',
                     'KN': 'Saint Kitts and Nevis',
                     'KR': 'Korea, Republic of',
                     'KW': 'Kuwait',
                     'LA': "Lao People's Democratic Republic",
                     'LB': 'Lebanon',
                     'LR': 'Liberia',
                     'LY': 'Libya',
                     'LC': 'Saint Lucia',
                     'LI': 'Liechtenstein',
                     'LK': 'Sri Lanka',
                     'LS': 'Lesotho',
                     'LT': 'Lithuania',
                     'LU': 'Luxembourg',
                     'LV': 'Latvia',
                     'MO': 'Macao',
                     'MF': 'Saint Martin (French part)',
                     'MA': 'Morocco',
                     'MC': 'Monaco',
                     'MD': 'Moldova, Republic of',
                     'MG': 'Madagascar',
                     'MV': 'Maldives',
                     'MX': 'Mexico',
                     'MH': 'Marshall Islands',
                     'MK': 'North Macedonia',
                     'ML': 'Mali',
                     'MT': 'Malta',
                     'MM': 'Myanmar',
                     'ME': 'Montenegro',
                     'MN': 'Mongolia',
                     'MP': 'Northern Mariana Islands',
                     'MZ': 'Mozambique',
                     'MR': 'Mauritania',
                     'MS': 'Montserrat',
                     'MQ': 'Martinique',
                     'MU': 'Mauritius',
                     'MW': 'Malawi',
                     'MY': 'Malaysia',
                     'YT': 'Mayotte',
                     'NA': 'Namibia',
                     'NC': 'New Caledonia',
                     'NE': 'Niger',
                     'NF': 'Norfolk Island',
                     'NG': 'Nigeria',
                     'NI': 'Nicaragua',
                     'NU': 'Niue',
                     'NL': 'Netherlands',
                     'NO': 'Norway',
                     'NP': 'Nepal',
                     'NR': 'Nauru',
                     'NZ': 'New Zealand',
                     'OM': 'Oman',
                     'PK': 'Pakistan',
                     'PA': 'Panama',
                     'PN': 'Pitcairn',
                     'PE': 'Peru',
                     'PH': 'Philippines',
                     'PW': 'Palau',
                     'PG': 'Papua New Guinea',
                     'PL': 'Poland',
                     'PR': 'Puerto Rico',
                     'KP': "Korea, Democratic People's Republic of",
                     'PT': 'Portugal',
                     'PY': 'Paraguay',
                     'PS': 'Palestine, State of',
                     'PF': 'French Polynesia',
                     'QA': 'Qatar',
                     'RE': 'Réunion',
                     'RO': 'Romania',
                     'RU': 'Russian Federation',
                     'RW': 'Rwanda',
                     'SA': 'Saudi Arabia',
                     'SD': 'Sudan',
                     'SN': 'Senegal',
                     'SG': 'Singapore',
                     'GS': 'South Georgia and the South Sandwich Islands',
                     'SH': 'Saint Helena, Ascension and Tristan da Cunha',
                     'SJ': 'Svalbard and Jan Mayen',
                     'SB': 'Solomon Islands',
                     'SL': 'Sierra Leone',
                     'SV': 'El Salvador',
                     'SM': 'San Marino',
                     'SO': 'Somalia',
                     'PM': 'Saint Pierre and Miquelon',
                     'RS': 'Serbia',
                     'SS': 'South Sudan',
                     'ST': 'Sao Tome and Principe',
                     'SR': 'Suriname',
                     'SK': 'Slovakia',
                     'SI': 'Slovenia',
                     'SE': 'Sweden',
                     'SZ': 'Eswatini',
                     'SX': 'Sint Maarten (Dutch part)',
                     'SC': 'Seychelles',
                     'SY': 'Syrian Arab Republic',
                     'TC': 'Turks and Caicos Islands',
                     'TD': 'Chad',
                     'TG': 'Togo',
                     'TH': 'Thailand',
                     'TJ': 'Tajikistan',
                     'TK': 'Tokelau',
                     'TM': 'Turkmenistan',
                     'TL': 'Timor-Leste',
                     'TO': 'Tonga',
                     'TT': 'Trinidad and Tobago',
                     'TN': 'Tunisia',
                     'TR': 'Turkey',
                     'TV': 'Tuvalu',
                     'TW': 'Taiwan, Province of China',
                     'TZ': 'Tanzania, United Republic of',
                     'UG': 'Uganda',
                     'UA': 'Ukraine',
                     'UM': 'United States Minor Outlying Islands',
                     'UY': 'Uruguay',
                     'US': 'United States',
                     'UZ': 'Uzbekistan',
                     'VA': 'Holy See (Vatican City State)',
                     'VC': 'Saint Vincent and the Grenadines',
                     'VE': 'Venezuela, Bolivarian Republic of',
                     'VG': 'Virgin Islands, British',
                     'VI': 'Virgin Islands, U.S.',
                     'VN': 'Viet Nam',
                     'VU': 'Vanuatu',
                     'WF': 'Wallis and Futuna',
                     'WS': 'Samoa',
                     'YE': 'Yemen',
                     'ZA': 'South Africa',
                     'ZM': 'Zambia',
                     'ZW': 'Zimbabwe'}

COUNTRY_APLHA_2_TO_3 = {'AW': 'ABW', 'AF': 'AFG', 'AO': 'AGO', 'AI': 'AIA', 'AX': 'ALA', 'AL': 'ALB', 'AD': 'AND', 'AE': 'ARE',
                        'AR': 'ARG', 'AM': 'ARM', 'AS': 'ASM', 'AQ': 'ATA', 'TF': 'ATF', 'AG': 'ATG', 'AU': 'AUS', 'AT': 'AUT', 'AZ': 'AZE', 'BI': 'BDI',
                        'BE': 'BEL', 'BJ': 'BEN', 'BQ': 'BES', 'BF': 'BFA', 'BD': 'BGD', 'BG': 'BGR', 'BH': 'BHR', 'BS': 'BHS', 'BA': 'BIH', 'BL': 'BLM',
                        'BY': 'BLR', 'BZ': 'BLZ', 'BM': 'BMU', 'BO': 'BOL', 'BR': 'BRA', 'BB': 'BRB', 'BN': 'BRN', 'BT': 'BTN', 'BV': 'BVT', 'BW': 'BWA',
                        'CF': 'CAF', 'CA': 'CAN', 'CC': 'CCK', 'CH': 'CHE', 'CL': 'CHL', 'CN': 'CHN', 'CI': 'CIV', 'CM': 'CMR', 'CD': 'COD', 'CG': 'COG',
                        'CK': 'COK', 'CO': 'COL', 'KM': 'COM', 'CV': 'CPV', 'CR': 'CRI', 'CU': 'CUB', 'CW': 'CUW', 'CX': 'CXR', 'KY': 'CYM', 'CY': 'CYP',
                        'CZ': 'CZE', 'DE': 'DEU', 'DJ': 'DJI', 'DM': 'DMA', 'DK': 'DNK', 'DO': 'DOM', 'DZ': 'DZA', 'EC': 'ECU', 'EG': 'EGY', 'ER': 'ERI',
                        'EH': 'ESH', 'ES': 'ESP', 'EE': 'EST', 'ET': 'ETH', 'FI': 'FIN', 'FJ': 'FJI', 'FK': 'FLK', 'FR': 'FRA', 'FO': 'FRO', 'FM': 'FSM',
                        'GA': 'GAB', 'GB': 'GBR', 'GE': 'GEO', 'GG': 'GGY', 'GH': 'GHA', 'GI': 'GIB', 'GN': 'GIN', 'GP': 'GLP', 'GM': 'GMB', 'GW': 'GNB',
                        'GQ': 'GNQ', 'GR': 'GRC', 'GD': 'GRD', 'GL': 'GRL', 'GT': 'GTM', 'GF': 'GUF', 'GU': 'GUM', 'GY': 'GUY', 'HK': 'HKG', 'HM': 'HMD',
                        'HN': 'HND', 'HR': 'HRV', 'HT': 'HTI', 'HU': 'HUN', 'ID': 'IDN', 'IM': 'IMN', 'IN': 'IND', 'IO': 'IOT', 'IE': 'IRL', 'IR': 'IRN',
                        'IQ': 'IRQ', 'IS': 'ISL', 'IL': 'ISR', 'IT': 'ITA', 'JM': 'JAM', 'JE': 'JEY', 'JO': 'JOR', 'JP': 'JPN', 'KZ': 'KAZ', 'KE': 'KEN',
                        'KG': 'KGZ', 'KH': 'KHM', 'KI': 'KIR', 'KN': 'KNA', 'KR': 'KOR', 'KW': 'KWT', 'LA': 'LAO', 'LB': 'LBN', 'LR': 'LBR', 'LY': 'LBY',
                        'LC': 'LCA', 'LI': 'LIE', 'LK': 'LKA', 'LS': 'LSO', 'LT': 'LTU', 'LU': 'LUX', 'LV': 'LVA', 'MO': 'MAC', 'MF': 'MAF', 'MA': 'MAR',
                        'MC': 'MCO', 'MD': 'MDA', 'MG': 'MDG', 'MV': 'MDV', 'MX': 'MEX', 'MH': 'MHL', 'MK': 'MKD', 'ML': 'MLI', 'MT': 'MLT', 'MM': 'MMR',
                        'ME': 'MNE', 'MN': 'MNG', 'MP': 'MNP', 'MZ': 'MOZ', 'MR': 'MRT', 'MS': 'MSR', 'MQ': 'MTQ', 'MU': 'MUS', 'MW': 'MWI', 'MY': 'MYS',
                        'YT': 'MYT', 'NA': 'NAM', 'NC': 'NCL', 'NE': 'NER', 'NF': 'NFK', 'NG': 'NGA', 'NI': 'NIC', 'NU': 'NIU', 'NL': 'NLD', 'NO': 'NOR',
                        'NP': 'NPL', 'NR': 'NRU', 'NZ': 'NZL', 'OM': 'OMN', 'PK': 'PAK', 'PA': 'PAN', 'PN': 'PCN', 'PE': 'PER', 'PH': 'PHL', 'PW': 'PLW',
                        'PG': 'PNG', 'PL': 'POL', 'PR': 'PRI', 'KP': 'PRK', 'PT': 'PRT', 'PY': 'PRY', 'PS': 'PSE', 'PF': 'PYF', 'QA': 'QAT', 'RE': 'REU',
                        'RO': 'ROU', 'RU': 'RUS', 'RW': 'RWA', 'SA': 'SAU', 'SD': 'SDN', 'SN': 'SEN', 'SG': 'SGP', 'GS': 'SGS', 'SH': 'SHN', 'SJ': 'SJM',
                        'SB': 'SLB', 'SL': 'SLE', 'SV': 'SLV', 'SM': 'SMR', 'SO': 'SOM', 'PM': 'SPM', 'RS': 'SRB', 'SS': 'SSD', 'ST': 'STP', 'SR': 'SUR',
                        'SK': 'SVK', 'SI': 'SVN', 'SE': 'SWE', 'SZ': 'SWZ', 'SX': 'SXM', 'SC': 'SYC', 'SY': 'SYR', 'TC': 'TCA', 'TD': 'TCD', 'TG': 'TGO',
                        'TH': 'THA', 'TJ': 'TJK', 'TK': 'TKL', 'TM': 'TKM', 'TL': 'TLS', 'TO': 'TON', 'TT': 'TTO', 'TN': 'TUN', 'TR': 'TUR', 'TV': 'TUV',
                        'TW': 'TWN', 'TZ': 'TZA', 'UG': 'UGA', 'UA': 'UKR', 'UM': 'UMI', 'UY': 'URY', 'US': 'USA', 'UZ': 'UZB', 'VA': 'VAT', 'VC': 'VCT',
                        'VE': 'VEN', 'VG': 'VGB', 'VI': 'VIR', 'VN': 'VNM', 'VU': 'VUT', 'WF': 'WLF', 'WS': 'WSM', 'YE': 'YEM', 'ZA': 'ZAF', 'ZM': 'ZMB',
                        'ZW': 'ZWE'}


if COUNTRY_CODE:
    COUNTRY = ALPHA2_TO_COUNTRY[COUNTRY_CODE]
    DATA_PATH = 'data/{}/'.format(COUNTRY.lower())
    TWEETS_PATH = DATA_PATH + '{}_tweets.csv'.format(COUNTRY.lower())
else:
    COUNTRY = None
    DATA_PATH = 'data/{}/'.format(GLOBAL_LABEL.lower())
    TWEETS_PATH = DATA_PATH + '{}_tweets.csv'.format(GLOBAL_LABEL.lower())

DATA_DASH_PATH = DATA_PATH + 'dash_output/'

FRAGMENTED_TWEETS_PATH = DATA_PATH + 'fragmented_tweets/tweets/'
FRAGMENTED_TWEETS_ENGAGEMENTS_PATH = DATA_PATH + \
    'fragmented_tweets/tweets_engagements/'
