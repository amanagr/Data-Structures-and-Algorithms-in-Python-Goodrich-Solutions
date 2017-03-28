class CreditCard:
    ''' A consumer credit card'''
    def __init__(self, customer, bank, acnt, limit):
        ''' Create a new credit card instance

        The initial balance is zero.

        customer : name of the customer(Eg: 'aman')
        bank     : name of the bank (eg: 'SBI')
        acnt     : the account identifier (eg: 1234 1234 1234 1234)
        limit    : credit limit (measured in rupees)
        '''

        self._customer = customer           # _ is used to declare private varibles
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    def get_customer(self):
        ''' Return the name of the customer '''
        return self._customer

    def get_bank(self):
        ''' Return the bank's name '''
        return self._bank

    def get_acccount(self):
        ''' Return the account identifier '''
        return self._account

    def get_balance(self):
        ''' Return the account balance '''
        return self._balance

    def get_limit(self):
        ''' return the credit limit '''
        return self._limit

    def charge(self, price):
        ''' Charge given price to card, assuming sufficient credit limit.

        Return True if the charge was proceccessed. False otherwise '''

        if self._balance + price > self._limit:
            return False
        else :
            self._balance += price
            return True

    def make_payment(self, amount):
        ''' Process customer payment that reduces balance '''
        self._balance -= amount


cc = CreditCard("Aman Agrawal", "SBI", "1234", 1000)



cc.charge(15)
cc.make_payment(1)

print(cc.get_balance())















