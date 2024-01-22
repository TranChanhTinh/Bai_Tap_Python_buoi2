import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
# Chuyển đổi mảng thành chuỗi bytes bằng phương thức tostring()
result_bytes = my_array.tostring()

import struct
array_of_numbers = struct.unpack('I' * (len(result_bytes) // 4), result_bytes)

print(array_of_numbers)
#Tạo mảng NumPy: my_array = np.array([1, 2, 3, 4, 5]) - Tạo một mảng NumPy gồm các số từ 1 đến 5.
#Chuyển đổi mảng thành chuỗi bytes: result_bytes = my_array.tostring() - Sử dụng phương thức tostring() của NumPy để chuyển đổi mảng thành chuỗi bytes.
#Import thư viện struct: import struct - Import thư viện struct để sử dụng các hàm chuyển đổi dữ liệu giữa kiểu số và chuỗi byte.
#Chuyển đổi chuỗi bytes thành mảng số:
#'I' đại diện cho kiểu dữ liệu là unsigned int (4 byte).
#(len(result_bytes) // 4) là số lượng phần tử trong mảng, giả sử mỗi số chiếm 4 byte.
#struct.unpack() được sử dụng để chuyển đổi chuỗi byte thành mảng số.
#-In mảng số kết quả: print(array_of_numbers) - In mảng số đã được chuyển đổi từ chuỗi byte.