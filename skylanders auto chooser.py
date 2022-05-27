from hashlib import new
from mailbox import linesep
import serial.tools.list_ports
import msvcrt
import sys
import os

#name of command that you will schedule
autocommandVarName = "yourcommandhere"

#if its a file path do folder/file
#if its empty, it will ask you for file name. can input it here 
#to save time (must update if file name changes)
filename = ""

#rfid tags and their corresponding auto command groups
Cynder = ["66AADCA4", "thirtyBallAuto(),"]
DoubleTrouble = ["F6413CF6", "climbOutOfField()"]
LegendarySlamBam = ["A48B4C24", "knockOverOtherRobot()"]
Bouncer = ["6224FE67", "breakDown()"]
Swarm = ["76247EE1", "hackOtherRobots()"]
ShroomBoom = ["04E82919", "regularAuto()"]

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []


for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))
while True:
	val = input("Select Port: COM")
	if(val.isnumeric()):
		break;
	else:
		print("this isnt a number!")

if not filename:
	while True:
		try:
			filenametwo = input("enter file name: ")
			f = open(filenametwo, "r")
			f.close()
			filename = filenametwo
			break
		except:
			print("file doesnt exist!")

print("press any key to exit the program")
newVal = "COM" + str(val)

for x in range(0, len(portList)):
    if portList[x].startswith("Com" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])



serialInst.baudrate = 9600
serialInst.port = newVal #"COM4" #portVar dont know why portVar doesnt work
serialInst.open()
# Python Program to Print Lines
# Containing Given String in File

# input file name with extension

# using try catch except to
# handle file not found error.

# entering try block

# Python Program to Print Lines
# Containing Given String in File

# input file name with extension

# using try catch except to
# handle file not found error.

# entering try block
try:

	# opening and reading the file
	file_read = open(filename, "r")

	# asking the user to enter the string to be
	# searched
	text = autocommandVarName + " ="
	textTwo = autocommandVarName + "= "
	textThree = autocommandVarName + "="
 

	# reading file content line by line.
	lines = file_read.readlines()

	new_list = []
	countList = []
	idx = 0
	count = 0

	# looping through each line in the file
	for line in lines:
		count = count+1
		# if line have the input string, get the index
		# of that line and put the
		# line into newly created list
		if text in line or textTwo in line or textThree in line:
			new_list.insert(idx, line)
			countList.insert(idx, count)
			idx += 1

	# closing file after reading
	file_read.close()

	# if length of new list is 0 that means
	# the input string doesn't
	# found in the text file
	if len(new_list)==0:
		print("\n\"" +text+ "\" is not found in \"" +filename+ "\"!")
	elif len(new_list) > 1:
		print("\n\You shouldnt be setting " + autocommandVarName + " more than once!")
	else:
		print(new_list[0])
		print(countList[0])
# entering except block
# if input file doesn't exist
except:
    print("\nThe file doesn't exist!")
data = ""
while True:
	if serialInst.in_waiting:
		packet = serialInst.readline()
		newVal = str(packet.decode('utf')).strip()
		lineSegment = ""
		# with is like your try .. finally block in this case
		with open(filename, 'r') as file:
		# read a list of lines into data
			data = file.readlines()

		# now change the 2nd line, note that you have to add a newline
		if newVal == LegendarySlamBam[0]:
        	 lineSegment = LegendarySlamBam[1]
		
		elif newVal == Cynder[0]:
			lineSegment = Cynder[1]

		elif newVal == DoubleTrouble[0]:
			lineSegment = DoubleTrouble[1]

		elif newVal == Bouncer[0]:
			lineSegment = Bouncer[1]

		elif newVal == Swarm[0]:
			lineSegment = Swarm[1]

		elif newVal == ShroomBoom[0]:
			lineSegment = ShroomBoom[1]
     
		data[countList[0]-1] = autocommandVarName + " = " + lineSegment + "\n"
		print(countList[0])

		# and write everything back
		with open(filename, 'w') as file:
			file.writelines( data )