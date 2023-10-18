import requests

class Currency_convertor:
	rates = {} 
	def __init__(self, url):
		data = requests.get(url).json()

		self.rates = data["rates"] 

	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

if __name__ == "__main__":

	# got api access key from fixer.io
	url ='http://data.fixer.io/api/latest?access_key=a0b66cd8615ed8726d5a232ccca7f37d'
	c = Currency_convertor(url)
	from_country = input("From currency(e.g. USD): ")
	to_country = input("TO Country(e.g. INR): ")
	amount = int(input("Amount: "))

	c.convert(from_country, to_country, amount)
