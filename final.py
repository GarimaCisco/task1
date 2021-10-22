from configparser import ConfigParser
from difflib import *
import sys
import ast
def counting(filename):
    count = 0
    with open(filename, 'r') as f:

        for line in f:

            if (line.startswith('/')):

                count = count + 1

    return count
def percentage(filename):


    per =""

    with open(filename, 'r') as f:
        for line in f:
            if(line.startswith('Total Coverage')):
                per="".join(line)
    return (per.split()[-1].split("%")[0])


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

file='config.init'
config=ConfigParser()
config.read(file)
count1=counting(input1)
count2=counting(input2)
diff_files=count1-count2
code_coverage1_per=percentage(input1)
code_coverage2_per=percentage(input2)
diff_coverage=float(code_coverage1_per)-float(code_coverage2_per)
config.set('input1','no_of_files',str(count1))
config.set('input2','no_of_files',str(count2))
config.set('input1','total_coverage_percentage',code_coverage1_per)
config.set('input2','total_coverage_percentage',code_coverage2_per)
config.set('difference_in_files','difference_in_no_of_files',str(diff_files))
config.set('difference_in_files','difference_in_coverage',str(diff_coverage))
with open(file,'w')as configfile:
    config.write(configfile)
print('Summary')
print(config['input1'])
print(dict(config.items('input1')))
print(config['input2'])
print(dict(config.items('input2')))
print(config['difference_in_files'])
print(dict(config.items('difference_in_files')))
if(diff_coverage<0):
    print("Input 2 file is having more coverage rate compare to Input1 file by:")
    print((diff_coverage*-1))
elif  (diff_coverage>0):
    print("Input 1 file is having more coverage rate compare to Input2 file by:")
    print((diff_coverage))
else:
    print("Both are having same coverage")
