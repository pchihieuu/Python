# Cau2: vè list, tuple, dict, set.
#2.1 tìm max, min trong tuple1
tuple1 = ('a', 2, 'c', 4, 6, 8)
tuple2 = ('d', 1,'e',3,5,7,9)
# sử dụng list comprehension, tạo một list mới bằng cách thực hiện một biểu thức trên mỗi phần tử của iterable.
# sau đó lọc ra các phần tử của tuple_example mà là số nguyên (int).
max_value = max([i for i in tuple1 if isinstance(i, int)])
min_value = min([i for i in tuple1 if isinstance(i, int)])
print("Max value: ", max_value)
print("Min value:", min_value)
# 2.2 Nghịch đảo tuple2
reversed_tuple2 = tuple2[::-1]
print("Tuple2 sau khi đảo ngược:", reversed_tuple2)
# 2.3 Tạo tuple3 bằng cách nối tuple1 và tuple2
tuple3 = tuple1 + tuple2
print("Tuple3 sau khi nối:", tuple3)
# 2.4 Tìm giá trị ở tuple2 với index = 5
value_at_index = tuple2[5]
print("Giá trị ở index 5 của tuple2:", value_at_index)

# Cau 3: hàm
def perimeter(a, b, c):
    #Tính chu vi tam giác cân.
    return a + b + c

def acreage(a, b):
    #Tính diện tích tam giác cân."""
    return 0.5 * a * b

# Nhập chiều dài cạnh đáy và chiều cao từ người dùng
canh_day = float(input("Nhập chiều dài cạnh đáy của tam giác cân: "))
chieu_cao = float(input("Nhập chiều cao của tam giác cân: "))

# Xác định chiều dài cạnh bằng cách chia đôi chiều dài cạnh đáy (tam giác cân)
canh_a = canh_day / 2
canh_b = canh_day / 2
canh_c = chieu_cao

# In kết quả
print(f"Chu vi của tam giác cân là: {perimeter(canh_a, canh_b, canh_c)}")
print(f"Diện tích của tam giác cân là: {acreage(canh_day, chieu_cao)}")

# Cau 3.02:
# Hàm giải phương trình bậc 1
def giai_pt_bac_1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Nghiệm của phương trình là x = {x}"
if __name__=="__main__":
# Nhập hệ số a và b từ người dùng
  a = float(input("Nhập hệ số a: "))
  b = float(input("Nhập hệ số b: "))
# In kết quả
print(f"Kết quả của phương trình bậc nhất là: {giai_pt_bac_1(a, b)}")

# Cau 1: Class, kế thừa.
# So.01: Gán values trực tiếp
class Car:
    def __init__(self, open):
        self.open = open

    def open(self):
        self.open = True

    def close(self):
        self.open = False

    def xuatCar(self):
        if self.open:
            return("Cửa Mở")
        else:
            return("Cửa Đóng")


class MotoCycle:
    def __init__(self, stand_out):
        self.stand_out = stand_out

    def xuatMoto(self):
        if self.stand_out:
            return ("Đứng được")
        else:
            return ("Không đứng được")

class Vehicle(Car, MotoCycle):
    def __init__(self, started, speed, open, stand_out):
        Car.__init__(self, open)
        MotoCycle.__init__(self, stand_out)
        self.started = started
        self.speed = speed
    def start(self):
        if self.started:
            return ("Di chuyển")
        else:
            return ("Dừng lại")
    def speed(self):
        self.speed
    def xuattt(self):
        print("Thông tin xe:")
        print("Trạng thái chạy của xe:", self.start())
        print(f"Tốc độ: {self.speed}km ")
        print("Trạng thái cửa xe:", self.xuatCar())
        print("Trạng thái chân đứng của xe máy:", self.xuatMoto())

    def nhap_tt(self):
        started_input = input("Nhập trạng thái (Có/Không) có đang chạy không: ")
        self.started = bool(started_input.lower() == "true")

        speed_input = input("Nhập tốc độ: ")
        self.speed = int(speed_input)
        # Using conditional expression, ternary operator, khong phan biet chu hoa
        car_open_input = input("Nhập trạng thái của cửa xe (Có/Không có mở không): ")
        self.open_door() if car_open_input.lower() == "true" else self.close_door()

        moto_stand_out_input = input("Nhập trạng thái chân đứng của xe máy (Có/Không có đứng không): ")
        self.stand_out = bool(moto_stand_out_input.lower() == "true")


x = Vehicle(True, 2000, False, True)
x.xuattt()

# So.02: Nhập dữ liệu từ người dùng.
class Car:
    def __init__(self, open):
        self.open = open

    def open(self):
        self.open = True

    def close(self):
        self.open = False

    def xuatCar(self):
        if self.open:
            return("Cửa Mở")
        else:
            return("Cửa Đóng")


class MotoCycle:
    def __init__(self, stand_out):
        self.stand_out = stand_out

    def xuatMoto(self):
        if self.stand_out:
            return ("Đứng được")
        else:
            return ("Không đứng được")

class Vehicle(Car, MotoCycle):
    def __init__(self):
        Car.__init__(self, False)
        MotoCycle.__init__(self, False)
        self.started = False
        self.speed = 0
    def start(self):
        if self.started:
            return ("Di chuyển")
        else:
            return ("Dừng lại")
    def speed(self):
        self.speed
    def xuattt(self):
        print("Thông tin xe:")
        print("Trạng thái chạy của xe:", self.start())
        print(f"Tốc độ: {self.speed}km ")
        print("Trạng thái cửa xe:", self.xuatCar())
        print("Trạng thái chân đứng của xe máy:", self.xuatMoto())

    def nhap_tt(self):
        started_input = input("Nhập trạng thái (Có/Không) có đang chạy không: ")
        self.started = bool(started_input.lower() == "true")

        speed_input = input("Nhập tốc độ: ")
        self.speed = int(speed_input)
        # Using conditional expression, ternary operator, khong phan biet chu hoa
        car_open_input = input("Nhập trạng thái của cửa xe (Có/Không) có mở không): ")
        self.open() if car_open_input.lower() == "true" else self.close()

        moto_stand_out_input = input("Nhập trạng thái chân đứng của xe máy (Có/Không có đứng không): ")
        self.stand_out = bool(moto_stand_out_input.lower() == "true")

# Tạo một đối tượng Vehicle
x = Vehicle()
x.nhap_tt()
x.xuattt()

