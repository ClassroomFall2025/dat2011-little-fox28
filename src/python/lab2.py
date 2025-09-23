import sys
import os
from typing import Optional, Union
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.utils.handle_input import HandleInput
from src.utils.highlight import highlight_text

NUMERIC = int | float
DEFAULT = ["Nhập x: ", "Nhập y: ", "Nhập z: "]

class FirstDegreeEquation(HandleInput):
    """Solves first-degree equation in the form ax + b = 0"""

    def __init__(self):
        super().__init__()

    def calculation(self) -> float:
        self.handle_input(2, ["Nhập a:", "Nhập b:"])

        a = self.getter_x()
        b = self.getter_y()

        if a == 0:
            if b == 0:
                raise Exception("Phương trình có vô số nghiệm")
            raise Exception("Phương trình vô nghiệm")

        return -b / a

class SquareRootEquation(HandleInput):
    """
    Solves quadratic equations in the form ax² + bx + c = 0
    Handles degenerate cases (a=0) by delegating to FirstDegreeEquation
    """
    def __init__(self):
        super().__init__()
        self._z: Optional[NUMERIC] = None

    def calculation(self) -> Union[tuple[float, float], float, None]:
        """
        Solves the quadratic equation
        Returns:
            tuple[float, float]: Two distinct roots if delta > 0
            float: One root if delta = 0
            None: If equation has no real roots or is degenerate
        """
        self.handle_input(3,["Nhập a: ", "Nhập b: ", "Nhập c: "])
        a = self.getter_x()
        b = self.getter_y()
        c = self.getter_z()

        if a == 0:
            first_degree = FirstDegreeEquation()
            first_degree.setter_x(b)
            first_degree.setter_y(c)
            try:
                return first_degree.calculation()
            except ValueError as e:
                print(highlight_text(str(e)))
                return None
        
        delta = b * b - 4 * a * c
        
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(highlight_text("2 nghiệm phân biệt:"))
            print(f"x₁ = {x1:.4f}")
            print(f"x₂ = {x2:.4f}")
            return x1, x2
        elif delta == 0:
            x = -b / (2 * a)
            print(highlight_text("Nghiệm kép:"))
            print(f"x = {x:.4f}")
            return x
        else:
            print(highlight_text("Vô nghiệm"))
            return None

cal = SquareRootEquation()
print(cal.calculation())