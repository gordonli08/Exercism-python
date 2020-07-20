from __future__ import division

def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

class Rational:
    def __init__(self, numer, denom):
        _gcd = gcd(numer,denom)
        self.numer = numer/_gcd
        self.denom = denom/_gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            (self.numer * other.denom) + (other.numer * self.denom),
            self.denom * other.denom
        )

    def __sub__(self, other):
        return Rational(
            (self.numer * other.denom) - (other.numer * self.denom),
            self.denom * other.denom
        )

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        return Rational(
            self.numer * other.denom,
            other.numer * self.denom
        )

    def __abs__(self):
        return Rational(
            abs(self.numer),
            abs(self.denom)
        )

    def __pow__(self, power):
        if power > 0:
            return Rational(
                self.numer ** power,
                self.denom ** power
            )
        elif power == 0:
            return Rational(1,1)
        else:
            return Rational(
                self.denom ** abs(power),
                self.numer ** abs(power)
            )

    def __rpow__(self, base):
        return pow(base ** self.numer, 1/self.denom)

