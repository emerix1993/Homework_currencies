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
        elif action == "add":
            add_currency = input("Enter add currency: ")
            if type_currency == add_currency:
                amount_add = int(input("Enter add amount: "))
                print(f"result: {amount + amount_add}")
            else:
                print("For this operation you need same currencies")
        elif action == "sub":
            sub_currency = input("Enter add currency: ")
            if type_currency == sub_currency:
                amount_add = int(input("Enter add amount: "))
                print(f"result: {amount - amount_add}")
            else:
                print("For this operation you need same currencies")




if __name__ == "__main__":
    main()
