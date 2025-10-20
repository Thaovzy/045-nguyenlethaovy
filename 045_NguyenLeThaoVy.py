student_list = []

def add_student(name, year_of_birth, address):
    student = {
        "name": name,
        "year": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"✅ Da them sinh vien {name} thanh cong!")

def print_students():
    print("===== DANH SACH SINH VIEN =====")
    for s in student_list:
        print(f"- {s['name']} | {s['year']} | {s['address']}")
    if len(student_list) == 0:
        print("Danh sach rong!")

def search_student(name):
    found = False
    for s in student_list:
        if s['name'].lower() == name.lower():
            print(f"✅ Tim thay: {s['name']} - {s['year']} - {s['address']}")
            found = True
    if not found:
        print("❌ Khong tim thay sinh vien nay.")

def show_menu():
    print("==== CHUONG TRINH QUAN LY SINH VIEN ====")
    print("1. Them sinh vien")
    print("2. Xem danh sach sinh vien")
    print("3. Tim sinh vien theo ten")
    print("4. Thoat")

def main():
    while True:
        show_menu()
        choice = input("Nhap lua chon: ")
        if choice == '1':
            name = input("Nhap ten: ")
            year = int(input("Nhap nam sinh: "))
            address = input("Nhap dia chi: ")
            add_student(name, year, address)
        elif choice == '2':
            print_students()
        elif choice == '3':
            name = input("Nhap ten can tim: ")
            search_student(name)
        elif choice == '4':
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le!")

if __name__ == "__main__":
    main()
