"""
version 1.0
"""
import xlwt #导入xlwt工作表处理模块

dict1 = {"姓名":"成绩"} #创建字典

print("正在初始化程序……")
name = mark = n = total = 0 #初始化变量

#输入学生姓名及成绩
print("开始输入学生成绩，在姓名或成绩处输入-1完成输入")

while 1:
    n += 1
    name = input("请输入第%d位学生姓名：" %n) #输入学生姓名
    mark = eval(input("请输入第%d位学生成绩：" %n)) #输入学生成绩
    dict1[name] = mark #将学生姓名及成绩导入字典
    total = total + mark 
    if name == "-1" or mark == -1:
        break
print("共输入%d名学生成绩，正在计算平均分……" %n)
average = total/(n-1) #计算平均分
dict1["平均分"]=average
del dict1["-1"]

#生成xls工作表
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet("sheet1",cell_overwrite_ok=True)

#向工作表逐个导入字典键值对
print("正在填充工作表……")
print("]---------------------------[")
a = 0
for k in dict1.keys(): #遍历字典keys
    sheet1.write(a,0,k) #将keys写入表格sheet1 A列
    a += 1
    pass
a = 0
for v in dict1.values(): #遍历字典values
    sheet1.write(a,1,v) #将values写入表格sheet1 B列
    a += 1
    pass

#保存工作表至同根目录
print("正在保存工作表……",end="  ")
print("创建xls文件……")
workbook.save("report.xls")

print("-已在目录下创建report.xls文件-")
