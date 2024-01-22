import array as arr

def tim_cac_cap_so_tong_duoc(numbers, target_sum):
    cac_cap = []  # Danh sách để lưu trữ các cặp số thỏa mãn điều kiện
    cac_so_da_xem = set()  # Tập hợp để theo dõi các số đã xem

    for num in numbers:
        so_bo_sung = target_sum - num  # Tính số bổ sung để có tổng bằng target_sum

        if so_bo_sung in cac_so_da_xem:
            cac_cap.append((so_bo_sung, num))  # Nếu số bổ sung đã xem, thêm cặp số vào danh sách

        cac_so_da_xem.add(num)  # Thêm số hiện tại vào tập hợp để theo dõi

    return cac_cap

numbers = [2, 7, 11, 15]
target_sum = 9
result = tim_cac_cap_so_tong_duoc(numbers, target_sum)
print(f"Tong cua {target_sum} = {result}")