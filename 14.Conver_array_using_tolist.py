import numpy as np
array=np.array([1,2,0,4])
list=array.tolist()
print(list)
#import numpy as np: Dòng này import thư viện NumPy và đặt tên ngắn là np để sử dụng ngắn gọn hơn trong mã.
#array = np.array([1, 2, 0, 4]): Dòng này tạo một mảng NumPy có tên là array và chứa các giá trị [1, 2, 0, 4].
#list = array.tolist(): Dòng này sử dụng phương thức tolist() của NumPy để chuyển đổi mảng NumPy thành một danh sách Python. 
#Kết quả được gán vào biến list.
#print(list): Dòng này in ra màn hình danh sách (list) sau khi chuyển đổi từ mảng NumPy.