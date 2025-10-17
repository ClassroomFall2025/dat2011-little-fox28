from abc import ABC, abstractmethod

class SinhVienFPoly(ABC):
    """
    Lớp cơ sở trừu tượng cho tất cả sinh viên FPoly.
    Định nghĩa các thuộc tính và phương thức chung.
    """

    def __init__(self, full_name: str, major: str):
        self._full_name = full_name
        self._major = major

    @property
    def full_name(self):
        return self._full_name

    @property
    def major(self):
        return self._major

    @abstractmethod
    def get_score(self) -> float:
        pass

    def get_grade(self) -> str:
        score = self.get_score()
        if score < 5:
            return "Yếu"
        if 5 <= score < 7:
            return "Trung bình"
        if 7 <= score < 8:
            return "Khá"
        if 8 <= score < 9:
            return "Giỏi"
        return "Xuất sắc"

    def export(self) -> dict:
        return {
            "Họ và tên": self.full_name,
            "Ngành": self.major,
            "Điểm TB": round(self.get_score(), 2),
            "Học lực": self.get_grade()
        }


class SinhVienIT(SinhVienFPoly):
    def __init__(self, full_name: str, major: str, java_score: float, html_score: float, css_score: float):
        super().__init__(full_name, major)
        self.java_score = java_score
        self.html_score = html_score
        self.css_score = css_score

    def get_score(self) -> float:
        return (2 * self.java_score + self.html_score + self.css_score) / 4

    def export(self) -> dict:

        data = super().export()
        data.update({
            "Điểm Java": self.java_score,
            "Điểm HTML": self.html_score,
            "Điểm Css": self.css_score,
        })
        return data


class SinhVienBiz(SinhVienFPoly):
    def __init__(self, full_name: str, major: str, marketing_score: float, sales_score: float):
        super().__init__(full_name, major)
        self.marketing_score = marketing_score
        self.sales_score = sales_score

    def get_score(self) -> float:
        return (2 * self.marketing_score + self.sales_score) / 3

    def export(self) -> dict:
        data = super().export()
        data.update({
            "Điểm Marketing": self.marketing_score,
            "Điểm Sales": self.sales_score,
        })
        return data


class HandleStudent:
    IT_MAJORS = {"IT", "Data", "Web", "Mobile", "System"}
    BIZ_MAJORS = {"Marketing", "Sales"}

    def __init__(self):
        self.students: list[SinhVienFPoly] = []

    def add_student(self):
        print("\n--- Thêm sinh viên mới ---")
        full_name = input("Nhập họ và tên: ")
        major = input("Nhập ngành: ")

        student_object = None
        if major in self.IT_MAJORS:
            java_score = float(input("Nhập điểm Java: "))
            html_score = float(input("Nhập điểm HTML: "))
            css_score = float(input("Nhập điểm Css: "))
            student_object = SinhVienIT(full_name, major, java_score, html_score, css_score)

        elif major in self.BIZ_MAJORS:
            marketing_score = float(input("Nhập điểm Marketing: "))
            sales_score = float(input("Nhập điểm Sales: "))
            student_object = SinhVienBiz(full_name, major, marketing_score, sales_score)
        else:
            print(f"Ngành '{major}' không hợp lệ.")
            return

        self.students.append(student_object)
        print(f"Đã thêm sinh viên: {full_name}")

    def export_student_list(self):
        if not self.students:
            print("Danh sách sinh viên trống.")
            return

        print("\n--- Danh sách sinh viên ---")
        for i, student in enumerate(self.students, 1):
            print(f"Sinh viên #{i}:")
            for key, value in student.export().items():
                print(f"  - {key}: {value}")
            print("-" * 20)

    def filter_students_by_grade(self, grade: str) -> list[SinhVienFPoly]:
        filtered_list = [
            student for student in self.students if student.get_grade().lower() == grade.lower()
        ]
        return filtered_list

    def sort_students_by_score(self, reverse: bool = True):
        self.students.sort(key=lambda student: student.get_score(), reverse=reverse)
        print("\nĐã sắp xếp danh sách sinh viên theo điểm số giảm dần.")