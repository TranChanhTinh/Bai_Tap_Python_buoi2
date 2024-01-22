import numpy as np
twoDArray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

newTwoArray=np.insert(twoDArray,0,[[1,2,3,4]],axis=1)
print(newTwoArray)

#Import thư viện NumPy: Dòng này import thư viện NumPy và đặt tên ngắn gọn là np để thuận tiện khi sử dụng các hàm từ thư viện này.
#Khởi tạo mảng hai chiều: 
#twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]) 
#Tạo một mảng hai chiều twoDArray bằng cách sử dụng hàm np.array(). Mảng này có kích thước 4x4.
#In ra mảng hai chiều gốc: print(twoDArray) In ra màn hình mảng hai chiều twoDArray.
#Chèn một hàng mới vào mảng: newTwoArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1) 
#Sử dụng hàm np.insert() để chèn một hàng mới vào mảng.
#twoDArray là mảng gốc.0 là chỉ số của hàng mới sẽ được chèn (ở đầu mảng). [[1, 2, 3, 4]] là mảng mới cần chèn. 
#axis=1 chỉ định rằng chèn theo chiều ngang (cột).
#In ra mảng mới sau khi chèn: print(newTwoArray) 
#In ra màn hình mảng mới sau khi chèn. Mảng mới này có thêm một hàng ở đầu mảng so với mảng gốc.