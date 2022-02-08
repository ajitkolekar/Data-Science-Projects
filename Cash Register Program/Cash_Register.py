# Author: Ajit Kolekar
# Cash Register Program

# This program asks user for the cost of each item in the cart and when
# done, displays the number of items in the cart and the total cost of them

# locale module is imported to print the amount in currency format
import locale


# class CashRegister is defined to keep track of number of items in the
# cart and the total cost of them
class CashRegister:

    # __init__ method to initiate an instance of CashRegister class.
    # The item_count and total_price attributes are set to 0 and 0.00
    # respectively if they are not passed in when the class is initiated
    def __init__(self, item_count=0, total_price=0.00):
        self.item_count = item_count
        self.total_price = total_price

    # get_count method returns the item_count attribute
    def get_count(self):
        return self.item_count

    # get_total method returns the total_price attribute
    def get_total(self):
        return self.total_price

    # add_item method increases the total_price by the price value passed in
    # and increments the item_count
    def add_item(self, price):
        self.item_count += 1
        self.total_price += price


# main function
def main():
    # setting locale for all categories to default
    locale.setlocale(locale.LC_ALL, '')
    # creating an instance of CashRegister class
    cash_register = CashRegister()
    # welcome message and request user input
    print('Welcome valued customer to the store!')
    print('Please begin the checkout process.')
    print('Enter the cost of an item in the cart one at a time.')
    print('Enter Y when done.')

    # the loop will continue until user enters 'y' or 'Y'
    while True:
        response = input('--> ')
        if response.upper() == 'Y':
            break
        try:
            # convert user response to float and call add_item function
            response = float(response)
            cash_register.add_item(response)
        # valueError exception is raised if the entered value is not number
        except ValueError:
            print('Please enter a valid amount')

    # display the total number of items and total price
    count = cash_register.get_count()
    amount = locale.currency(cash_register.get_total())

    print('Thank you for shopping!')
    print('Total number of items in your cart: {:>10}'.format(count))
    print('Total price of items in your cart:  {:>10}'.format(amount))


# call to main function
main()
