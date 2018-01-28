from myinvestorlib import yahoo_finance_scraper

# How to create a Animal object
cat = yahoo_finance_scraper.YahooFinanceScraper('Whiskers', 33, 10, 'Meow')

print(cat.toString())
