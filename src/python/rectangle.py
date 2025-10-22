from dat2011_little_fox28.src.utils.handle_input_for_number import HandleInputForNumber

class Rectangle(HandleInputForNumber):
    """Đối tượng tính chu vi và diện tích hình chữ nhật"""

    def __init__(self):
        super().__init__()

    def area(self) -> float:
        return self.getter_x() * self.getter_y()

    def perimeter(self) -> float:
        return (self.getter_x() + self.getter_y()) * 2

    def calculation(self) -> None:
        """Tính chu vi và diện tích hình chữ nhật"""

        self.handle_input(2, ["Nhập chiều dài: ", "Nhập chiều rộng: "])
        print(f"Chiều dài HCN: {self.getter_x()}")
        print(f"Chiều rộng HCN: {self.getter_y()}")
        print(f"Diện tích hình chữ nhật: {self.area()}")
        print(f"Chu vi hình chữ nhật: {self.perimeter()}")
        print("-----------------------------------------")

class Square(HandleInputForNumber):
    """ Đối tượng tính diện tích hình vuông """
    def __init__(self):
        super().__init__()

    def perimeter(self) -> float:
        return self.getter_x() * 4

    def area(self) -> float:
        return self.getter_x() * self.getter_x()

    def calculation(self) -> None:
        self.handle_input(1, ["Nhập cạnh hình vuông: "])
        print(f"Cạnh hình vuông: {self.getter_x()}")
        print(f"Chu vi hình vuông {self.perimeter()}")
        print(f"Diện tích hình vuông {self.area()}")
