# ĐỀ KTGK 04

# Câu 1: Viết chương trình in list từ list [12, 16, 24, 35, 24, 266, 88, 120, 16, 155, 88, 120, 155,
# 266], sau khi đã xóa hết các giá trị trùng nhau. Tìm phần tử lớn nhất và nhỏ nhất trong list
# mới. (3,0 điểm)

# Khởi tạo list ban đầu
lst = [12, 16, 24, 35, 24, 266, 88, 120, 16, 155, 88, 120, 155, 266]

# Xóa các giá trị trùng nhau bằng cách chuyển list thành set
lst = list(set(lst))

# In list mới
print("List sau khi xóa các giá trị trùng nhau:", lst)

# Tìm phần tử lớn nhất và nhỏ nhất
print("Phần tử lớn nhất trong list:", max(lst))
print("Phần tử nhỏ nhất trong list:", min(lst))

# Câu 2: Viết chương trình nhập: số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn, từ
# đó tính ra số tiền thực lĩnh của nhân viên. Biết rằng: số giờ tiêu chuẩn mỗi tuần là 44 giờ, và
# mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn. (2,0 điểm)

# Nhập số giờ làm mỗi tuần và thù lao trên mỗi giờ làm tiêu chuẩn
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
thu_lao_tieu_chuan = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

# Số giờ tiêu chuẩn mỗi tuần
so_gio_tieu_chuan = 44

# Tính số tiền thực lĩnh
if so_gio_lam <= so_gio_tieu_chuan:
    tien_thuc_linh = so_gio_lam * thu_lao_tieu_chuan
else:
    tien_thuc_linh = so_gio_tieu_chuan * thu_lao_tieu_chuan + (so_gio_lam - so_gio_tieu_chuan) * thu_lao_tieu_chuan * 1.5

print("Số tiền thực lĩnh của nhân viên là:", tien_thuc_linh)


# Câu 3: Viết chương trình tính diện tích tam giác (dùng hàm) (2.0 điểm)

def tinh_dien_tich_tam_giac(canha, canhb, canhc):
    # Tính nửa chu vi
    p = (canha + canhb + canhc) / 2

    # Tính diện tích theo công thức Heron
    dientich = (p * (p - canha) * (p - canhb) * (p - canhc)) ** 0.5

    return dientich

# Nhập độ dài 3 cạnh của tam giác
canha = float(input("Nhập độ dài cạnh a: "))
canhb = float(input("Nhập độ dài cạnh b: "))
canhc = float(input("Nhập độ dài cạnh c: "))

# Tính diện tích tam giác
dientich = tinh_dien_tich_tam_giac(canha, canhb, canhc)

print("Diện tích tam giác là:", dientich)


# Câu 4: Định nghĩa một class có tên là Shape và class con là Square. Square có hàm init để lấy
# đối số là chiều dài. Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của
# Shape là 0. (3.0 điểm)

class Shape:
    def __init__(self):
        self.area = 0

    def calculate_area(self):
        print(f"Diện tích của hình là: {self.area}")


class Square(Shape):
    def __init__(self, side_length):
        super().__init__()  # Gọi hàm init của lớp cha để khởi tạo diện tích mặc định
        self.side_length = side_length
        # self.calculate_area()  # Tính diện tích của hình vuông ngay từ khi khởi tạo

    def calculate_area(self):
        self.area = self.side_length ** 2  # Diện tích của hình vuông là bình phương chiều dài cạnh
        print(f"Diện tích của hình vuông là: {self.area}")


# Sử dụng các class đã định nghĩa
shape = Shape()
shape.calculate_area()  # In diện tích mặc định của hình Shape

square = Square(4)  # Khởi tạo một hình vuông có chiều dài cạnh là 4
square.calculate_area()  # In diện tích của hình vuông

