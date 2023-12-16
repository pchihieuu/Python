class Cha:
    def __init__(self, htcha, ngaysinhcha):
        self.htcha = htcha
        self.ngaysinhcha = ngaysinhcha

    def xuatttcha(self):
        print("Họ tên Cha: ", self.htcha)
        print("Ngày sinh Cha: ", self.ngaysinhcha)


class Me:
    def __init__(self, htme, ngaysinhme):
        self.htme = htme
        self.ngaysinhme = ngaysinhme

    def xuatttme(self):
        print("Họ tên Mẹ: ", self.htme)
        print("Ngày sinh Mẹ: ", self.ngaysinhme)


class Congdan(Cha, Me):
    def __init__(self, hoten, socm, ns, gt, htcha, ngaysinhcha, htme, ngaysinhme):
        Cha.__init__(self, htcha, ngaysinhcha)
        Me.__init__(self, htme, ngaysinhme)
        self.hoten = hoten
        self.socm = socm
        self.ns = ns
        self.gt = gt

    def xuattt(self):
        print("Họ tên: ", self.hoten)
        print("Số CM: ", self.socm)
        print("Ngày sinh: ", self.ns)
        print("Giới tính: ", self.gt)
        self.xuatttcha()
        self.xuatttme()


# Nhập dữ liệu cho 2 công dân x, y và xuất thông tin của họ ra màn hình
x = Congdan("Nguyen Van Dang","12345" ,"01/01/2000", "Nam", "Nguyen Van Teo", "01/01/1970", "Nguyen Thi Ly", "01/01/1975")
y = Congdan("Nguyen Van Hao","34344","01/01/2001", "Nam", "Nguyen Van Khoi", "01/01/1971", "Nguyen Thi Hau", "01/01/1976")

x.xuattt()
y.xuattt()
