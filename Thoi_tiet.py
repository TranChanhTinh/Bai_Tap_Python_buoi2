import array as arr

def tinh_nhiet_do_trung_binh(nhiet_do_ngay):
    tong_nhiet_do = sum(nhiet_do_ngay)
    nhiet_do_trung_binh = tong_nhiet_do / len(nhiet_do_ngay)
    return nhiet_do_trung_binh

def dem_so_ngay_tren_trung_binh(nhiet_do_ngay, nhiet_do_trung_binh):
    so_ngay_tren_trung_binh = sum(nhiet_do > nhiet_do_trung_binh for nhiet_do in nhiet_do_ngay)
    return so_ngay_tren_trung_binh

so_ngay = int(input("Nhập số ngày: "))   
nhiet_do_ngay = arr.array('i', [])
for ngay in range(1, so_ngay + 1):
        nhiet_do = int(input(f"Nhiệt độ ngày {ngay}: "))
        nhiet_do_ngay.append(nhiet_do)

nhiet_do_trung_binh = tinh_nhiet_do_trung_binh(nhiet_do_ngay)
print("\nNhiệt độ các ngày:", nhiet_do_ngay)
print("Nhiệt độ trung bình =", nhiet_do_trung_binh)
   
so_ngay_tren_trung_binh = dem_so_ngay_tren_trung_binh(nhiet_do_ngay, nhiet_do_trung_binh)
print(f"Số ngày có nhiệt độ trên trung bình là {so_ngay_tren_trung_binh} ngày")
