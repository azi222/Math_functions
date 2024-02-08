#Temperatur Converter
class Converter:
    @staticmethod
    def temperetura_farangeyta(temperatura):
        return (temperatura * 9 / 5) + 32

    @staticmethod
    def temperetura_celsiya(temperatura):
        return (temperatura - 32) * 5 / 9

#Distance function
class KMetrConverter:
    @staticmethod
    def distance_km(S):
        return round(S * 1.60934, 4)

    @staticmethod
    def distance_m(S):
        return round(S * 0.621371, 4)

#Volume function
class Volume:
    @staticmethod
    def volume_g(v):
        return round(v * 0.264172, 4)

    @staticmethod
    def volume_l(v):
        return round(v * 3.78541, 4)
#fraction calculator
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        if self.numerator == self.denominator:
            Fr = 1
        else:
            Fr = f"{self.numerator}/{self.denominator}"
        print(Fr)

    def sum_fr(self, adder_fraction):
        new_numerator = self.numerator * adder_fraction.denominator + adder_fraction.numerator * self.denominator
        new_denominator = self.denominator * adder_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def sub_fr(self, adder_fraction):
        new_numerator = self.numerator * adder_fraction.denominator - adder_fraction.numerator * self.denominator
        new_denominator = self.denominator * adder_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def mul_fr(self, adder_fraction):
        new_numerator = self.numerator * adder_fraction.numerator
        new_denominator = self.denominator * adder_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def del_fr(self, adder_fraction):
        new_numerator = self.numerator * adder_fraction.denominator
        new_denominator = self.denominator * adder_fraction.numerator
        return Fraction(new_numerator, new_denominator)
