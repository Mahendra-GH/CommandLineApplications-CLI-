from calc.investment import Investment
class Sip(Investment):
    """this class calculate the SIP Investement
    """
    def calculate(self):
        """This method will calculate the SIP
        """
        months = self.time * 12
        yearly_returns = self.rateofinterest/100
        returns = yearly_returns/12
        total_amount = (
            self.amount
            * (((1 + returns) ** months - 1) / returns)
            * (1 + returns)
        )
        return total_amount