import csv
import os
from dat2011_little_fox28.src.python.Bank.account import Account

CSV_HEADERS = ['acc_id', 'user_name', 'acc_type', 'account_balance']
ACCOUNT_HEADER = ['Số tài khoản', 'Tên khách hàng', 'Loại tài khoản', 'Số dư']
file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'taikhoan.csv')

def map_csv_to_account_header():
    return dict(zip(CSV_HEADERS, ACCOUNT_HEADER))

class AccountService:
    def __init__(self):
        self.file_name = file_name
        self.account_list = self._csv_account_reader()

    def find_account(self, id):
        """Tìm tài khoản dựa tên số tài khoản"""
        for account in self.account_list:
            if account.acc_id == id:
                return account
        return None

    def _csv_account_writer(self):
        """Ghi toàn bộ danh sách tài khoản hiện tại vào file CSV."""
        try:
            with open(self.file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
                writer.writeheader()
                for account in self.account_list:
                    writer.writerow(account.to_dict())
        except IOError as e:
            print(f"Lỗi nghiêm trọng khi ghi file: {e}")


    def _csv_account_reader(self):
        """Đọc danh sách tài khoản từ file CSV."""
        accounts = []
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        account = Account(
                            acc_id=row['acc_id'],
                            user_name=row['user_name'],
                            acc_type=row['acc_type'],
                            account_balance=float(row['account_balance'])
                        )
                        accounts.append(account)
                    except (ValueError, KeyError) as e:
                        print(f"Cảnh báo: Bỏ qua dòng lỗi trong CSV: {row} -> {e}")
        except FileNotFoundError:
            pass
        return accounts