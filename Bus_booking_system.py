class Bus:
    def __init__(self, bcode, bus_name, seat, depart_time, arrival_time):
        """
        Khởi tạo một đối tượng Bus với các thuộc tính bcode (mã xe),
        bus_name (tên xe), seat (số ghế), depart_time (thời gian khởi hành),
        và arrival_time (thời gian đến).
        """
        self.bcode = bcode
        self.bus_name = bus_name
        self.seat = seat
        self.booked = 0
        self.depart_time = depart_time
        self.arrival_time = arrival_time

    # Phương thức này trả về một chuỗi
    def __str__(self):
        return f"{self.bcode:<8} | {self.bus_name:<15} | {self.seat:<8} | {self.booked:<8} | {self.depart_time:<13} | {self.arrival_time:<10}"

# -------------------------------------------
# Khởi tạo một nút trong cây nhị phân
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

# -------------------------------------------
class BinarySearchTree:
    def __init__(self):
        # Khởi tạo một cây nhị phân rỗng.
        self.root = None

    # Chèn một nút mới vào cây nhị phân.
    def insert(self, key, data):
        if not self.root:
            self.root = Node(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    # Chèn một nút mới vào cây nhị phân bằng cách đệ quy.
    def _insert_recursive(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
            else:
                self._insert_recursive(node.left, key, data)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, data)
            else:
                self._insert_recursive(node.right, key, data)
        else:
            #Trường hợp khóa trùng lặp
            pass

    # Duyệt cây theo thứ tự trung tố
    def in_order_traverse(self, node):
        if node is not None:
            self.in_order_traverse(node.left)
            print(node.data)
            self.in_order_traverse(node.right)
            
    # Duyệt cây theo mức độ rộng
    def breadth_first_traverse(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            # Lấy node đầu tiên ra khỏi danh sách
            node = queue.pop(0)
            print(node.data)
            # Thêm node con (nếu có) vào danh sách
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
    # Duyệt cây theo thứ tự trung tố và ghi vào file
    def in_order_traverse_to_file(self, node, file):
        if node is not None:
            if node.left:
                self.in_order_traverse_to_file(node.left, file)
            file.write(f"{node.data.bcode}, {node.data.bus_name}, {node.data.seat}, {node.data.booked}, {node.data.depart_time}, {node.data.arrival_time}\n")
            if node.right:
                self.in_order_traverse_to_file(node.right, file)

    # Tìm kiếm một nút trong cây theo khóa
    def search(self, key):
        return self._search_recursive(self.root, key)

    # Tìm kiếm một nút trong cây theo khóa (đệ quy)
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # Xóa một nút khỏi cây theo khóa cho trước
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    # Xóa một nút khỏi cây theo khóa cho trước (đệ quy)
    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.data = temp.data
                node.right = self._delete_recursive(node.right, temp.key)
        return node

    # Tìm và trả về nút có khóa nhỏ nhất trong cây con phải
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Đếm số lượng xe buýt trong cây
    def count_buses(self):
        return self._count_buses_recursive(self.root)

    # Đếm số lượng xe buýt trong cây (đệ quy)
    def _count_buses_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_buses_recursive(node.left) + self._count_buses_recursive(node.right)
    
    # Duyệt cây theo thứ tự trung tố
    def in_order_traverse_to_list(self, node, node_list):
        if node is not None:
            self.in_order_traverse_to_list(node.left, node_list)
            node_list.append(node)
            self.in_order_traverse_to_list(node.right, node_list)

    # Cân bằng cây nhị phân
    def balance_tree(self):
        nodes = []
        self.in_order_traverse_to_list(self.root, nodes)
        self.root = self.build_balanced_tree(nodes)

    # Xây dựng một cây nhị phân cân bằng từ một danh sách các nút
    def build_balanced_tree(self, nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = nodes[mid]
        root.left = self.build_balanced_tree(nodes[:mid])
        root.right = self.build_balanced_tree(nodes[mid + 1:])
        return root

    
# -------------------------------------------
class Customer:
    def __init__(self, ccode, cus_name, phone):
        """
        Khởi tạo một đối tượng Customer với các thuộc tính ccode (mã khách hàng),
        cus_name (tên khách hàng), và phone (số điện thoại).
        """
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone

    def __str__(self):
        return f"{self.ccode:<13} | {self.cus_name:<15} | {self.phone:<12}"

# -------------------------------------------
# Khởi tạo một nút trong danh sách liên kết với dữ liệu cho trước.
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# -------------------------------------------
class LinkedList:
    # Khởi tạo một danh sách liên kết rỗng.
    def __init__(self):
        self.head = None

    # Thêm một phần tử vào cuối danh sách liên kết.
    def append(self, data):
        if not self.head:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)

    # In ra màn hình tất cả các phần tử trong danh sách liên kết
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
# ===========================================
"""
Hiển thị menu chính của chương trình.
"""
def display_menu():
    print("Hệ thống đặt vé xe buýt")
    print("1. Quản lý Xe buýt")
    print("2. Quản lý Khách hàng")
    print("3. Quản lý Đặt vé")
    print("4. Thoát")

# -------------------------------------------
# Quản lý các chức năng liên quan đến xe buýt
def manage_buses(buses_tree):
    while True:
        print("\n-------------")
        print("Quản lý Xe buýt")
        print("1. Tải dữ liệu từ file")
        print("2. Nhập và thêm dữ liệu")
        print("3. Duyệt theo thứ tự")
        print("4. Duyệt theo mức độ rộng")
        print("5. Ghi ra file theo thứ tự")
        print("6. Tìm kiếm theo mã xe")
        print("7. Xóa theo mã xe")
        print("8. Cân bằng cây")
        print("9. Đếm số lượng xe buýt")
        print("10. Quay lại menu chính")

        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            load_data_from_file(buses_tree)
        elif choice == "2":
            input_and_insert_data(buses_tree)
        elif choice == "3":
            print("Duyệt theo thứ tự:")
            display_bus_table_header()
            buses_tree.in_order_traverse(buses_tree.root)
        elif choice == "4":
            print("Duyệt theo mức độ rộng:")
            display_bus_table_header()
            buses_tree.breadth_first_traverse()
        elif choice == "5":
            save_to_file(buses_tree)
        elif choice == "6":
            search_bus(buses_tree)
        elif choice == "7":
            delete_bus(buses_tree)
        elif choice == "8":
            balance_tree(buses_tree)
        elif choice == "9":
            print(f"Số lượng xe buýt: {buses_tree.count_buses()}")
        elif choice == "10":
            return
        else:
            print("Lựa chọn không hợp lệ.")

# Tải dữ liệu về xe buýt từ một file và chèn vào cây nhị phân
def load_data_from_file(buses_tree):
    file_name = input("Nhập tên file: ")
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                bcode, bus_name, seat, depart_time, arrival_time = data
                bus = Bus(bcode, bus_name, int(seat), float(depart_time), float(arrival_time))
                buses_tree.insert(bcode, bus)
        print("Dữ liệu được tải thành công.")
    except FileNotFoundError:
        print("Không tìm thấy file.")
        
# Nhập thông tin về xe buýt mới và thêm vào cây nhị phân
def input_and_insert_data(buses_tree):
    print("Nhập thông tin xe buýt mới:")
    bcode = input("Nhập mã xe: ")
    if check_duplicate_bcode(buses_tree, bcode):
        print("Mã xe đã tồn tại trong hệ thống.")
        return
    bus_name = input("Nhập tên xe: ")
    seat = int(input("Nhập số ghế: "))
    if seat <= 0:
        print("Số ghế phải lớn hơn 0.")
        return
    depart_time = float(input("Nhập giờ khởi hành: "))
    if depart_time <= 0:
        print("Giờ khởi hành phải lớn hơn 0.")
        return
    arrival_time = float(input("Nhập giờ đến: "))
    if arrival_time <= depart_time:
        print("Giờ đến phải lớn hơn giờ khởi hành.")
        return
    bus = Bus(bcode, bus_name, seat, depart_time, arrival_time)
    buses_tree.insert(bcode, bus)
    print("Xe buýt được thêm thành công.")
    
# Kiểm tra sự trùng lặp của mã xe trong cây nhị phân
def check_duplicate_bcode(buses_tree, bcode):
    return buses_tree.search(bcode) is not None
    
# Hiển thị tiêu đề cho bảng thông tin về xe buýt
def display_bus_table_header():
    print(f"{'Mã xe':<8} | {'Tên xe':<15} | {'Số ghế':<8} | {'Đã đặt':<8} | {'Giờ khởi hành':<12} | {'Giờ đến':<10}")
        
# Lưu thông tin về các xe buýt vào một file
def save_to_file(buses_tree):
    file_name = input("Nhập tên file: ")
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            buses_tree.in_order_traverse_to_file(buses_tree.root, file)
        print("Dữ liệu được ghi vào file thành công.")
    except FileNotFoundError:
        print("Không tìm thấy file.")

# Tìm kiếm thông tin về một xe buýt dựa trên mã xe
def search_bus(buses_tree):
    bcode = input("Nhập mã xe buýt cần tìm: ")
    bus = buses_tree.search(bcode)
    if bus:
        print("Thông tin xe buýt:")
        print(bus.data)
    else:
        print("Không tìm thấy xe buýt có mã này.")

# Xóa thông tin về một xe buýt dựa trên mã xe
def delete_bus(buses_tree):
    bcode = input("Nhập mã xe buýt cần xóa: ")
    buses_tree.delete(bcode)
    print("Xe buýt đã được xóa.")

# Cân bằng cây nhị phân tìm kiếm chứa thông tin về các xe buýt
def balance_tree(buses_tree):
    nodes = []
    buses_tree.in_order_traverse_to_list(buses_tree.root, nodes)
    buses_tree.root = buses_tree.build_balanced_tree(nodes)


# -------------------------------------------
def manage_customers(customers_list):
    while True:
        print("\n----------------")
        print("Quản lý Khách hàng")
        print("1. Tải dữ liệu từ file")
        print("2. Thêm khách hàng")
        print("3. Hiển thị danh sách khách hàng")
        print("4. Lưu danh sách khách hàng vào file")
        print("5. Tìm kiếm khách hàng theo mã")
        print("6. Xóa khách hàng theo mã")
        print("7. Quay lại menu chính")

        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            load_customer_data_from_file(customers_list)
        elif choice == "2":
            add_customer(customers_list)
        elif choice == "3":
            print("Danh sách khách hàng:")
            display_customer_table_header()
            customers_list.display()
        elif choice == "4":
            save_customer_list_to_file(customers_list)
        elif choice == "5":
            search_customer_by_ccode(customers_list)
        elif choice == "6":
            delete_customer_by_ccode(customers_list)
        elif choice == "7":
            return
        else:
            print("Lựa chọn không hợp lệ.")

# Tải dữ liệu về danh sách khách hàng từ một file
def load_customer_data_from_file(customers_list):
    file_name = input("Nhập tên file: ")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")
                ccode, cus_name, phone = data
                customer = Customer(ccode, cus_name, phone)
                customers_list.append(customer)
        print("Dữ liệu được tải thành công.")
    except FileNotFoundError:
        print("Không tìm thấy file.")

# Thêm thông tin về một khách hàng mới vào danh sách
def add_customer(customers_list):
    print("Nhập thông tin khách hàng mới:")
    ccode = input("Nhập mã khách hàng: ")
    if check_duplicate_ccode(customers_list, ccode):
        print("Mã khách hàng đã tồn tại trong hệ thống.")
        return
    cus_name = input("Nhập tên khách hàng: ")
    
    phone = input("Nhập số điện thoại: ")
    if not phone.isdigit():
        print("Số điện thoại phải chứa chỉ chứa chữ số.")
        return

    customer = Customer(ccode, cus_name, phone)
    customers_list.append(customer)
    print("Khách hàng được thêm thành công.")
    
# Kiểm tra sự trùng lặp của mã khách hàng trong danh sách liên kết
def check_duplicate_ccode(customers_list, ccode):
    current = customers_list.head
    while current:
        if current.data.ccode == ccode:
            return True
        current = current.next
    return False
    
# Hiển thị tiêu đề cho bảng thông tin về khách hàng
def display_customer_table_header():
    print(f"{'Mã khách hàng':<8} | {'Tên khách hàng':<15} | {'Điện thoại':<12}")

# Lưu danh sách khách hàng vào một file
def save_customer_list_to_file(customers_list):
    file_name = input("Nhập tên file: ")
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            current = customers_list.head
            while current:
                file.write(f"{current.data.ccode},{current.data.cus_name},{current.data.phone}\n")
                current = current.next
        print("Danh sách khách hàng được ghi vào file thành công.")
    except FileNotFoundError:
        print("Không tìm thấy file.")
        
# Tìm kiếm khách hàng trong danh sách theo mã khách hàng
def search_customer_by_ccode(customers_list, ccode):
    current = customers_list.head
    while current:
        if current.data.ccode == ccode:
            return current.data
        current = current.next
    return None

# Xóa khách hàng khỏi danh sách theo mã khách hàng
def delete_customer_by_ccode(customers_list):
    ccode = input("Nhập mã khách hàng cần xóa: ")
    current = customers_list.head
    prev = None
    while current:
        if current.data.ccode == ccode:
            if prev:
                prev.next = current.next
            else:
                customers_list.head = current.next
            print("Khách hàng đã được xóa.")
            return
        prev = current
        current = current.next
    print("Không tìm thấy khách hàng có mã này.")


# -------------------------------------------
def manage_bookings(bookings_list, buses_tree, customers_list):
    while True:
        print("\n------------")
        print("Quản lý Đặt vé")
        print("1. Nhập thông tin đặt vé")
        print("2. Hiển thị thông tin đặt vé")
        print("3. Sắp xếp theo mã xe + mã khách hàng")
        print("4. Quay lại menu chính")

        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            input_booking_data(bookings_list, buses_tree, customers_list)
        elif choice == "2":
            print("Thông tin đặt vé:")
            print( f"| {'Mã xe':<8} | {'Mã khách hàng':<12} | {'Số ghế':<8} |")
            bookings_list.display()
        elif choice == "3":
            sort_bookings(bookings_list)
        elif choice == "4":
            return
        else:
            print("Lựa chọn không hợp lệ.")

# Nhập thông tin đặt vé
def input_booking_data(bookings_list, buses_tree, customers_list):
    bcode = input("Nhập mã xe buýt: ")
    bus_node = buses_tree.search(bcode)
    if not bus_node:
        print("Không tìm thấy xe buýt có mã này.")
        return

    bus = bus_node.data
    ccode = input("Nhập mã khách hàng: ")
    customer = search_customer_by_ccode(customers_list, ccode)
    if not customer:
        print("Không tìm thấy khách hàng có mã này.")
        return

    seat = int(input("Nhập số ghế cần đặt: "))
    if seat <= 0:
        print("Số ghế cần đặt phải lớn hơn 0.")
        return
    if seat > bus.seat - bus.booked:
        print("Không đủ ghế trống trên xe buýt.")
        return

    booking_info = f"| {bcode:<8} | {ccode:<13} | {seat:<8} |"
    bookings_list.append(booking_info)
    bus.booked += seat

    print("Đặt vé thành công.")

    while True:
        choice = input("Bạn có muốn tiếp tục đặt vé không? (Y/N): ").strip().upper()
        if choice == "Y":
            input_booking_data(bookings_list, buses_tree, customers_list)
            break
        elif choice == "N":
            break
        else:
            print("Lựa chọn không hợp lệ.")

# Sắp xếp danh sách đặt vé theo mã xe và mã khách hàng
def sort_bookings(bookings_list):
    # Chuyển đổi danh sách LinkedList thành danh sách thông thường
    bookings = []
    current = bookings_list.head
    while current:
        bookings.append(current.data)
        current = current.next

    # Sắp xếp danh sách đặt vé
    sorted_bookings = sorted(bookings, key=lambda x: (x.split("|")[1].strip(), x.split("|")[2].strip()))
    print("Danh sách đặt vé sau khi sắp xếp:\n")
    print( f"| {'Mã xe':<8} | {'Mã khách hàng':<12} | {'Số ghế':<8} |")
    for booking in sorted_bookings:
        print(booking)


# ===========================================
'''
Hàm main chạy chương trình
'''
def main():
    buses_tree = BinarySearchTree()
    customers_list = LinkedList()
    bookings_list = LinkedList()

    while True:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            manage_buses(buses_tree)
        elif choice == "2":
            manage_customers(customers_list)
        elif choice == "3":
            manage_bookings(bookings_list, buses_tree, customers_list)
        elif choice == "4":
            print("Đang thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại lựa chọn.")
            
if __name__ == "__main__":
    main()