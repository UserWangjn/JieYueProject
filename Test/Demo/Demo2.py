import csv
import os
file_path = os.path.abspath('.'+'\\data\\user_info.csv')
#print(file_path)
datas = csv.reader(open(file_path,'r'))
for data in datas:
	print(data[1][0])

print(datas)
