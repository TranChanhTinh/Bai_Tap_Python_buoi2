from array import array

# Khởi tạo mảng với kiểu dữ liệu 'b' (singed char)
my_array = array('b', b'Hello')

# In ra mảng trước khi nối chuỗi
print("Mảng trước khi nối chuỗi:", my_array)

# Chuỗi cần nối vào mảng
string_to_add = " World"
# không sử dụng fromlist() được vì hàm này yêu câu giá trị int chứ không phải char 
#sử dụng frombytes thay cho fromlist()
# Chuyển đổi chuỗi thành bytes và sử dụng phương thức frombytes() để nối vào mảng
my_array.frombytes(string_to_add.encode('utf-8'))

# In ra mảng sau khi nối chuỗi
print("Mảng sau khi nối chuỗi:", my_array)
# Chuỗi giá trị ASCII
ascii_values = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]

# Chuyển đổi từng giá trị ASCII thành ký tự và tạo chuỗi
result_string = ''.join(chr(value) for value in ascii_values)

# In kết quả
print("Chuỗi ký tự tương ứng với giá trị ASCII là:", result_string)
