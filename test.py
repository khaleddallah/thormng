#code to parse ROS log file and get some information from them


import re
import sys,os
import json
import cPickle as pickle





file_name = sys.argv[1]
out_file_name = sys.argv[1]+".out"
count_file_name = sys.argv[1]+".count"
sort_file_name = sys.argv[1]+".sort"
with open(file_name,'r+') as handfile :
	hand = handfile.readlines()

found=0
#get list of lines
##hand = list(handfile)



new_data=[]
essen=dict()
essen2=[]
sort=dict()
sort2=[]
for i in range(len(hand)):
		print(i)
		mhm = re.findall('\$(.*)', hand[i])
		if (len(mhm) > 0)  :
			new_data.append("$"+mhm[0][:-4]+"\n")
			found=found+1
			print("$")

		mhm2 = re.findall('\#(.*)', hand[i])
		if (len(mhm2) > 0)  :
			new_data.append("#"+mhm2[0][:-4]+"\n")
			found=found+1
			print("#")

		mhm3 = re.findall('\@(.*)', hand[i])
		if (len(mhm3) > 0)  :
			new_data.append("@"+mhm3[0][:-4]+"\n")
			found=found+1
			print("@")

count_sort=1
for j in range(len(new_data)):
	if new_data[j]  in essen:
		essen[new_data[j]]+=1
	else :
		essen[new_data[j]]=1
		#sort[count_sort]=new_data[j]
		sort2.append(str(str(count_sort)+" >> "+new_data[j]+"\n"))
		count_sort+=1


for i in essen.keys() :
	essen2.append(str(i+" >> "+str(essen[i])+"\n\n"))


#print (json.dumps(sort))
print("=============================================")

with open(out_file_name, 'w+') as wfile:
	wfile.writelines(new_data)

with open(count_file_name,'w+') as count :
	count.writelines(essen2)

with open(sort_file_name,'w+') as sortf :
	sortf.writelines(sort2)