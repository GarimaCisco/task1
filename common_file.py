with open('input1_diff_coverage_final.summary','r') as file1:
    with open('input2_diff_coverage_final.summary','r') as file2:
        same=set(file1).intersection(file2)
same.discard('\n')
with open('common.txt','w') as file_out:
    for line in same:
        file_out.write(line)
~                             
