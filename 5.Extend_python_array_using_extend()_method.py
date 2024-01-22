import array as arr
#Dòng này import mô-đun array và đặt tên ngắn là arr để sử dụng ngắn gọn hơn trong mã.
my_array=arr.array('i',[1,2,3,4,5])
#Dòng này tạo một mảng có tên là my_array với kiểu dữ liệu là số nguyên ('i') và khởi tạo nó với các giá trị [1, 2, 3, 4, 5].
my_array_2=arr.array('i',[6,7,8,9,10])
#Dòng này tạo một mảng khác có tên là my_array_2 cũng với kiểu dữ liệu là số nguyên ('i') và khởi tạo nó với các giá trị [6, 7, 8, 9, 10].
my_array.extend(my_array_2)
#Dòng này sử dụng phương thức extend() của mảng my_array để thêm các phần tử của mảng my_array_2 vào cuối my_array.
#Sau dòng này, my_array sẽ chứa tất cả các phần tử của cả hai mảng.
print(my_array)#in ra màn hình mảng my_array sau khi đã được mở rộng