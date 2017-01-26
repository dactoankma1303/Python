import random
print('|------------------------------------------------------|')
print('|       Chao mung ban den voi tro choi doan so         |')
print('|       May tinh se chon ngau nhien mot so tu 1--> 100 |')
print('|       Ban hay tim ra so do                           |')
print('|       Chuc ban thanh cong ^^!                        |')
print('|------------------------------------------------------|')
print('                                                        ')
print('|------------------------------------------------------|')
print('| Nhap ten cua ban sau do nhan  Enter  de tiep tuc     |')

myName = raw_input('>> ')


def timso():
  print('| Hi, ' + myName + ',ban co 10 lan doan               ')
  solandoan = 0
  sobimat = random.randint(1,101)
  while solandoan <10:
   print('Ban doan so may :') 
   so = input('>> ')
   so = int(so)
   solandoan += 1
      
   if so in range(1,101):
       if so < sobimat:
         print('So ban doan nho hon roi.')
       elif so > sobimat:
         print('So ban doan lon hon roi.')
       else: break
   else:
       print('Ban phai nhap so trong khoang 1 --> 100')
      
  if so == sobimat:
   print('Ban doan dung roi ! Ban mat ' + str(solandoan) + " lan doan de tim ra so " + str(sobimat) + " !")
  else:
   print('Ban doan qua so lan roi. Con so can tim la ' + str(sobimat) + "")
 
timso()
print('---------------------------------------------------------')
print('Nhap so khac 0 de choi tiep / Nhap so 0 de thoat tro choi')
choice = int(raw_input('Lua chon cua ban >> '))
while choice != 0 :
     if choice == 0 :
         break
     elif choice !=0 :
         timso()
     print('---------------------------------------------------------')
     print('Nhap so khac 0 de choi tiep / Nhap so 0 de thoat tro choi')
     choice = int(raw_input('Lua chon cua ban >>  '))
print('Tam biet ! ')


    
        
