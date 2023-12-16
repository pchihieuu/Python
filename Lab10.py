# Cau 1: Thực hiện nối set và list
# Output: {'Blue', 'Yellow', 'Orange', 'Green', 'Black', 'Red'}
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

result = set(sample_list).union(sample_set)
print(result)

# Cau2:  Trả về Set mới giống nhau mới từ 2 Set đã cho.
# Output: {40, 50, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = set1.intersection(set2)
print(result)

# Cau3: Viết chương trình Python để trả về một bộ mới với các mục duy nhất từ cả hai bộ bằng cách loại bỏ các bản sao.
# Output: {70, 40, 10, 50, 20, 60, 30}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.union(set2)
print(result)

# Cau4: Cho các mối quan hệ giữa các đối tượng sau:
# Require: Tạo 2 biến đối tượng và xuất thông tin đối tượng ra để xem trên màn hình Console.
class A:
    def __init__(self, tena):
        self.tena = tena


    def xuatttcha(self):
        print("Tên của A: ", self.tena)



class B:
    def __init__(self, tenb):
        self.tenb = tenb

    def xuatttme(self):
        print("Tên của B: ", self.tenb)



class C(A, B):
    def __init__(self, hoten, ns, tena, tenb):
        A.__init__(self, tena)
        B.__init__(self, tenb)
        self.hoten = hoten
        self.ns = ns


    def xuattt(self):
        print("Họ tên: ", self.hoten)
        print("Ngày sinh: ", self.ns)
        # print("Giới tính: ", self.gt)
        self.xuatttcha()
        self.xuatttme()


# Nhập dữ liệu cho 2 công dân x, y và xuất thông tin của họ ra màn hình
x = C("Nguyen Van X", "01/01/2000", "Nguyen Van A", "Nguyen Thi B")
y = C("Nguyen Van Y", "01/01/2001", "Nguyen Van C", "Nguyen Thi D")

x.xuattt()
y.xuattt()


