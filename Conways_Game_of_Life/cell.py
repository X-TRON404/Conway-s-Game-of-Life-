import random

class Cell:
    def __init__(self,status=None):
        '''
        Initialize a cell with the boolean argument status if argument is passed or else a random ON/OFF (True/False) status for the cell
        '''
        self.status = status if status is not None else True if random.randint(0, 1) == 1 else False

    def is_ON(self):
        '''
        Check ON status of the cell. If ON return True, else return False.
        '''
        if type(self.status) not in [bool]:
            raise TypeError('ON/OFF state must be a boolean value')
        return self.status
        
    def turn_ON(self):
        '''
        Turn ON the cell
        '''
        if type(self.status) not in [bool]:
            raise TypeError('ON/OFF state must be a boolean value')
        self.status = True

    def turn_OFF(self):
        '''
        Turn OFF the cell
        '''
        if type(self.status) not in [bool]:
            raise TypeError('ON/OFF state must be a boolean value')
        self.status = False