from dat2011_little_fox28.src.utils.handle_input_for_number import HandleInputForNumber
from dat2011_little_fox28.src.utils.handle_input_for_string import HandleInputForString


class Product:
    def __init__(self, product_name: str, price: float, discount_price: float):
        self.__product_name = product_name
        self.__price = price
        self.__discount_price = discount_price

    def calc_import_tax(self) -> float:
        tax = 0.1
        return self.price * tax

    def __str__(self) -> str:
        return (f"Tên sản phẩm: {self.product_name}\n"
                f"Giá: {self.price}\n"
                f"Giá giảm: {self.discount_price}")

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def discount_price(self):
        return self.__discount_price

    @discount_price.setter
    def discount_price(self, value):
        self.__discount_price = value


class HandleProduct:
    def __init__(self):
        self.store = []


    def new_product(self, name, price, discount_price) -> None:
        product = Product(name, price, discount_price)
        self.store.append(product)

    def export_products(self):
        if not self.store:
            return

        for index, product in enumerate(self.store):
            print(f"---Sản phẩm thứ {index + 1}---")
            print(product)
            print(f"Thuế nhập khẩu: {product.calc_import_tax()}")

        return

    def handle_create_product(self):
        while True:
            handle_name = HandleInputForString()
            handle_name.handle_input(1,["Nhập tên sản phẩm(Nhập 'n' để thoát chương trình): "])
            name = handle_name.getter_x()

            if name == "n":
                break

            handle_price = HandleInputForNumber()
            handle_price.handle_input(2, ["Nhập giá sản phẩm: ", "Nhập giá giảm: "])
            price = handle_price.getter_x()
            discount_price = handle_price.getter_y()

            self.new_product(name, price, discount_price)

        print("Cam on vi da den")
