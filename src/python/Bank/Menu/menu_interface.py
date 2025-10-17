from abc import ABC, abstractmethod


class MenuInterface(ABC):

    @abstractmethod
    def list_account(self):
        """Hiển thị danh sách tài khoản"""
        pass

    @abstractmethod
    def create_account(self):
        """Tạo tài khoản mới"""
        pass

    @abstractmethod
    def edit_account(self):
        """Chỉnh sửa thông tin tài khoản"""
        pass

    @abstractmethod
    def remove_account(self):
        """Xóa tài khoản"""
        pass

    @abstractmethod
    def find_account_by_username(self):
        """Tìm tài khoản theo tên người dùng"""
        pass

    @abstractmethod
    def account_statement(self):
        """Sao kê tài khoản"""
        pass

    @abstractmethod
    def deposit_money(self):
        """Gửi tiền vào tài khoản"""
        pass

    @abstractmethod
    def check_account_balance(self):
        """Kiểm tra số dư tài khoản"""
        pass

    @abstractmethod
    def backup_data(self):
        """Sao lưu dữ liệu"""
        pass

    @abstractmethod
    def restore_data(self):
        """Phục hồi dữ liệu"""
        pass
