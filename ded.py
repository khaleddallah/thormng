import re
import sys

file_name = sys.argv[1]



with open(file_name,'r+') as handfile :
	hand = handfile.readlines()

found=0
#get list of lines
##hand = list(handfile)

skip=0
mod=''
out=0


new_data=['']*len(hand)
for i in range(len(hand)):
	#new_data[i]=hand[i]
	if skip==1 :
		if (out==5):
			new_data[i]=hand[i]
			skip=0
			mod=''
			out=0
		if (re.search('[\s]*\{[\s]*',hand[i])):
			new_data[i]=mod
			skip=0
			mod=''
			out=0
		else:
			new_data[i]=hand[i]
			out=out+1
			continue



	else:
		new_data[i]=hand[i]
		#delete plus spaces
		##hand[i] = hand[i].rstrip()

		#find line like "void Onli::imuD(Imu::ConstPtr &msg)"
		#mhm = re.findall('[A-z,0-9]+\s([A-z,0-9]+::[~,A-z,0-9]+\(.*)', hand[i])
		mhm = re.findall('^([\s,A-z,0-9]+::[~,A-z,0-9,\s]+\(.*)', hand[i])

		if (len(mhm) > 0)  :
			if mhm[0][-1]==';':
				continue

			#if found mhm print it 
			print (str(found),"#",str(i),">>",mhm[0])
			
			#write plus line then type ("dbg_pub(" + NameOfFunc + ");"
			
			#handfile.write('\n'+'dbg_pub("'+mhm[0]+'");')
			mod='  '+'{'+'\n'+'ROS_DEBUG_ONCE("'+mhm[0]+'");'+'\n' 
			found=found+1
			skip=1




print("=============================================")
with open(file_name, 'w') as wfile:
	wfile.writelines( new_data )