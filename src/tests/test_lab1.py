import math

import pytest

from src.python.lab1_calculation import Calculation


class TestCalculation:
    def setup_method(self):
        self.calc = Calculation()
        # Gán giá trị mặc định cho x, y
        self.calc.setterX(10)
        self.calc.setterY(2)

    def test_addition(self):
        assert self.calc.addition() == 12

    def test_subtraction(self):
        assert self.calc.subtraction() == 8

    def test_multiplication(self):
        assert self.calc.multiplication() == 20

    def test_division(self):
        assert self.calc.division() == math.trunc(2/10)

    def test_division_with_remainder(self):
        assert self.calc.division_with_remainder() == math.remainder(2, 10)

    def test_exponentiation(self):
        assert self.calc.exponentiation() == math.pow(10, 2)

    def test_square_root(self):
        self.calc.setterX(16)
        assert self.calc.square_root() == 4

    def test_sine(self):
        self.calc.setterX(math.pi/2)
        assert pytest.approx(self.calc.sine(), 0.0001) == 1

    def test_cosine(self):
        self.calc.setterX(0)
        assert pytest.approx(self.calc.cosine(), 0.0001) == 1

    def test_tangent(self):
        self.calc.setterX(0)
        assert pytest.approx(self.calc.tangent(), 0.0001) == 0

    def test_log10(self):
        self.calc.setterX(100)
        assert self.calc.log10() == 2

    def test_ln(self):
        self.calc.setterX(math.e)
        assert pytest.approx(self.calc.ln(), 0.0001) == 1

    def test_log_base(self):
        self.calc.setterX(8)
        self.calc.setterY(2)
        assert self.calc.log_base() == 3
