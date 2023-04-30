class Price:
    exchange_rates = {'USD': 1, 'EUR': 1.2, 'GBP': 1.4, 'UAH': 0.027}  # exchange rates for currencies
    commision  = 0.012

class Menu:
    def __init__(self,amount, currency):
        self.amount = amount
        self.currency = currency

    def another_currency_to_uah(self, amount, currency):
        exchange_rate = Price.exchange_rates['UAH'] / Price.exchange_rates[self.currency]
        if Price.exchange_rates[self.currency] != "USD":
            print("converted started")
            intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
            Price.exchange_rates["UAH"] / intermediate
            converted_amount = self.amount / exchange_rate
            commision_operation = Price.commision*converted_amount
            print(f"commision system is -> {commision_operation} UAH")
            return f"you total is: {converted_amount - commision_operation}"

    def another_currency_to_usd(self,amount, currency):
        exchange_rate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]  # calculate exchange rate
        converted_amount = self.amount * exchange_rate
        commision_operation = Price.commision * converted_amount
        print(f"commision system is -> {commision_operation} USD")
        final_balance = converted_amount - commision_operation
        return final_balance



    def another_currency_to_eur(self,amount, currency):
        exchange_rate = Price.exchange_rates['EUR'] / Price.exchange_rates[self.currency]
        if Price.exchange_rates[self.currency] != "USD":
            print("converted started")
            intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
            Price.exchange_rates["EUR"] / intermediate
            converted_amount = self.amount / exchange_rate
            commision_operation = Price.commision*converted_amount
            print(f"commision system is -> {commision_operation} EUR")
            return f"you total is: {converted_amount - commision_operation}"

    def another_currency_to_gbp(self,amount, currency):
        exchange_rate = Price.exchange_rates['GBP'] / Price.exchange_rates[self.currency]
        if Price.exchange_rates[self.currency] != "USD":
            print("converted started")
            intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
            Price.exchange_rates["GBP"] / intermediate
            converted_amount = self.amount / exchange_rate
            commision_operation = Price.commision*converted_amount
            print(f"commision system is -> {commision_operation} GBP")
            return f"you total is: {converted_amount - commision_operation}"

    # def convert_from(self, currency: str, amount: float) -> 'Price':
    #     if self.currency == currency:
    #         return Price(self.amount, self.currency)
    #     else:
    #         # convert to USD first
    #         usd_amount = self.convert_to('USD').amount
    #         # convert to target currency
    #         converted_amount = Price(usd_amount, 'USD').convert_to(currency).amount
    #         return Price(converted_amount, currency)


def main():
    while True:
        type_currency = input("Enter you currency: ")
        if type_currency == "USD":
            pass
        elif type_currency == "EUR":
            pass
        elif type_currency == "UAH":
            pass
        elif type_currency == "GBP":
            pass
        amount = int(input("Enter you amount: "))
        if type(amount) == str:
            raise TypeError
        else:
            pass
        action = input("Change you action: ")
        if action == "convert":
            pass
        type_exchange_currency = input("Enter currency: ")
        if type_exchange_currency == type_currency:
            print("This is same currencies: ")
        elif type_exchange_currency == "USD":
            menu = Menu(amount,type_currency)
            print(menu.another_currency_to_usd(amount, type_currency))
        elif type_exchange_currency == "EUR":
            menu = Menu(amount,type_currency)
            print(menu.another_currency_to_eur(amount, type_currency))
        elif type_exchange_currency == "UAH":
            menu = Menu(amount, type_currency)
            print(menu.another_currency_to_uah(amount, type_currency))
        elif type_exchange_currency == "GBP":
            menu = Menu(amount, type_currency)
            print(menu.another_currency_to_gbp(amount, type_currency))


if __name__ == "__main__":
    main()

#
#     def __add__(self, other):
#         if self.currency == other.currency:
#             result_amount = self.amount + other.amount
#             result_currency = self.currency
#         else:
#             converted_amount = self.convert_to('USD').amount + other.convert_to('USD').amount
#             result_amount = self.convert_from('USD', converted_amount).amount
#             result_currency = self.currency if self.currency != 'USD' else other.currency
#         return Price(result_amount, result_currency)
#
#     def __sub__(self, other: "Price") -> 'Price':
#         if self.currency == other.currency:
#             result_amount = self.amount - other.amount
#             result_currency = self.currency
#         else:
#             converted_amount = self.convert_to('USD').amount - other.convert_to('USD').amount
#             result_amount = self.convert_from('USD', converted_amount).amount
#             result_currency = self.currency if self.currency != 'USD' else other.currency
#         return Price(result_amount, result_currency)
#
#     def convert_to(self, currency: str) -> 'Price':
#         if self.currency == currency:
#             return self
#         else:
#             converted_amount = self.amount * self.exchange_rates[currency] / self.exchange_rates[self.currency]
#             return Price(converted_amount, currency)
#
#     def convert_from(self, currency: str, amount: float) -> 'Price':
#         if self.currency == currency:
#             return Price(amount, self.currency)
#         else:
#             converted_amount = amount * self.exchange_rates[self.currency] / self.exchange_rates[currency]
#             return Price(converted_amount, self.currency)
#
#     def __repr__(self) -> str:
#         return f'{self.amount:.2f} {self.currency}'
#
# price1 = Price(100,"USD")
# price2 = Price(50, 'EUR')
# price3 = Price(2000,"UAH")
# result = price1 + price2 + price3
# print(result) # выведет "141.67 USD"
