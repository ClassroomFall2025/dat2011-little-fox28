import math
import datetime
from typing import Union

from ..utils.handle_input_for_number import HandleInputForNumber
from ..utils.highlight import highlight_text


class Calculation(HandleInputForNumber):
    """
        Đối tượng thực hiện các phép toán cơ bản.
        Kiểu dữ liệu hỗ trợ: @int, @float.
    """
    def __init__(self):
        super().__init__()

    # Basic calcualtion
    def addition(self) -> float:
        x, y = self.getter_x(), self.getter_y()
        return x + y
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
    
    # First Degree Equation
    def first_degree_equation(self) -> float:
        """
            Căn bậc 1
        """
        a = self.getter_x()
        b = self.getter_y()

        if a == 0:
            if b == 0:
                raise Exception("Phương trình có vô số nghiệm")
            raise Exception("Phương trình vô nghiệm")
        
        return -b / a
    
    # Square Root Equation
    def square_root_equation(self) -> Union[tuple[float, float], float, None]:
        """
            Căn bậc 2
        """
        a = self.getter_x()
        b = self.getter_y()
        c = self.getter_z()

        if a is None or b is None or c is None:
            raise ValueError("Các hệ số a, b, và c phải được cung cấp giá trị.")

        if a == 0:
            if b == 0:
                if c == 0:
                    print(highlight_text("Phương trình có vô số nghiệm"))
                    return None
                else:
                    print(highlight_text("Phương trình vô nghiệm"))
                    return None
            else:
                x = -c / b
                print(highlight_text("Phương trình có một nghiệm:"))
                print(f"x = {x:.4f}")
                return x
        
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

class OthersFeature:
    def __init__(self):
        self._log = []

    def get_time(self):
        """
            Lấy thời gian hiện tại
        """
        return datetime.datetime.now().strftime("%d/%m/%Y - %Hh:%Mm:%Ss")

    def history(self, feature_name: str, result: any, inputs: list):
        """
            Lưu lại lịch sử các phép tính
        """
        log_entry = {
            "timestamp": self.get_time(),
            "feature": feature_name,
            "inputs": inputs,
            "result": result
        }
        self._log.append(log_entry)

    def get_history(self):
        """
            Lấy lịch sử các phép tính
        """
        if not self._log:
            return "Lịch sử trống."
        
        history_str = "--- Lịch sử tính toán ---\n"
        for entry in self._log:
            inputs_str = ", ".join(map(str, entry["inputs"]))

            history_str += f"[{entry['timestamp']}] {entry['feature']}"
            if entry['inputs']:
                 history_str += f" với đầu vào ({inputs_str})"
            history_str += f" -> Kết quả: {entry['result']}\n"

        history_str += "--------------------------"
        return history_str
