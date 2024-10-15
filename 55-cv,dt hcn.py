# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:22:42 2024

@author: PC
"""

def chu_vi(d, r):
    return 2 * (d + r)

def dien_tich(d, r):
    return d * r

def ve_hinh_chu_nhat(d, r):
    for i in range(d):
        print('*' * r)  

if __name__ == "__main__":
    chieu_dai = int(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = int(input("Nhập chiều rộng hình chữ nhật: "))
    print(f"Chu vi hình chữ nhật: {chu_vi(chieu_dai, chieu_rong)}")
    print(f"Diện tích hình chữ nhật: {dien_tich(chieu_dai, chieu_rong)}")
    print("Hình chữ nhật:")
    ve_hinh_chu_nhat(chieu_dai, chieu_rong)