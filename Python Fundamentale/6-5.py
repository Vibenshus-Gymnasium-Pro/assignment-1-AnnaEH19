Data = {
    'The nile': 'Egypt',
    'Yangtze': 'China',
    'Ob-Irtysh': 'Kazakhstan',
}

for rivers, country in Data.items():
    print(rivers.title() + " is a river in " + country.title() + ".")