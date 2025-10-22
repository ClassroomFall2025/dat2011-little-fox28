DEFAULT = ["Nhập x: ", "Nhập y: ", "Nhập z: "]
class HandleInputForString:

    def __init__(self):
        self._x: str = ""
        self._y: str = None
        self._z: str = None
        self.retry = 0

    def setter_x(self, x: str) -> None:
        if not isinstance(x, str) or not x.strip():
            raise ValueError("x must be a non-empty string")
        self._x = x.strip()

    def getter_x(self) -> str:
        return self._x

    def setter_y(self, y: str) -> None:
        if y is not None and (not isinstance(y, str) or not y.strip()):
            raise ValueError("y must be a non-empty string")
        self._y = y.strip() if y is not None else None

    def getter_y(self) -> str:
        return self._y

    def setter_z(self, z: str) -> None:
        if z is not None and (not isinstance(z, str) or not z.strip()):
            raise ValueError("z must be a non-empty string")
        self._z = z.strip() if z is not None else None

    def getter_z(self) -> str:
        return self._z

    def handle_input(self, n_inputs: int = 2, prompts: list[str] = DEFAULT) -> None:
        if n_inputs < 1 or n_inputs > 3:
            raise ValueError("Chỉ hỗ trợ nhập 1, 2 hoặc 3 đối số.")

        while True:
            try:
                values = []
                for i in range(n_inputs):
                    val = input(prompts[i])
                    if not val.strip():
                        raise ValueError("Chuỗi không được rỗng")
                    values.append(val)

                self.setter_x(values[0])
                if n_inputs >= 2:
                    self.setter_y(values[1])
                if n_inputs == 3:
                    self.setter_z(values[2])
                break

            except ValueError as e:
                self.retry += 1
                if self.retry >= 3:
                    raise Exception("Người dùng thử quá nhiều lần. Vui lòng chạy lại chương trình")
                print(f"Lỗi: {e} Hãy nhập lại.")