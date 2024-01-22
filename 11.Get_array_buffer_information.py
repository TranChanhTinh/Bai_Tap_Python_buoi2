from array import array

# Khởi tạo mảng với kiểu dữ liệu 'i' (integer)
my_array = array('i', [1, 2, 3, 4, 5])

# Lấy thông tin về bộ đệm của mảng
buffer_info = my_array.buffer_info()

# In ra thông tin về bộ đệm
print("Địa chỉ bắt đầu của bộ đệm:", buffer_info[0])
print("Số lượng phần tử trong mảng:", buffer_info[1])
