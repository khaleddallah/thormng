#code to parse (pkg list) and get ros_kinetic* and put them in single line


'''
import re
x="[32m[DEBUG] [1527453654.360824329, 36.486000000]: void THORMANG3OnlineWalking::start()[0m"
mhm = re.findall('.*?\]:(.*\))', x)
print mhm
mhm=mhm[0]
print ("-----")
mhm = mhm + '\n'
print (mhm)
print ("=====")
mhm = mhm[:-1]
print (mhm)
'''
import re
import sys

file_name = sys.argv[1]



with open(file_name,'r+') as handfile :
	hand = handfile.readlines()

print ('len(hand)='+str(len(hand)))
new_data=['']*len(hand)
found=0 
for i in range(len(hand)):
	mhm = re.findall('^(ros-kinetic.*)/.*',hand[i])
	if (len(mhm)>0):
		new_data[found]=mhm[0]+' '
		found+=1
		print mhm[0]



print len('len(new_data)='+str(len(new_data)))
with open(file_name+"3", 'w+') as wfile:
	wfile.writelines( new_data )