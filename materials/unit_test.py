from myinvestorlib import yahoo

# How to create a Animal object
cat = yahoo.YahooFinanceScraper('Whiskers', 33, 10, 'Meow')

print(cat.toString())
