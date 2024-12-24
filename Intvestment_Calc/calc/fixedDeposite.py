from calc.investment import Investment
class FixedDeposite(Investment):
    """This class will calculates the FixedDeposite using Investment class
    """
    def calculate(self):
        """this function calc the FD
        formula:
               total_amount = self.amount * (1 + returns) ** self.time
             
               
        """
        returns=self.rateofinterest/100
        total=self.amount * (1 + returns) ** self.time
        return total