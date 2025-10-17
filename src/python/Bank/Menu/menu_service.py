from dat2011_little_fox28.src.python.Bank.Menu.menu_interface import MenuInterface
from dat2011_little_fox28.src.python.Bank.account import Account
from dat2011_little_fox28.src.python.Bank.account_service import AccountService
from dat2011_little_fox28.src.utils.handle_input_for_number import HandleInputForNumber
from dat2011_little_fox28.src.utils.handle_input_for_string import HandleInputForString

import os
import csv
from datetime import datetime

INPUT_HEADER = ['Nhập số tài khoản:', 'Nhập tên khách hàng:', 'Nhập loại tài khoản:', 'Nhập số dư:']
file_name='taikhoan.csv'


class MenuService(MenuInterface, AccountService):
    def __init__(self):
        super().__init__()

    def create_account(self):
        """Tạo tài khoản mới"""
        try:
            acc_id_input = HandleInputForNumber()
            acc_id_input.handle_input(1, [INPUT_HEADER[0]])
            acc_id = str(int(acc_id_input.getter_x()))

            if self.find_account(acc_id):
                print("Lỗi: Tài khoản đã tồn tại.")
                return

            acc_inf_input = HandleInputForString()
            acc_inf_input.handle_input(2, INPUT_HEADER[1:3])
            user_name = acc_inf_input.getter_x()
            acc_type = acc_inf_input.getter_y().upper()

            balance_input = HandleInputForNumber()
            balance_input.handle_input(1, [INPUT_HEADER[3]])
            account_balance = balance_input.getter_x()

            new_account = Account(acc_id, user_name, acc_type, account_balance)
            self.account_list.append(new_account)
            self._csv_account_writer()
            print("Tạo tài khoản thành công 💥")
            print(new_account.show_account())
        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại")

    def list_account(self):
        """Hiển thị danh sách tài khoản"""
        if not self.account_list:
            print("Chưa có tài khoản nào.")
            return
        for acc in self.account_list:
            print(acc.show_account())

    def edit_account(self):
        """Chỉnh sửa thông tin tài khoản"""
        try:
            acc_id_input = HandleInputForNumber()
            acc_id_input.handle_input(1, ["Nhập số tài khoản cần sửa:"])
            acc_id = str(int(acc_id_input.getter_x()))

            account = self.find_account(acc_id)
            if not account:
                print("Lỗi: Tài khoản không tồn tại.")
                return

            print("Thông tin tài khoản hiện tại:")
            print(account.show_account())

            acc_inf_input = HandleInputForString()
            acc_inf_input.handle_input(2, ["Nhập tên khách hàng mới:", "Nhập loại tài khoản mới (T/C):"])
            new_user_name = acc_inf_input.getter_x()
            new_acc_type = acc_inf_input.getter_y().upper()

            # Create a new account object with updated info and replace the old one
            updated_account = Account(account.acc_id, new_user_name, new_acc_type, account.account_balance)
            # Find the index of the old account and replace it
            for i, acc in enumerate(self.account_list):
                if acc.acc_id == acc_id:
                    self.account_list[i] = updated_account
                    break
            
            self._csv_account_writer()
            print("Cập nhật tài khoản thành công.")
            print(updated_account.show_account())

        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")

    def remove_account(self):
        """Xóa tài khoản"""
        try:
            acc_id_input = HandleInputForNumber()
            acc_id_input.handle_input(1, ["Nhập số tài khoản cần xóa:"])
            acc_id = str(int(acc_id_input.getter_x()))

            account = self.find_account(acc_id)
            if not account:
                print("Lỗi: Tài khoản không tồn tại.")
                return

            self.account_list.remove(account)
            self._csv_account_writer()
            print("Xóa tài khoản thành công.")
        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")

    def find_account_by_username(self):
        """Tìm tài khoản theo tên khách hàng"""
        try:
            name_input = HandleInputForString()
            name_input.handle_input(1, ["Nhập tên khách hàng cần tìm:"])
            user_name = name_input.getter_x()

            found_accounts = [acc for acc in self.account_list if user_name.lower() in acc.user_name.lower()]

            if not found_accounts:
                print("Không tìm thấy tài khoản nào với tên khách hàng này.")
                return

            for acc in found_accounts:
                print(acc.show_account())
        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")

    def account_statement(self):
        """Sao kê tài khoản"""
        try:
            acc_id_input = HandleInputForNumber()
            acc_id_input.handle_input(1, ["Nhập số tài khoản để sao kê:"])
            acc_id = str(int(acc_id_input.getter_x()))

            account = self.find_account(acc_id)
            if not account:
                print("Lỗi: Tài khoản không tồn tại.")
                return
            print("Thông tin tài khoản:")
            print(account.show_account())
        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")

    def deposit_money(self):
        """Gửi tiền vào tài khoản"""
        try:
            acc_id_input = HandleInputForNumber()
            acc_id_input.handle_input(1, ["Nhập số tài khoản để gửi tiền:"])
            acc_id = str(int(acc_id_input.getter_x()))

            account = self.find_account(acc_id)
            if not account:
                print("Lỗi: Tài khoản không tồn tại.")
                return

            amount_input = HandleInputForNumber()
            amount_input.handle_input(1, ["Nhập số tiền cần gửi:"])
            amount = amount_input.getter_x()

            if account.deposit_money(amount):
                self._csv_account_writer()
                print(f"Gửi tiền thành công. Số dư mới: {account.account_balance:,.0f} VNĐ")
        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")
            
    def withdraw_money(self):
        """Rút tiền từ tài khoản"""
        try:
            acc_id_input = HandleInputForNumber()
            acc_id_input.handle_input(1, ["Nhập số tài khoản để rút tiền:"])
            acc_id = str(int(acc_id_input.getter_x()))

            account = self.find_account(acc_id)
            if not account:
                print("Lỗi: Tài khoản không tồn tại.")
                return

            amount_input = HandleInputForNumber()
            amount_input.handle_input(1, ["Nhập số tiền cần rút:"])
            amount = amount_input.getter_x()

            if account.withdrawal_money(amount):
                self._csv_account_writer()
                print(f"Rút tiền thành công. Số dư mới: {account.account_balance:,.0f} VNĐ")
        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")

    def transfer_money(self): # bonus
        """Chuyển tiền giữa 2 tài khoản"""
        try:
            # Get sender account
            sender_id_input = HandleInputForNumber()
            sender_id_input.handle_input(1, ["Nhập số tài khoản người gửi:"])
            sender_id = str(int(sender_id_input.getter_x()))
            sender_account = self.find_account(sender_id)
            if not sender_account:
                print("Lỗi: Tài khoản người gửi không tồn tại.")
                return

            # Get receiver account
            receiver_id_input = HandleInputForNumber()
            receiver_id_input.handle_input(1, ["Nhập số tài khoản người nhận:"])
            receiver_id = str(int(receiver_id_input.getter_x()))
            receiver_account = self.find_account(receiver_id)
            if not receiver_account:
                print("Lỗi: Tài khoản người nhận không tồn tại.")
                return
                
            if sender_id == receiver_id:
                print("Lỗi: Không thể chuyển tiền cho chính mình.")
                return

            # Get amount
            amount_input = HandleInputForNumber()
            amount_input.handle_input(1, ["Nhập số tiền cần chuyển:"])
            amount = amount_input.getter_x()

            if sender_account.withdrawal_money(amount):
                receiver_account.deposit_money(amount)
                self._csv_account_writer()
                print("Chuyển tiền thành công.")
                print(f"Số dư tài khoản người gửi: {sender_account.account_balance:,.0f} VNĐ")
                print(f"Số dư tài khoản người nhận: {receiver_account.account_balance:,.0f} VNĐ")

        except (ValueError, Exception) as e:
            print(f"Lỗi: {e}. Vui lòng thử lại.")


    def check_account_balance(self):
        """Kiểm tra số dư tài khoản"""
        self.account_statement() # Same functionality

    def backup_data(self):
backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'backup')
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            timestamp = datetime.now().strftime("dd/mm/yyyy")
            backup_file_name = f"taikhoan_{timestamp}.csv"
            backup_file_path = os.path.join(backup_dir, backup_file_name)

            with open(backup_file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['acc_id', 'user_name', 'acc_type', 'account_balance'])
                writer.writeheader()
                for account in self.account_list:
                    writer.writerow(account.to_dict())
            
            self._csv_account_writer()
            print(f"Sao lưu dữ liệu thành công vào: {backup_file_path}")
        except Exception as e:
            print(f"Lỗi khi sao lưu: {e}")

    def restore_data(self):
        """Phục hồi dữ liệu từ một file backup."""
        try:
            backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'backup')
            if not os.path.exists(backup_dir) or not os.path.isdir(backup_dir):
                print("Lỗi: Thư mục backup không tồn tại.")
                return

            backup_files = [f for f in os.listdir(backup_dir) if f.endswith('.csv')]

            if not backup_files:
                print("Không tìm thấy file backup nào.")
                return

            print("Chọn một file để phục hồi:")
            for i, file_name in enumerate(backup_files):
                print(f"  {i + 1}: {file_name}")

            choice_input = HandleInputForNumber()
            choice_input.handle_input(1, ["Nhập lựa chọn của bạn (nhập 0 để thoát): "])
            choice = int(choice_input.getter_x())

            if choice == 0:
                print("Hủy phục hồi.")
                return

            if 1 <= choice <= len(backup_files):
                selected_file = os.path.join(backup_dir, backup_files[choice - 1])
                
                new_accounts = []
                with open(selected_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            account = Account(
                                acc_id=row['acc_id'],
                                user_name=row['user_name'],
                                acc_type=row['acc_type'],
                                account_balance=float(row['account_balance'])
                            )
                            new_accounts.append(account)
                        except (ValueError, KeyError) as e:
                            print(f"Cảnh báo: Bỏ qua dòng lỗi trong file backup: {row} -> {e}")
                
                self.account_list = new_accounts
                self._csv_account_writer()
                print(f"Đã phục hồi thành công từ file '{backup_files[choice - 1]}'.")
            else:
                print("Lựa chọn không hợp lệ.")

        except (ValueError, Exception) as e:
            print(f"Đã xảy ra lỗi trong quá trình phục hồi: {e}")