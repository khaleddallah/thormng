#parse log.sort files and get differents between log.sort files
import re
import sys

#get files path
file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
file_name3 = sys.argv[3]
file_sort = sys.argv[4]
file_out = sys.argv[5]

#handle filse an put them in list
with open(file_name1,'r+') as handfile1 :
	hand1 = handfile1.readlines()

with open(file_name2,'r+') as handfile2 :
	hand2 = handfile2.readlines()

with open(file_name3,'r+') as handfile3 :
	hand3 = handfile3.readlines()

with open(file_sort,'r+') as sortfile :
	imp = sortfile.readlines()


#put all codes of three files in single list (codes)
hand=hand1+hand2+hand3


#clean imp data
impclean=[]
for i in range(len(imp)):
	mhm=re.findall('.*\>\>\s[$,#,@](.*)',imp[i])
	if (len(mhm)>0):		
		impclean.append(mhm[0])
		print(str(i)+'>> '+mhm[0])
print(len(impclean))
print("==========================================================")


#loop on one of sort log file (imp)
output=[]
temp_out=[]
found=0
#flag to enable parsing body of function
k=-1
for i in range(len(impclean)):
	print(impclean[i])
	#search about function in codes
	for j in range(len(hand)):
		#when flag of body parsing on
		if(k>=0):
			if(re.search('{',hand[j].strip())):
				k+=1
				temp_out.append(hand[j])
			elif(re.search('}',hand[j].strip())):
				k-=1
				temp_out.append(hand[j])
				if(k<=0):
					#turn flag off
					k=-1
					#add it to (output) list 
					output=output+temp_out+['\n\n\n']
			else:
				temp_out.append(hand[j])

		if(impclean[i].strip()==hand[j].strip()):
			#parse its body
			found+=1
			#clean temp_out
			temp_out=[]
			#append it definiation
			temp_out.append(hand[j])
			#turn flag on
			k=0

			



 
#write (output) list to file
with open(sys.argv[5], 'w+') as outfile:
	outfile.writelines(output)



#python /home/rv/thormng/src/getfunc.py /home/rv/thormng/src/ROBOTIS-THORMANG-MPC/thormang3_walking_module/src/thormang3_online_walking.cpp /home/rv/thormng/src/ROBOTIS-THORMANG-MPC/thormang3_walking_module/src/walking_module.cpp /home/rv/thormng/src/ROBOTIS-THORMANG-MPC/thormang3_balance_control/src/thormang3_balance_control.cpp /home/rv/dbg-all-with-once/ob.sort /home/rv/thormng/src/listFunction