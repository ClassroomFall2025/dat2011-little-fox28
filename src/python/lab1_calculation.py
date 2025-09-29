import math
from dat2011_little_fox28.src.utils.handle_input_for_number import HandleInput

class Calculation(HandleInput):
    """
        Đối tượng thực hiện các phép toán cơ bản.
        Kiểu dữ liệu hỗ trợ: @int, @float.
    """
    def __init__(self):
        super().__init__()

    # Basic calculation
    def addition(self) -> float:
        return math.fsum([self.getter_x(), self.getter_y()])
    def subtraction(self) -> float:
        return math.fsum([self.getter_x(), -self.getter_y()])
    def multiplication(self) -> float:
        if self.getter_x() == 0 or self.getter_y() == 0:
            return 0
        return math.prod([self.getter_x(), self.getter_y()])
    def division(self) -> float:
        if self.getter_x() == 0:
            return 0
        if self.getter_y() == 0:
            return float('Một số không nên chia cho 0!')
        return math.trunc(self.getter_y() / self.getter_x())
    def division_with_remainder(self) -> float:
        if self.getter_x() == 0:
            return 0
        if self.getter_y() == 0:
            return float('Một số không nên chia cho 0!')
        return math.remainder(self.getter_y(), self.getter_x())
    
    # Advance calculation
    def exponentiation(self) -> float:
        return math.pow(self.getter_x(), self.getter_y())
    def square_root(self) -> float:
        return math.sqrt(self.getter_x())
    
    # Trigonometric functions
    def sine(self) -> float:
        return math.sin(self.getter_x())
    def cosine(self) -> float:
        return math.cos(self.getter_x())
    def tangent(self) -> float:
        return math.tan(self.getter_x())
    
    # Logarithm functions
    def log10(self) -> float:
        return math.log10(self.getter_x())
    def ln(self) -> float:
        return math.log(self.getter_x())
    def log_base(self) -> float:
        return math.log(self.getter_x(), self.getter_y())