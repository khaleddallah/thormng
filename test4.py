#parse log.sort files and get differents between log.sort files
import re
import sys

#get files path
file_name1 = sys.argv[1]
file_name2 = sys.argv[2]


#handle filse an put them in list
with open(file_name1,'r+') as handfile :
	hand1 = handfile.readlines()

with open(file_name2,'r+') as handfile :
	hand2 = handfile.readlines()



new_data1=[]
for i in range(len(hand1)):
	if(sys.argv[3]=='divi'):
		new_data1.append(hand1[i])
	mhm = re.findall('.*\s\>\>\s(.*)',hand1[i])
	if (len(mhm)>0):
		new_data1.append(mhm[0])
print(len(new_data1))

new_data2=[]
for i in range(len(hand2)):
	if(sys.argv[3]=='divi'):
		new_data2.append(hand2[i])
	mhm = re.findall('.*\s\>\>\s(.*)',hand2[i])
	if (len(mhm)>0):
		new_data2.append(mhm[0])
print(len(new_data2))


divi=[]
same=[]
found=1
for i in range(len(new_data1)):
	if(new_data1[i] in new_data2):
		continue
	else:
		print(new_data1[i])
		divi.append(str(found)+" : "+new_data1[i]+'\n')
		found+=1

with open(sys.argv[3], 'w+') as wfile:
	wfile.writelines(divi)