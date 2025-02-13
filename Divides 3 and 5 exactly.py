N = int(input("number(จำนวนตัวเลข) : "))

x = []
for i in range (N): #วนลูปตามจำนวนเลข
  num = int(input("number : "))
  x.append(num) #ตรวจสอบเงื่อนไข

count3 = 0 #เอาไว้หาร 3
count5 = 0 #เอาไว้หาร 5

for i in x:
  if i % 3 == 0:
    count3 += 1
  if i % 5 == 0:
    count5 += 1

  print("หาร 3 ลง :",count3,"หาร 5 ลง :",count5)

