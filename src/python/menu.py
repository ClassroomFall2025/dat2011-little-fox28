from dat2011_little_fox28.src.utils.highlight import highlight_text, highlight_warning
from .calculation import Calculation, OthersFeature


def display_menu(options: dict) -> None:
    """
        Giao diện menu
    """
    print(highlight_text("--- Calculator Menu 🦊 ---"))
    for key, value in options.items():
        print(f"{key}. {value['text']}")
    print("0. Exit")
    print(highlight_text("-----------------------"))


def menu() -> None:
    """
    Máy tính bỏ túi
    """
    calc = Calculation()
    others_feature = OthersFeature()

    menu_options = {
        "1": {"text": "Phép cộng", "method": calc.addition, "inputs": 2},
        "2": {"text": "Phép trừ", "method": calc.subtraction, "inputs": 2},
        "3": {"text": "Phép nhân", "method": calc.multiplication, "inputs": 2},
        "4": {"text": "Phép chia", "method": calc.division, "inputs": 2},
        "5": {"text": "Phép chia lấy số dư", "method": calc.division_with_remainder, "inputs": 2},
        "6": {"text": "Lũy thừa / số mũ (x^y)", "method": calc.exponentiation, "inputs": 2},
        "7": {"text": "Căn bậc hai", "method": calc.square_root, "inputs": 1},
        "8": {"text": "Sine", "method": calc.sine, "inputs": 1},
        "9": {"text": "Cosine", "method": calc.cosine, "inputs": 1},
        "10": {"text": "Tangent", "method": calc.tangent, "inputs": 1},
        "11": {"text": "Log base 10", "method": calc.log10, "inputs": 1},
        "12": {"text": "Natural Log (ln)", "method": calc.ln, "inputs": 1},
        "13": {"text": "Log với cơ số", "method": calc.log_base, "inputs": 2, "prompts": ["Nhập x (số): ", "Nhập y (cơ số): "]},
        "14": {"text": "Phương trình bậc 1 (ax + b = 0)", "method": calc.first_degree_equation, "inputs": 2, "prompts": ["Nhập a: ", "Nhập b: "]},
        "15": {"text": "Phương trình bậc hai (ax^2 + bx + c = 0)", "method": calc.square_root_equation, "inputs": 3, "prompts": ["Nhập a: ", "Nhập b: ", "Nhập c: "]},
        "16": {"text": "Thời gian hiện tại", "method": others_feature.get_time},
        "17": {"text": "Xem lịch sử", "method": others_feature.get_history},
    }

    while True:
        display_menu(menu_options)
        choice = input("Nhập số để chọn phép tính: ")

        if choice == "0":
            print("Thoát...")
            break

        if choice in menu_options:
            option = menu_options[choice]
            try:
                num_inputs = option.get("inputs")
                method = option.get("method")

                inputs_for_history = []
                if num_inputs is not None and num_inputs > 0:
                    prompts = option.get("prompts", ["Nhập x: ", "Nhập y: ", "Nhập z: "])
                    calc.handle_input(num_inputs, prompts)
                    if num_inputs >= 1:
                        inputs_for_history.append(calc.getter_x())
                    if num_inputs >= 2:
                        inputs_for_history.append(calc.getter_y())
                    if num_inputs >= 3:
                        inputs_for_history.append(calc.getter_z())

                result = method()
                print(highlight_warning(f"Kết quả: {result}"))

                # Lưu lịch sử
                if choice != str(len(menu_options)):
                    others_feature.history(option.get("text"), result, inputs_for_history)

            except Exception as e:
                print(f"Lỗi: {e}")
        else:
            print(f"Chọn các số từ 0 - {len(menu_options)}")

if __name__ == "__main__":
    menu()