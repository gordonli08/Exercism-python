from threading import Lock

STATUS_NEW = 'new'
STATUS_OPEN = 'open'
STATUS_CLOSED = 'closed'

class BankAccount:
    def __init__(self):
        self._status = STATUS_NEW
        self._lock = Lock()

    def get_balance(self):
        with self._lock:
            if self._status != STATUS_OPEN:
                raise ValueError('Account is not available. Please open an account.')
            return self._balance

    def open(self):
        with self._lock:
            if self._status == STATUS_OPEN:
                raise ValueError('Cannot open an open account')
            self._balance = 0
            self._status = STATUS_OPEN

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Cannot deposit a negative amount')
        with self._lock:
            if self._status != STATUS_OPEN:
                raise ValueError('Account is closed or has not been opened')
            self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Cannot withdraw a negative amount')
        with self._lock:
            if self._status != STATUS_OPEN:
                raise ValueError('Account is closed or has not been opened')
            if amount > self._balance:
                raise ValueError('Cannot withdraw more than balance')
            self._balance -= amount

    def close(self):
        with self._lock:
            if self._status != STATUS_OPEN:
                raise ValueError('Account has been closed or has not been opened')
            self._status = STATUS_CLOSED
