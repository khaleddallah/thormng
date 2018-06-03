#code to put ROS_DEBUG_* with real parameter and with get all mulit line pararmeter
import re
import sys

file_name = sys.argv[1]
arg = sys.argv[2]


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
			
			#get between ()
			b_new_param=re.findall(".*\((.+)\)",mod)
			#get first statement 
			b_new_name=re.findall("(.*)\(.*\)",mod)

			if len(b_new_param)>0:
				mod2='"'+b_new_name[0]+'("+'
				#strip in , 
				b_new_strip=b_new_param[0].split("+")
				print
				if (len(b_new_strip)>0):
					for h in range(len(b_new_strip)):
						if (h==len(b_new_strip)-1):
							x=b_new_strip[h].split(" ")
							#mod2+='std::string('+x[-1]+')+'+'")"'+')'
							mod2+='std::string('+x[-1]+')+'+'")"'+')'
						else:
							x=b_new_strip[h].split(" ")
							mod2+='std::string('+x[-1]+')+'
				else:
					mod2+=str("("+b_new_param[0]+")")
				new_data[i]='  '+'{'+'\n'+'ROS_DEBUG_STREAM('+mod2[:-1]+');'+'\n'

			else :
				mod2='"'+mod
				new_data[i]='  '+'{'+'\n'+'ROS_DEBUG_STREAM('+mod2+'");'+'\n'

			#new_data[i]='  '+'{'+'\n'+'ROS_DEBUG_STREAM('+mod2+'");'+'\n'
			found+=1
			skip=0
			mod=''
			out=0
		else:
			#add new param line (NEW) 
			mod = mod+hand[i][:-1]
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


		#if it a command 
		if (len(mhm) > 0)  :
			if mhm[0][-1]==';':
				continue

			#if found mhm print it 
			print (str(found),"#",str(i),">>",mhm[0])
			
			#write plus line then type ("dbg_pub(" + NameOfFunc + ");"
			
			#handfile.write('\n'+'dbg_pub("'+mhm[0]+'");')
			mod=mhm[0]
			found=found+1
			skip=1




print("=============================================")
print (found)
with open(file_name, 'w') as wfile:
	wfile.writelines( new_data )