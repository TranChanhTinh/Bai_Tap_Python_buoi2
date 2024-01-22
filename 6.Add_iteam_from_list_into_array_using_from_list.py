from array import array
#Dòng này import lớp array từ mô-đun array để sử dụng.
my_array = array('i', [1, 2, 3, 4, 5])
#Dòng này tạo một mảng có tên là my_array với kiểu dữ liệu là số nguyên ('i') và khởi tạo nó với các giá trị [1, 2, 3, 4, 5].
elements_to_add = [6, 7, 8, 9, 10]
#Dòng này tạo một danh sách (list) có tên là elements_to_add chứa các giá trị [6, 7, 8, 9, 10].
my_array.fromlist(elements_to_add)
#Dòng này sử dụng phương thức fromlist() của mảng my_array để thêm các phần tử từ danh sách elements_to_add vào cuối mảng. 
#Sau dòng này, my_array sẽ chứa tất cả các phần tử của cả hai mảng.
print(my_array)
#Dòng này in ra màn hình mảng my_array sau khi đã được mở rộng.