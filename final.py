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

def com(input1,input2):
    with open(input1,'r') as file1:
        with open(input2,'r') as file2:
            same=set(file1).intersection(file2)

            for line in same:
                if (line.startswith('/')):
                    print(line)

def diff(input1,input2):

    with open(input1,'r') as file1:
        with open(input2,'r') as file2:
            differ=set(file1).difference(set(file2))
            for x in differ:
                if(x.startswith('/')):
                    print(x)


input1="/Users/gargarg/Desktop/task1/input1_diff_coverage_final.summary"
input2="/Users/gargarg/Desktop/task1/input2_diff_coverage_final.summary"
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
print('Common files in both input files')
com(input1,input2)
print(config['input1'])
print(dict(config.items('input1')))
print('unique files in input1:')
diff(input1,input2)
print(config['input2'])
print(dict(config.items('input2')))
print('unique files in input2:')
diff(input2,input1)
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
