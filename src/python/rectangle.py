from dat2011_little_fox28.src.utils.handle_input_for_number import HandleInputForNumber

class Rectangle(HandleInputForNumber):
    """Đối tượng tính chu vi và diện tích hình chữ nhật"""

    def __init__(self):
        super().__init__()

    def calculation(self) -> None:
        """Tính chu vi và diện tích hình chữ nhật"""
        self.handle_input()
        print(f"Diện tích hình chữ nhật: {self.area()}")
        print(f"Chu vi hình chữ nhật: {self.perimeter()}")

    def area(self) -> float:
        return self.getter_x() * self.getter_y()

    def perimeter(self) -> float:
        return (self.getter_x() + self.getter_y()) * 2