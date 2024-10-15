# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:16:52 2024

@author: PC
"""
def kiemtra():
    n = int(input("Nhập một số trong đoạn [-89, 90]: "))
    while n < -89 or n > 90:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
        n = int(input("Nhập một số trong đoạn [-89, 90]: "))     
    return n
print(f"Số hợp lệ bạn đã nhập là: {kiemtra()}")
