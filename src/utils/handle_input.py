NUMERIC = int | float

class MathVarsInput:
    """
        TwoVarsForMath: xử lý đầu vào của 1, 2 hoặc 3 biến cho các phép tính toán học.\n
        Kiểu dữ liệu hỗ trợ: @int, @float
        Cho phép nhập 1, 2 hoặc 3 đối số, trong đó đối số 2 và 3 là tùy chọn.
    """
    def __init__(self):
        self._x: NUMERIC = 1
        self._y: NUMERIC = None
        self._z: NUMERIC = None
        self.retry = 0

    def handle_input(self, n_args: int = 2) -> None:
        """
        Nhập vào 1, 2 hoặc 3 biến số thực dương. n_args: số lượng biến cần nhập (1, 2 hoặc 3)
        """
        if n_args < 1 or n_args > 3:
            raise ValueError("Chỉ hỗ trợ nhập 1, 2 hoặc 3 đối số.")
        while True:
            try:
                values = []
                prompts = ["Nhập x: ", "Nhập y (tùy chọn): ", "Nhập z (tùy chọn): "]
                for i in range(n_args):
                    val = float(input(prompts[i]))
                    if val <= 0:
                        raise ValueError("Giá trị phải là số dương.")
                    values.append(val)
                # Gán giá trị
                self.setterX(values[0])
                if n_args >= 2:
                    self.setterY(values[1])
                else:
                    self._y = None
                if n_args == 3:
                    self.setterZ(values[2])
                else:
                    self._z = None
                break
            except ValueError as e:
                self.retry += 1
                if self.retry >= 3:
                    raise Exception("Người dùng thử quá nhiều lần. Vui lòng chạy lại chương trình")
                print(f"Lỗi: {e} Hãy nhập lại.")

    def getterX(self) -> NUMERIC:
        return self._x

    def getterY(self) -> NUMERIC:
        return self._y

    def getterZ(self) -> NUMERIC:
        return self._z

    def setterX(self, x) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError("x bắt buộc phải là int hoặc float")
        self._x = x

    def setterY(self, y) -> None:
        if y is not None and not isinstance(y, (int, float)):
            raise TypeError("y bắt buộc phải là int hoặc float")
        self._y = y

    def setterZ(self, z) -> None:
        if z is not None and not isinstance(z, (int, float)):
            raise TypeError("z bắt buộc phải là int hoặc float")
        self._z = z