# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:59:14 2024

@author: PC
"""

def kiemtra(n):
    return n < 0 and n % 2 == 0
n = int(input("Nhập một số: "))
print(kiemtra(n))