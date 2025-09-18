import math
from src.utils.handle_input import MathVarsInput

class Calculation(MathVarsInput):
    """
        Đối tượng thực hiện các phép toán cơ bản.
        Kiểu dữ liệu hỗ trợ: @int, @float.
    """
    def __init__(self):
        super().__init__()

    # Basic calculation
    def addition(self) -> float:
        return math.fsum([self.getterX(), self.getterY()])
    def subtraction(self) -> float:
        return math.fsum([self.getterX(), -self.getterY()])
    def multiplication(self) -> float:
        if self.getterX() == 0 or self.getterY() == 0:
            return 0
        return math.prod([self.getterX(), self.getterY()])
    def division(self) -> float:
        if self.getterX() == 0:
            return 0
        if self.getterY() == 0:
            return float('Một số không nên chia cho 0!')
        return math.trunc(self.getterY() / self.getterX())
    def division_with_remainder(self) -> float:
        if self.getterX() == 0:
            return 0
        if self.getterY() == 0:
            return float('Một số không nên chia cho 0!')
        return math.remainder(self.getterY(), self.getterX())
    
    # Advance calculation
    def exponentiation(self) -> float:
        return math.pow(self.getterX(), self.getterY())
    def square_root(self) -> float:
        return math.sqrt(self.getterX())
    
    # Trigonometric functions
    def sine(self) -> float:
        return math.sin(self.getterX())
    def cosine(self) -> float:
        return math.cos(self.getterX())
    def tangent(self) -> float:
        return math.tan(self.getterX())
    
    # Logarithm functions
    def log10(self) -> float:
        return math.log10(self.getterX())
    def ln(self) -> float:
        return math.log(self.getterX())
    def log_base(self) -> float:
        return math.log(self.getterX(), self.getterY())