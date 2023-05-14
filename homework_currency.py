class Price:
    exchange_rates = {'USD': 1, 'EUR': 1.2, 'GBP': 1.4, 'UAH': 0.027}  # exchange rates for currencies
    commision = 0.012


class Menu:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert(self, convert_currency):
        exchange_rate = Price.exchange_rates[convert_currency] / Price.exchange_rates[self.currency]
        if Price.exchange_rates[self.currency] != convert_currency:
            print("converted started")
            intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
            Price.exchange_rates[convert_currency] / intermediate
            converted_amount = self.amount / exchange_rate
            commision_operation = Price.commision * converted_amount
            print(f"commision system is -> {commision_operation} {convert_currency}")
            return f"you total is: {converted_amount - commision_operation} {convert_currency}"

    # def another_currency_to_uah(self, amount, currency):
    #     exchange_rate = Price.exchange_rates['UAH'] / Price.exchange_rates[self.currency]
    #     if Price.exchange_rates[self.currency] != "USD":
    #         print("converted started")
    #         intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
    #         Price.exchange_rates["UAH"] / intermediate
    #         converted_amount = self.amount / exchange_rate
    #         commision_operation = Price.commision * converted_amount
    #         print(f"commision system is -> {commision_operation} ₴")
    #         return f"you total is: {converted_amount - commision_operation} ₴"
    #
    # def another_currency_to_usd(self, amount, currency):
    #     exchange_rate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]  # calculate exchange rate
    #     converted_amount = self.amount * exchange_rate
    #     commision_operation = Price.commision * converted_amount
    #     print(f"commision system is -> {commision_operation} 💵")
    #     final_balance = converted_amount - commision_operation
    #     return f"you total is: {final_balance} 💵"
    #
    # def another_currency_to_eur(self, amount, currency):
    #     exchange_rate = Price.exchange_rates['EUR'] / Price.exchange_rates[self.currency]
    #     if Price.exchange_rates[self.currency] != "USD":
    #         print("converted started")
    #         intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
    #         Price.exchange_rates["EUR"] / intermediate
    #         converted_amount = self.amount / exchange_rate
    #         commision_operation = Price.commision * converted_amount
    #         print(f"commision system is -> {commision_operation} 💶")
    #         return f"you total is: {converted_amount - commision_operation} 💶"
    #
    # def another_currency_to_gbp(self, amount, currency):
    #     exchange_rate = Price.exchange_rates['GBP'] / Price.exchange_rates[self.currency]
    #     if Price.exchange_rates[self.currency] != "USD":
    #         print("converted started")
    #         intermediate = Price.exchange_rates[self.currency] / Price.exchange_rates["USD"]
    #         Price.exchange_rates["GBP"] / intermediate
    #         converted_amount = self.amount / exchange_rate
    #         commision_operation = Price.commision * converted_amount
    #         print(f"commision system is -> {commision_operation} 💷")
    #         return f"you total is: {converted_amount - commision_operation} 💷"

    def __sub__(self, other):
        if self.currency == other.currency:
            new_amount = self.amount - other.amount
            return Menu(new_amount, self.currency)
        else:
            raise ValueError("You need same currencies")

    def __add__(self, other):
        if self.currency == other.currency:
            return Menu(self.amount + other.amount, self.currency)
        else:
            raise ValueError("You need same currencies")


def main():
    while True:
        input_currency = input("Enter you currency: ")
        amount = int(input("Enter you amount: "))
        output_currency = input("Enter you currency: ")
        if input_currency != output_currency:
            menu = Menu(amount, input_currency)
            print(menu.convert(output_currency))
        else:
            action = input("Enter action: ")
            if action == "sub":
                output_amount = int(input("Enter output amount: "))
                menu1 = Menu(amount, input_currency)
                menu2 = Menu(output_amount, output_currency)
                result = menu1 - menu2
                print(f"result: {result.amount} {result.currency}")
            elif action == "add":
                output_amount = int(input("Enter output amount: "))
                menu1 = Menu(amount, input_currency)
                menu2 = Menu(output_amount, output_currency)
                result = menu1 + menu2
                print(f"result: {result.amount} {result.currency}")

        # if type_currency == "USD":
        #     pass
        # elif type_currency == "EUR":
        #     pass
        # elif type_currency == "UAH":
        #     pass
        # elif type_currency == "GBP":
        #     pass
        # amount = int(input("Enter you amount: "))
        # if type(amount) == str:
        #     raise TypeError
        # else:
        #     pass
        # action = input("Change you action: ")
        # if action == "convert":
        #     type_exchange_currency = input("Enter currency: ")
        #     if type_exchange_currency == type_currency:
        #         print("This is same currencies: ")
        #     elif type_exchange_currency == "USD":
        #         menu = Menu(amount, type_currency)
        #         print(menu.another_currency_to_usd(amount, type_currency))
        #     elif type_exchange_currency == "EUR":
        #         menu = Menu(amount, type_currency)
        #         print(menu.another_currency_to_eur(amount, type_currency))
        #         print("******")
        #         print(menu.convert("EUR"))
        #     elif type_exchange_currency == "UAH":
        #         menu = Menu(amount, type_currency)
        #         print(menu.another_currency_to_uah(amount, type_currency))
        #         print("*****")
        #         print(menu.convert("UAH"))
        #     elif type_exchange_currency == "GBP":
        #         menu = Menu(amount, type_currency)
        #         print(menu.another_currency_to_gbp(amount, type_currency))
        # elif action == "sub":
        #     sub_currency = input("Enter sub currency: ")
        #     if type_currency == sub_currency:
        #         sub_amount = int(input("Enter sub amount: "))
        #         menu1 = Menu(amount, type_currency)
        #         menu2 = Menu(sub_amount, sub_currency)
        #         result = menu1 - menu2
        #         print(f"result: {result.amount} {result.currency}")
        #     else:
        #         print("For this operation you need same currencies")
        # elif action == "add":
        #     sub_currency = input("Enter sub currency: ")
        #     if type_currency == sub_currency:
        #         sub_amount = int(input("Enter sub amount: "))
        #         menu1 = Menu(amount, type_currency)
        #         menu2 = Menu(sub_amount, sub_currency)
        #         result = menu1 + menu2
        #         print(f"result: {result.amount} {result.currency}")
        #     else:
        #         print("For this operation you need same currencies")


if __name__ == "__main__":
    main()
