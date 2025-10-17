from dat2011_little_fox28.src.python.Bank.Menu.menu_service import MenuService
from dat2011_little_fox28.src.utils.handle_input_for_number import HandleInputForNumber


class BanKMenu(MenuService):
    def __init__(self):
        super().__init__()
    
    def run(self):
        """Chạy menu chính"""
        while True:
            print("\n--- Menu Quản Lý Tài Khoản Ngân Hàng ---")
            print("1. Tạo tài khoản mới")
            print("2. Hiển thị danh sách tài khoản")
            print("3. Chỉnh sửa thông tin tài khoản")
            print("4. Xóa tài khoản")
            print("5. Tìm tài khoản theo tên")
            print("6. Sao kê tài khoản")
            print("7. Gửi tiền")
            print("8. Rút tiền")
            print("9. Chuyển tiền") #bonus
            print("10. Sao lưu dữ liệu")
            print("11. Phục hồi dữ liệu")
            print("0. Thoát")

            choice_input = HandleInputForNumber()
            try:
                choice_input.handle_input(1, ["Nhập lựa chọn của bạn:"])
                choice = int(choice_input.getter_x())

                if choice == 1:
                    self.create_account()
                elif choice == 2:
                    self.list_account()
                elif choice == 3:
                    self.edit_account()
                elif choice == 4:
                    self.remove_account()
                elif choice == 5:
                    self.find_account_by_username()
                elif choice == 6:
                    self.account_statement()
                elif choice == 7:
                    self.deposit_money()
                elif choice == 8:
                    self.withdraw_money()
                elif choice == 9:
                    self.transfer_money()
                elif choice == 10:
                    self.backup_data()
                elif choice == 11:
                    self.restore_data()
                elif choice == 0:
                    print("Cảm ơn bạn đã sử dụng dịch vụ.")
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            except (ValueError, Exception) as e:
                print(f"Lỗi: {e}. Vui lòng thử lại.")