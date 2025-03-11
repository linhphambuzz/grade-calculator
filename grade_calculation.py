
def calculate_grade(input):
	f=open(input).read()
	total=0.0
	for idx,line in enumerate(f.split("\n")[1:]):
		if not line: continue #mty line
		line=line.strip()
		assigment,grade,max_grade,percent=line.split()
		assert max_grade!=None,f"max grade is NULL for {assignment}"	
		assert grade!=None,f"grade is NULL for {assignment}"	
		assert percent!=None,f"percentage of grade is NULL {assignment}"	
		total+=(float(grade)/float(max_grade))*float(percent)
	return total 

if __name__=="__main__":
	grade=calculate_grade("my_grade.txt")
	
	print(f"Your final grade:{grade:.2f}")

