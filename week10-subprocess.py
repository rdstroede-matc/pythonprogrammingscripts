#!/usr/bin/env python3
import subprocess
#1
myProc = subprocess.run(['ps','-axco', 'command'], stdout=subprocess.PIPE)
#2
myProcString = myProc.stdout.decode()
myProcList = myProcString.split('\n')
#3
print("Length: ", len(myProcList))
print()
for i in myProcList:
	print(i)


