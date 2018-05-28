import re
x="[32m[DEBUG] [1527453654.360824329, 36.486000000]: void THORMANG3OnlineWalking::start()[0m"
mhm = re.findall('.*?\]:(.*\))', x)
print mhm