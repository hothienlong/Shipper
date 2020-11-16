import math
from functools import reduce
import random

file1 = open("input.txt","r") 
input_file = file1.read()
lines = input_file.split("\n")
khoA = list(map(int, lines[0].split(" ")))

N = int(lines[1].split(" ")[0])
M = int(lines[1].split(" ")[1])

def khoang_cach_giua_2_diem(diem1, diem2):
  return math.sqrt((diem2[0]- diem1[0])**2 + (diem2[1] - diem1[1])**2)

def print_order_list(order_list):
  for i in range (len(order_list)):
    print("Đơn hàng thứ " + str(order_list[i].id) + " : ", end = ' ')
    print(Order.to_tuple(order_list[i]))
  print()

class Order:
  def __init__(self, id, toado, thetich, trongluong):
    self.id = id
    self.toado = toado
    self.thetich = thetich
    self.trongluong = trongluong
  
  def to_tuple(self):
    return self.toado[0], self.toado[1], self.thetich, self.trongluong

class NhanVien:
  def __init__(self, lstOrder):
    self.lstOrder = lstOrder


def loi_nhuan(lstOrder): 
  quangduong = khoang_cach_giua_2_diem(lstOrder[0].toado, khoA)
  # quangduong = reduce(lambda acc, ele: khoang_cach_giua_2_diem(acc.toado,ele.toado), lstOrder)
  doanhthu = 0
  for i in range (len(lstOrder)):
    cong = 5 + lstOrder[i].thetich + (lstOrder[i].trongluong * 2)
    doanhthu += cong
    if(i < len(lstOrder)-1):
      quangduong += khoang_cach_giua_2_diem(lstOrder[i].toado, lstOrder[i+1].toado)

  chiphi = quangduong / 40 * 20 + 10
  loinhuan = doanhthu - chiphi
  return loinhuan


def ham_luong_gia(lstNhanVien):
  # trixma(trixma(f(i)-f(j)))
  luonggia = 0
  for i in range (len(lstNhanVien)):
    for j in range (len(lstNhanVien)):
      luonggia += abs(loi_nhuan(lstNhanVien[i].lstOrder) - loi_nhuan(lstNhanVien[j].lstOrder))
  return luonggia


def initialize_state(order_list, nhanvien_list):
  for i in range (len(order_list)):
    order_list[i].gan_nhanvien(random.randrange(number_nhanvien))
    

def write_result(order_list, number_nhanvien):
  f = open("output.txt",'w')
  # sort theo id_nhanvien => in xong nhan vien dau thi \n
  order_list.sort(key = lambda x: x.id_nhanvien)
  print_order_list(order_list)

  current_nhanvien = order_list[0].id_nhanvien
  current_order = 0
  while(current_order < len(order_list)):
    if(order_list[current_order].id_nhanvien == current_nhanvien):
      f.write(str(order_list[current_order].id) + " ")
      current_order += 1
    else:
      f.write('\n')
      current_nhanvien += 1


def main():

  order_list = []
  for i in range (2,N+2):
    id = i - 2
    toado = [int(lines[i].split(" ")[0]), int(lines[i].split(" ")[1])]
    thetich = int(lines[i].split(" ")[2])
    trongluong = int(lines[i].split(" ")[3])
    order = Order(id, toado, thetich, trongluong)
    order_list.append(order)
  
  # initialize_state(order_list, M)
  
  print_order_list(order_list)
  print("\nLợi nhuận = ", loi_nhuan(order_list, khoA))
  # write_result(order_list, M)
  # print("\nLợi nhuận = ", loi_nhuan(order_list, khoA))


if __name__ == "__main__":
    main()