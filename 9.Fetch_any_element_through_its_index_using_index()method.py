import numpy as np
twoDArray=np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)
def accessElements(array,rowIndex,colIndex):
    if rowIndex>=len(array)and colIndex>=len(array[0]):
        print('incorect index')
    else:
        print(array[rowIndex],[colIndex])
accessElements(twoDArray,2,3)
#Tạo mảng hai chiều với NumPy: Sử dụng NumPy để tạo một mảng hai chiều có kích thước 4x4 và gán cho biến twoDArray.
#In ra mảng hai chiều: In ra màn hình mảng hai chiều.
#Hàm accessElements(array, rowIndex, colIndex): Hàm này nhận vào một mảng array, một chỉ số hàng rowIndex, và một chỉ số cột colIndex. 
#Kiểm tra nếu chỉ số hàng hoặc chỉ số cột vượt quá kích thước của mảng, in ra thông báo "Incorrect index".
#Ngược lại, in ra phần tử của mảng tại vị trí được xác định bởi chỉ số hàng và chỉ số cột.
#Gọi hàm accessElements với mảng và chỉ số cụ thể: Gọi hàm accessElements với mảng twoDArray và chỉ số hàng là 2 và chỉ số cột là 3. 
#Trong trường hợp này, vị trí (2, 3) của mảng chứa giá trị 8, vì vậy hàm sẽ in ra giá trị này.