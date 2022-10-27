

class Jar:
    # classmethod to check if n is positive int
    @classmethod
    def is_positive_int(cls, n):
        return True if float(n).is_integer() and n > 0 else False

    def __init__(self, capacity=12):
        # creates self._size variable
        self._size = 0
        # if capacity is positive int sets self._capacity variable
        # if not -> VE
        if Jar.is_positive_int(capacity):
            self._capacity = capacity
        else:
            raise ValueError

    def __str__(self):
        amount = ""
        # just a loop to concat string with emojes
        for cookie in range(self.size):
            amount += "🍪"
        return amount

    def deposit(self, n):
        #  if n is positive int calls self.size with positive n (+n)
        #  if not -> VE
        if Jar.is_positive_int(n):
            self.size = n
        else:
            raise ValueError

    def withdraw(self, n):
        #  if n is positive int calls self.size with negative n (-n)
        #  if not -> VE
        if Jar.is_positive_int(n):
            # * -1 makes n negative
            self.size = n * -1
        else:
            raise ValueError

    # getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # setter for capacity
    @capacity.setter
    def capacity(self, n):
        if Jar.is_positive_int(n):
            self._capacity = n
        else:
            raise ValueError

    # getter for size
    @property
    def size(self):
        return self._size

    # setter for size
    @size.setter
    def size(self, n):
        # if n is positive (+n) checks if current size + n <= capacity
        # if so increments size with n
        # if not -> VE
        if n > 0:
            if self.size + n <= self.capacity:
                self._size += n
            else:
                raise ValueError
        # is n is negative (-n) checks if current size + (-n) is >=0
        # if so increments (subtracts) size by n(-n)
        # if not -> VE
        elif n < 0:
            if self.size + n >= 0:
                self._size += n
            else:
                raise ValueError
