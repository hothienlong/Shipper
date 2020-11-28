import math
from functools import reduce # sử dụng khi param cùng kiểu với return
import random
import copy

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
  def __init__(self, id, toado, thetich, trongluong, id_nhanvien):
    self.id = id
    self.toado = toado
    self.thetich = thetich
    self.trongluong = trongluong
    self.id_nhanvien = id_nhanvien

  def gan_nhanvien(self, id_nhanvien):
    self.id_nhanvien = id_nhanvien
  
  def to_tuple(self):
    return self.toado[0], self.toado[1], self.thetich, self.trongluong, self.id_nhanvien


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


def ham_luong_gia(lstOrder):
  lstNhanVien = {}
  for i in range (len(lstOrder)):
    current_nhanvien = lstOrder[i].id_nhanvien
    try:
      lstNhanVien[current_nhanvien] += [lstOrder[i]]
    except:
      lstNhanVien[current_nhanvien] = [lstOrder[i]]
      
  luonggia = 0
  for i in lstNhanVien:
    for j in lstNhanVien:
      # trixma(trixma(abs(f(i) - f(j))))
      luonggia += abs(loi_nhuan(lstNhanVien[i]) - loi_nhuan(lstNhanVien[j]))
  return luonggia


def initialize_state(order_list, number_nhanvien):
  assigned = []
  lstIdOrder = [i for i in range(len(order_list))]
  for i in range(number_nhanvien):
    lstChoice = list(set(lstIdOrder) - set(assigned))
    ran = random.choice(lstChoice)
    order_list[ran].gan_nhanvien(i)
    assigned.append(ran)
  lstNotAssigned = list(set(lstIdOrder) - set(assigned))
  for i in lstNotAssigned:
    order_list[i].gan_nhanvien(random.randrange(number_nhanvien))
    

def write_result(order_list):
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


def checkTotal(lstOrder, M):
  lstCheck = []
  for i in range(M):
    lstCheck.append(False)
  for x in lstOrder:
    lstCheck[x.id_nhanvien] = True
  for x in lstCheck:
    if x == False:
      return False
  return True


def generate_neighbours(lstOrder, M):

  neighbours = []

  for i in range(len(lstOrder)):

    curr_nv = lstOrder[i].id_nhanvien

    for nv in range(M):
      neighbour = copy.deepcopy(lstOrder)
      if nv != curr_nv:
        neighbour[i].id_nhanvien = nv
        if checkTotal(neighbour, M) == True:
          neighbours.append(neighbour)

  return neighbours


def hill_climbing_search(current, M):

  while True:

    E = []
    neighbours = []

    current_state = ham_luong_gia(current)
    print("current state = ", current_state)

    neighbours = generate_neighbours(current, M)

    for x in neighbours:
      E.append(ham_luong_gia(x))  

    min_value = min(E) if E else current_state

    if current_state <= min_value:
        return (current, current_state)

    else:
      best_neighbours = [i for i, x in enumerate(E) if x == min_value]

      neighbour = best_neighbours[random.randrange(len(best_neighbours))]

      current = neighbours[neighbour]


def main():
  order_list = []
  for i in range (2,N+2):
    id = i - 2
    toado = [int(lines[i].split(" ")[0]), int(lines[i].split(" ")[1])]
    thetich = int(lines[i].split(" ")[2])
    trongluong = int(lines[i].split(" ")[3])
    order = Order(id, toado, thetich, trongluong, 0)
    order_list.append(order)
  
  initialize_state(order_list, M)
  
  print_order_list(order_list)
  print("Lượng giá = ", ham_luong_gia(order_list))

  final_state = hill_climbing_search(order_list, M)
  print("Final List Order is: ")
  print_order_list(final_state[0])
  print("Final Min is: ")
  print(final_state[1])
  write_result(final_state[0])





if __name__ == "__main__":
    main()