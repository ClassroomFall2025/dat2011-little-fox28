VALID_ACC_TYPES = ("T", "C") # T: Tiết kiệm, C: Cá nhân

class Account:
    def __init__(self, acc_id, user_name, acc_type, account_balance):
        if acc_type not in VALID_ACC_TYPES:
            raise ValueError(f"Loại tài khoản không hợp lệ: '{acc_type}'. Chỉ chấp nhận {VALID_ACC_TYPES}.")

        self.__acc_id = acc_id
        self.__user_name = user_name
        self.__acc_type = acc_type
        self.__account_balance = account_balance

    def to_dict(self):
        return {
            "acc_id": self.__acc_id,
            "user_name": self.__user_name,
            "acc_type": self.__acc_type,
            "account_balance": self.__account_balance
        }

    def show_account(self):
        """Thông tin tài khoản"""
        acc_type_str = "Tiết kiệm" if self.__acc_type == "T" else "Cá nhân"
        return {
            "Số tài khoản": self.__acc_id,
            "Tên khách hàng": self.__user_name,
            "Loại tài khoản": acc_type_str,
            "Số dư": f"{self.__account_balance},0.f VNĐ"
        }

    def withdrawal_money(self, withdrawal) -> bool:
        """Rút tiền"""
        if withdrawal <= 0:
            ValueError("Số tiền rút phải lớn hơn 0.")
            return False
        if self.__account_balance < withdrawal:
            print(f"Lỗi: Số dư không đủ để thực hiện giao dịch. (Số dư: {self.__account_balance:,.0f} VNĐ)")
            return False
        self.__account_balance -= withdrawal
        return True

    def deposit_money(self, deposit) -> bool:
        """Gửi tiền"""
        if deposit <= 0:
            ValueError("Số tiền gửi phải lớn hơn 0.")
            return False
        self.__account_balance += deposit
        return True

    @property
    def acc_id(self):
        return self.__acc_id

    @property
    def user_name(self):
        return self.__user_name

    @property
    def acc_type(self):
        return self.__acc_type

    @property
    def account_balance(self):
        return self.__account_balance