#program to read file content


import sys

#b=sys.argv[1];
def ipmatch():
	file = open("ip.txt","r")
	#file="ip.txt"
	new = file.readlines()
	for i in new:
		i=i.split()
		if sys.argv[1]==i[0]:
			print("yes")
			sys.exit()
		else:
			print("no")



def main():
	ipmatch();


if __name__ == '__main__':
	main()
