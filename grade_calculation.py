import argparse 


def reformat(input):
	""" helper to turn old input file to csv """
	with open("my_grade.csv","w") as f:
		for line in open(input).read().split('\n'):
			line=line.strip().replace(" ",",")
			f.write(line)
			f.write('\n')
		f.close()
            
        

def calculate_grade(input):
	f=open(input).read()
	total=0.0
	for idx,line in enumerate(f.split("\n")[1:]):
		if not line: continue #mty line
		line=line.strip()
		assigment,grade,max_grade,percent=line.split(",")
		assert max_grade!=None,f"max grade is NULL for {assignment}"	
		assert grade!=None,f"grade is NULL for {assignment}"	
		assert percent!=None,f"percentage of grade is NULL {assignment}"	
		total+=(float(grade)/float(max_grade))*float(percent)
	return total 

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("-r","--reformat",action="store_true",help="reformat input file if file is space separated, see my_grade.txt")
	parser.add_argument("-i","--input",default="my_grade.csv",help="your grade file in csv")
	options=parser.parse_args()
	
	if options.reformat:
		reformat("my_grade.txt")
  
	grade=calculate_grade(options.input)
	print(f"Your final grade:{grade:.2f}")

