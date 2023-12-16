# KTGK ĐỀ 02
# Câu 3: Viết chương trình tính diện tích tam giác (2.0 điểm)

# Nhập chiều dài của ba cạnh của tam giác
a = float(input("Nhập chiều dài cạnh a: "))
b = float(input("Nhập chiều dài cạnh b: "))
c = float(input("Nhập chiều dài cạnh c: "))

# Tính nửa chu vi
p = (a + b + c) / 2

# Tính diện tích
dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5

# In diện tích
print("Diện tích của tam giác là: ", dien_tich)

# Câu 4: Định nghĩa class Quân nhân với các thuộc tính và phương thức như sau: (3.0 điểm)
from datetime import datetime

class QuanNhan:
    def __init__(self, ma_so, ho_ten, ngay_sinh, ngay_nhap_ngu, gioi_tinh, ngay_vao_dang, don_vi):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
        self.ngay_sinh = datetime.strptime(ngay_sinh, '%d/%m/%Y')
        self.ngay_nhap_ngu = datetime.strptime(ngay_nhap_ngu, '%d/%m/%Y')
        self.gioi_tinh = gioi_tinh
        self.ngay_vao_dang = datetime.strptime(ngay_vao_dang, '%d/%m/%Y')
        self.don_vi = don_vi

    def tinh_tuoi_quan_nhan(self):
        return (datetime.now() - self.ngay_nhap_ngu).days // 365

    def tinh_tuoi_dang(self):
        return (datetime.now() - self.ngay_vao_dang).days // 365

    def xuat_thong_tin(self):
        print(f'Mã số: {self.ma_so}\nHọ tên: {self.ho_ten}\nNgày sinh: {self.ngay_sinh.strftime("%d/%m/%Y")}\nNgày nhập ngũ: {self.ngay_nhap_ngu.strftime("%d/%m/%Y")}\nGiới tính: {self.gioi_tinh}\nNgày vào đảng: {self.ngay_vao_dang.strftime("%d/%m/%Y")}\nĐơn vị: {self.don_vi}\nTuổi quân nhân: {self.tinh_tuoi_quan_nhan()}\nTuổi đảng: {self.tinh_tuoi_dang()}')

quan_nhan1 = QuanNhan(input("Nhập mã số: "), input("Nhập họ tên: "), input("Nhập ngày sinh (dd/mm/yyyy): "), input("Nhập ngày nhập ngũ (dd/mm/yyyy): "), input("Giới tính: "), input("Nhập ngày vào đảng (dd/mm/yyyy): "), input("Đơn vị: "))
quan_nhan2 = QuanNhan(input("Nhập mã số: "), input("Nhập họ tên: "), input("Nhập ngày sinh (dd/mm/yyyy): "), str(input("Giới tính: ")), input("Nhập ngày vào đảng (dd/mm/yyyy): "), input("Nhập ngày nhập ngũ (dd/mm/yyyy): "), str(input("Đơn vị: ")))

print("Thông tin quân nhân 1:")
quan_nhan1.xuat_thong_tin()

print("Thông tin quân nhân 2:")
quan_nhan2.xuat_thong_tin()
