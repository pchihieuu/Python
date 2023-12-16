# KTGK ĐỀ 1:

# Câu 1: Viết chương trình Python để di chuyển tất cả các chữ số 0 đến cuối danh sách các số đã cho. (2,0 điểm)

def  move_zero_number(nums):
    zero = [i for i in nums if i == 0]
    non_zeros = [i for i in nums if i != 0]

    result_zero_number = non_zeros + zero
    return result_zero_number
    # Nhập danh sách từ người dùng
input_string = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
nums = [int(num) for num in input_string.split(",")]
# In ra ket qua
print("Ket qua: ", move_zero_number(nums))

# Câu 2: Viết chương trình tạo file văn bản (thongtin_tenban.txt) có nội dung bao gồm các
# thông tin cá nhân bạn như MSSV, Họ tên, Tuổi, ngày/tháng/năm sinh, lớp ban đầu. Dữ liệu
# nhập từ bàn phím. Sau đó sửa tên file. (3,0 điểm)

import os

# Nhập thông tin cá nhân
mssv = input("Nhập MSSV: ")
ho_ten = input("Nhập họ tên: ")
tuoi = input("Nhập tuổi: ")
ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
lop = input("Nhập lớp: ")

# Tạo tên file
ten_file = "thongtin_" + ho_ten.replace(" ", "_") + ".txt"

# Mở file để ghi với mã hóa 'utf-8'
with open(ten_file, 'w', encoding='utf-8') as f:
    f.write("MSSV: " + mssv + "\n")
    f.write("Họ tên: " + ho_ten + "\n")
    f.write("Tuổi: " + tuoi + "\n")
    f.write("Ngày sinh: " + ngay_sinh + "\n")
    f.write("Lớp: " + lop + "\n")

print("Đã tạo file", ten_file)

# Sửa tên file
ten_file_moi = input("Nhập tên file mới: ")
os.rename(ten_file, ten_file_moi)
print("Đã đổi tên file thành", ten_file_moi)
#MỞ RỘNG: ĐỌC FILE
# Nhập tên file cần đọc
ten_file = input("Nhập tên file cần đọc: ")

# Mở file để đọc nội dung với mã hóa 'utf-8'
with open(ten_file, 'r', encoding='utf-8') as f:
    noi_dung = f.read()

# In nội dung của file
print("Nội dung của file", ten_file, "là:")
print(noi_dung)

# Câu 3: Viết chương trình tính chu vi, diện tích hình chữ nhật (2.0 điểm)
chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng"))
chu_vi = ((chieu_dai + chieu_rong) * 2)
dien_tich = (chieu_dai * chieu_rong)

print("Chu vi hình chữ nhật: ", chu_vi)
print("Diện tích hình chữ nhật: ", dien_tich)

# Câu 4: Định nghĩa class Nhanvien với các thuộc tính và phương thức như sau: (3.0 điểm)
from datetime import datetime

class NhanVien:
    def __init__(self, ma_so, ho_ten, ngay_sinh, ngay_vao_lam, phong_ban, muc_luong):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
        self.ngay_sinh = datetime.strptime(ngay_sinh, '%d/%m/%Y')
        self.ngay_vao_lam = datetime.strptime(ngay_vao_lam, '%d/%m/%Y')
        self.phong_ban = phong_ban
        self.muc_luong = muc_luong
     # Các phương thức set
    def set_ma_so(self, ma_so):
        self.ma_so = ma_so

    def set_ho_ten(self, ho_ten):
        self.ho_ten = ho_ten

    def set_ngay_sinh(self, ngay_sinh):
        self.ngay_sinh = datetime.strptime(ngay_sinh, '%d/%m/%Y')

    def set_ngay_vao_lam(self, ngay_vao_lam):
        self.ngay_vao_lam = datetime.strptime(ngay_vao_lam, '%d/%m/%Y')

    def set_phong_ban(self, phong_ban):
        self.phong_ban = phong_ban

    def set_muc_luong(self, muc_luong):
        self.muc_luong = muc_luong

    def tinh_tuoi(self, ngay):
        return datetime.now().year - ngay.year

    def tinh_phu_cap(self):
        so_nam_cong_tac = self.tinh_tuoi(self.ngay_vao_lam)
        return so_nam_cong_tac * 0.02 * self.muc_luong

    def xuat_thong_tin(self):
        print(f"Mã số: {self.ma_so}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngày sinh: {self.ngay_sinh.strftime('%d/%m/%Y')}")
        print(f"Ngày vào làm: {self.ngay_vao_lam.strftime('%d/%m/%Y')}")
        print(f"Phòng ban: {self.phong_ban}")
        print(f"Mức lương: {self.muc_luong}")
        print(f"Tuổi: {self.tinh_tuoi(self.ngay_sinh)}")
        print(f"Phụ cấp thâm niên: {self.tinh_phu_cap()}")

nhan_vien1 = NhanVien(input("Nhập mã số: "), input("Nhập họ tên: "), input("Nhập ngày sinh (dd/mm/yyyy): "), input("Nhập ngày vào làm (dd/mm/yyyy): "), input("Nhập phòng ban: "), float(input("Nhập mức lương: ")))
nhan_vien2 = NhanVien(input("Nhập mã số: "), input("Nhập họ tên: "), input("Nhập ngày sinh (dd/mm/yyyy): "), input("Nhập ngày vào làm (dd/mm/yyyy): "), input("Nhập phòng ban: "), float(input("Nhập mức lương: ")))
nhan_vien3 = NhanVien(input("Nhập mã số: "), input("Nhập họ tên: "), input("Nhập ngày sinh (dd/mm/yyyy): "), input("Nhập ngày vào làm (dd/mm/yyyy): "), input("Nhập phòng ban: "), float(input("Nhập mức lương: ")))

print("Thông tin nhân viên 1:")
nhan_vien1.xuat_thong_tin()

print("Thông tin nhân viên 2:")
nhan_vien2.xuat_thong_tin()

print("Thông tin nhân viên 3:")
nhan_vien3.xuat_thong_tin()




