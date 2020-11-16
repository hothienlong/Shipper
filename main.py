import math
from functools import reduce

def khoang_cach_giua_2_diem(diem1, diem2):
  return math.sqrt((diem2[0]- diem1[0])**2 + (diem2[1] - diem1[1])**2)

def print_order_list(order_list):
  for i in range (len(order_list)):
    Order.print_list(order_list[i])


class Order:
  def __init__(self, id, toado, thetich, trongluong):
    self.id = id
    self.toado = toado
    self.thetich = thetich
    self.trongluong = trongluong
  
  def print_list(self):
    print("Đơn hàng thứ " + str(self.id) + " : ", end = ' ')
    print([self.toado[0], self.toado[1], self.thetich, self.trongluong])



def ham_luong_gia(lstOrder, khoA): 
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
  print("quang duong = ", quangduong)
  return loinhuan


def main():
  file1 = open("input.txt","r") 
  input_file = file1.read()
  lines = input_file.split("\n")
  khoA = list(map(int, lines[0].split(" ")))
  print(khoA)

  N = int(lines[1].split(" ")[0])
  M = int(lines[1].split(" ")[1])

  order_list = []
  for i in range (2,N+2):
    id = i - 2
    toado = [int(lines[i].split(" ")[0]), int(lines[i].split(" ")[1])]
    thetich = int(lines[i].split(" ")[2])
    trongluong = int(lines[i].split(" ")[3])
    order = Order(id, toado, thetich, trongluong)
    order_list.append(order)
 
  print_order_list(order_list)
  print(order_list[0].toado)
  print(ham_luong_gia(order_list, khoA))


main()