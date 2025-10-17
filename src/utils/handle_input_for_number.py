NUMERIC = int | float
DEFAULT = ["Nhập x: ", "Nhập y: ", "Nhập z: "]

class HandleInputForNumber:
    """
    HandleInputForNumber: xử lý đầu vào của 1, 2 hoặc 3 biến số.\n
    Kiểu dữ liệu hỗ trợ: @int, @float
    Cho phép nhập 1, 2 hoặc 3 đối số, trong đó đối số 2 và 3 là tùy chọn.
    """
    def __init__(self):
        self._x: NUMERIC = 1
        self._y: NUMERIC = None
        self._z: NUMERIC = None
        self.retry = 0

    def validate_input(self, value) -> bool:
        return isinstance(value, (int, float))

    def convert_input(self, value: str) -> NUMERIC:
        return float(value)


    def handle_input(self, n_inputs: int = 2, prompts: list[str] = DEFAULT) -> None:
        """
        Nhập vào 1, 2 hoặc 3 biến số thực dương. n_inputs: số lượng biến cần nhập (1, 2 hoặc 3)
        """

        if n_inputs < 1 or n_inputs > 3:
            raise ValueError("Chỉ hỗ trợ nhập 1, 2 hoặc 3 đối số.")
        while True:
            try:
                values = []
                # prompts = ["Nhập x: ", "Nhập y (tùy chọn): ", "Nhập z (tùy chọn): "]
                for i in range(n_inputs):
                    val = float(input(prompts[i]))
                    values.append(val)
                # Gán giá trị
                self.setter_x(values[0])
                if n_inputs >= 2:
                    self.setter_y(values[1])
                else:
                    self._y = None
                if n_inputs == 3:
                    self.setter_z(values[2])
                else:
                    self._z = None
                break
            except ValueError as e:
                self.retry += 1
                if self.retry >= 3:
                    raise Exception("Người dùng thử quá nhiều lần. Vui lòng chạy lại chương trình")
                print(f"Lỗi: {e} Hãy nhập lại.")

    def getter_x(self) -> NUMERIC:
        return self._x

    def getter_y(self) -> NUMERIC:
        return self._y

    def getter_z(self) -> NUMERIC:
        return self._z

    def setter_x(self, x) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError("x bắt buộc phải là int hoặc float")
        self._x = x

    def setter_y(self, y) -> None:
        if y is not None and not isinstance(y, (int, float)):
            raise TypeError("y bắt buộc phải là int hoặc float")
        self._y = y

    def setter_z(self, z) -> None:
        if z is not None and not isinstance(z, (int, float)):
            raise TypeError("z bắt buộc phải là int hoặc float")
        self._z = z