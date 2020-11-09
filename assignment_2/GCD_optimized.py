#this is original operation

import time
import xlsxwriter

x = 42;
y = 8;
z = 0;
i = 0;

print("i\t x\t y\t x%y");

while(y!= 0):
  z = x % y;
  print(i, "\t", x, "\t", y, "\t", z);
  x = y;
  i = i + 1; 
  y = z;


workbook = xlsxwriter.Workbook('Optimized Program.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "Number of calculation")
worksheet.write(0, 1, "Processing Time(ms)")
row = 1

begin = time.time()
num=0

while (num < 10000):
  num = num + 1
  x = 42
  y = 8
  while (y!=0):
    z = x % y;
    x = y;
    i = i + 1; 
    y = z;

  end = time.time()
  t= (end - begin)*1000
  worksheet.write(row,1,t)
  worksheet.write(row,0,num)
  row+=1

workbook.close()
print("Total number of calculation: ",num)
print(f"Total processing time: {t}")

