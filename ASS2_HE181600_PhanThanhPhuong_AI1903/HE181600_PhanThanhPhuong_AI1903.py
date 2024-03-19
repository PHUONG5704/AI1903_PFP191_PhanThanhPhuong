#1 

class Book:
    def __init__(self, ten_sach, ten_tac_gia, nha_xuat_ban, nam_xb, gia_ban):
        self.ten_sach = ten_sach
        self.ten_tac_gia = ten_tac_gia
        self.nha_xuat_ban = nha_xuat_ban
        self.nam_xb = nam_xb
        self.gia_ban = gia_ban

def menu():
    print("===========================================")
    print("1. Nhập thông tin của n cuốn sách của FU")
    print("2. In ra màn hình thông tin vừa nhập")
    print("3. Sắp xếp thông tin giảm dần theo năm xuất bản và hiển thị")
    print("4. Tìm kiếm theo tên sách")
    print("5. Tìm kiếm theo tên tác giả")
    print("6. Thoát")
    print("===========================================")

def nhap_thong_tin_sach():
    n = int(input("Nhập số lượng cuốn sách: "))
    books = []
    for i in range(n):
        print(f"Nhập thông tin cho cuốn sách thứ {i+1}:")
        ten_sach = input("Tên sách: ")
        ten_tac_gia = input("Tên tác giả: ")
        nha_xuat_ban = input("Nhà xuất bản: ")
        nam_xb = int(input("Năm xuất bản: "))
        gia_ban = float(input("Giá bán: "))
        books.append(Book(ten_sach, ten_tac_gia, nha_xuat_ban, nam_xb, gia_ban))
    with open("FU.txt", "w") as file:
        file.write(str(n) + "\n\n")
        for book in books:
            file.write(book.ten_sach + "\n")
            file.write(book.ten_tac_gia + "\n")
            file.write(book.nha_xuat_ban + "\n")
            file.write(str(book.nam_xb) + "\n")
            file.write(str(book.gia_ban) + "\n\n")
    print("Thông tin đã được lưu vào file FU.txt")

def in_thong_tin_sach():
    with open("FU.txt", "r") as file:
        lines = file.readlines()
        total_books = int(lines[0].strip())
        print(f"Tổng số cuốn sách: {total_books}")
        print("Thông tin các cuốn sách:")
        print("{:<30} {:<30} {:<10} {:<10}".format("Tên sách", "Tên tác giả", "Năm XB", "Giá"))
        for i in range(1, len(lines), 6):
            ten_sach = lines[i].strip()
            ten_tac_gia = lines[i+1].strip()
            nam_xb = int(lines[i+3].strip())
            gia_ban = float(lines[i+4].strip())
            print("{:<30} {:<30} {:<10} {:<10}".format(ten_sach, ten_tac_gia, nam_xb, gia_ban))

def sap_xep_va_hien_thi():
    with open("FU.txt", "r") as file:
        lines = file.readlines()[1:]
        books = []
        for i in range(0, len(lines), 6):
            ten_sach = lines[i].strip()
            ten_tac_gia = lines[i+1].strip()
            nha_xuat_ban = lines[i+2].strip()
            nam_xb = int(lines[i+3].strip())
            gia_ban = float(lines[i+4].strip())
            books.append(Book(ten_sach, ten_tac_gia, nha_xuat_ban, nam_xb, gia_ban))
        sorted_books = sorted(books, key=lambda x: (-x.nam_xb, -x.gia_ban))
        with open("FU2022.txt", "w") as output_file:
            output_file.write(str(len(sorted_books)) + "\n\n")
            for book in sorted_books:
                output_file.write(book.ten_sach + "\n")
                output_file.write(book.ten_tac_gia + "\n")
                output_file.write(book.nha_xuat_ban + "\n")
                output_file.write(str(book.nam_xb) + "\n")
                output_file.write(str(book.gia_ban) + "\n\n")
        print(f"Tổng số cuốn sách: {len(sorted_books)}")
        print("Thông tin các cuốn sách đã sắp xếp:")
        print("{:<30} {:<30} {:<10} {:<10}".format("Tên sách", "Tên tác giả", "Năm XB", "Giá"))
        for book in sorted_books:
            print("{:<30} {:<30} {:<10} {:<10}".format(book.ten_sach, book.ten_tac_gia, book.nam_xb, book.gia_ban))

def tim_kiem_theo_ten_sach():
    ten_sach_can_tim = input("Nhập tên sách cần tìm: ")
    found = False
    with open("FU.txt", "r") as file:
        lines = file.readlines()[1:]
        for i in range(0, len(lines), 6):
            ten_sach = lines[i].strip()
            ten_tac_gia = lines[i+1].strip()
            nha_xuat_ban = lines[i+2].strip()
            nam_xb = int(lines[i+3].strip())
            gia_ban = float(lines[i+4].strip())
            if ten_sach == ten_sach_can_tim:
                found = True
                print(f"{ten_sach}, {ten_tac_gia}, {nha_xuat_ban}")
    if not found:
        print("Không tìm thấy cuốn sách nào.")
        
def tim_kiem_theo_ten_tac_gia():
    ten_tac_gia_can_tim = input("Nhập tên tác giả cần tìm: ")
    found_books = {}
    with open("FU.txt", "r") as file:
        lines = file.readlines()[1:]
        for i in range(0, len(lines), 6):
            ten_sach = lines[i].strip()
            ten_tac_gia = lines[i+1].strip()
            nha_xuat_ban = lines[i+2].strip()
            nam_xb = int(lines[i+3].strip())
            gia_ban = float(lines[i+4].strip())
            if ten_tac_gia == ten_tac_gia_can_tim:
                found_books[ten_sach] = found_books.get(ten_sach, 0) + 1
    if found_books:
        print(f"Tác giả '{ten_tac_gia_can_tim}' đã viết {len(found_books)} cuốn sách:")
        for ten_sach, so_lan in found_books.items():
            print(f"{ten_tac_gia_can_tim}, {ten_sach}, {so_lan}")
    else:
        print("Không tìm thấy tác giả trên!")

# Hàm main
def main():
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            nhap_thong_tin_sach()
        elif choice == '2':
            in_thong_tin_sach()
        elif choice == '3':
            sap_xep_va_hien_thi()
        elif choice == '4':
            tim_kiem_theo_ten_sach()
        elif choice == '5':
            tim_kiem_theo_ten_tac_gia()
        elif choice == '6':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()

