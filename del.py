#code to delete ROS_DEBUG_* from c++ code 
import re
import sys

file_name = sys.argv[1]



with open(file_name,'r+') as handfile :
	hand = handfile.readlines()

found=0
deleted=0

new_data=['']*len(hand)
for i in range(len(hand)):
	mhm = re.findall('^ROS_DEBUG_.*', hand[i])
	if len(mhm)>0 :
		deleted+=1
		continue
		
	else :
		new_data[found]=hand[i]
		found+=1

print (deleted)
print("=============================================")
with open(file_name, 'w') as wfile:
	wfile.writelines( new_data )