"""This investment.py is returns Investment
"""
class Investment:
    """this class is about Inverstment

    """
    def __init__(self,amount,rateofinterest,time):
        """initilizing the amount,rateofinterest,time

        Args:
            amount (float): Enter Amount to calc
            rateofinterest (int):enter rateofinterest
            time (int): time_in_years
        """
        self._amount=amount
        self._rateofinterest=rateofinterest
        self._time=time
    @property
    def amount(self):
        """Getter property amount
        Returns: float
        """
        return self._amount
    
    @property
    def rateofinterest(self):
        """property for rateofinterest
        Returns:float
        """
        return self._rateofinterest
    @property
    def time(self):
        """Property for time
        Returns: int
        """
        return self._time
        