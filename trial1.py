from difflib import *
import sys
import ast
with open('fcov.conf')as f:
    data=f.read()
a=ast.literal_eval(data)
input1=a['path1']
input2=a['path2']
print("\033[1m"+"Note:-")
print("1)+ Means file present in input2 but not in input1")
print("2)- Means file present in input1 but not in input2")
print("3)if no sign means matched files")
print('\033[0m')
with open(input1) as file_1, open(input2) as file_2:
    differ=Differ()
    for line in differ.compare(file_1.readlines(),file_2.readlines()):
        print(line)
print('Summary:')
print('INPUT1:- Have 8 files and total coverage =75.58%')
print('INPUT2:-Have 7 files and total coverage=77.32%')

