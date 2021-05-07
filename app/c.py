
def try1(text):
        
        
        if text=="hey":
            return "Hi"
        #else:
                #return "Gazala"
        if text=="what's the lecture schedule for computers dept?":
        	text=comp()
        	e=str(text)
        	text="\nSchedule of Computer department is as follows:"+"<br>"+e
        	return text
        if text=="what's the lecture schedule for IT dept?":
        	text1=IT()
        	e1=str(text1)
        	text1="Schedule of IT department is as follows:"+"<br>"+e1
        	return text1
        if text=="who are all the faculties of computers dept?":
        	text2=faculties()
        	e2=str(text2)
        	text2="faculties of Computers are:"+"<br>"+e2
        	return text2
        	#return
        if text=="who are all the faculties of IT dept?":
        	text2=facultiesIT()
        	e2=str(text2)
        	text2="faculties of IT are:"+"<br>"+e2
        	return text2
        	#return
        if text=="what's my attendence Percentage?":
        	try1.flag+=1
        	return "Please tell me Your RollNo and Name."
        if try1.flag==1:
        	try1.flag=0
        	rollno=text
        	s=str(rollno)
        	rollno=s[0]
        	name=s[1]
        	ans=attendence(rollno,name)
        	ans=str(ans)
        	e2="Your Attendence Percentage is:"+ans
        	return e2
        if text=="what's IA Time Table for computers department?":
        	text5=timetable()
        	return text5
        if text=="what's IA Time Table for IT department?":
        	text5=timetableIT()
        	return text5

try1.flag=0  
 
def comp():
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/student_db?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.lectures
	oo=record.find_one({"dept":"computers","mon":"CC"})
	oo.pop('_id')
	oo.pop('dept')
	result=' '
	for key,val in oo.items():
		#print(val[0])

		result=result+key+":"+val[0]+"\t"+val[1]+"<br>" #first element

	
	return result
def IT():
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/student_db?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.lectures
	oo=record.find_one({"dept":"IT","mon":"FE"})
	oo.pop('_id')
	oo.pop('dept')
	result=' '
	for key,val in oo.items():
		#print(val[0])

		result=result+key+":"+val[0]+"\t"+val[1]+"<br>" #first element

	return result
def faculties():
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/chatbot?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.faculties
	
	oo=list(record.find({"dept":"computers"},{"name":1}))
	list1=[]
	for i in range(0,len(oo)):
		oo1=oo[i]['name']
		list1.append(oo1)
	result=''
	for i in list1:
		result=result+i+"<br>"

	return result
def facultiesIT():
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/chatbot?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.faculties
	
	oo=list(record.find({"dept":"IT"},{"name":1}))
	list1=[]
	for i in range(0,len(oo)):
		oo1=oo[i]['name']
		list1.append(oo1)
	result=''
	for i in list1:
		result=result+i+"<br>"

	return result
def attendence(rollno,name):
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/chatbot?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.Studentinfo
	oo=record.find_one({"rollno":rollno},{"attendence":1})
	oo.pop('_id')
	oo1=oo['attendence']
	return oo1
def timetable():
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/chatbot?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.Exam
	#print(record.find_one({"dept":"computers"},{"subject":1}))
	oo=record.find_one({"dept":"computers"},{"subject":1})
	oo.pop('_id')
	print('oo:',oo)
	all_sub=oo['subject']
	print('all_sub:',all_sub)
	result_str=''
	for i in all_sub:
			result_str=result_str+"DATE:"+i['Date']+"\t"+"SUBJECT:"+i['subjecct']+"\t"+"TIME:"+i["Time"]+"<br>"
	
	return result_str
def timetableIT():
	from pymongo import MongoClient
	client =MongoClient("mongodb+srv://Gazala:Gazala%40123@cluster0.nhjog.mongodb.net/chatbot?retryWrites=true&w=majority")
	db = client.test
	db=client.get_database('chatbot')
	record=db.Exam
	#print(record.find_one({"dept":"computers"},{"subject":1}))
	oo=record.find_one({"dept":"IT"},{"subject":1})
	oo.pop('_id')
	print('oo:',oo)
	all_sub=oo['subject']
	print('all_sub:',all_sub)
	result_str=''
	for i in all_sub:
			result_str=result_str+"DATE:"+i['Date']+"\t"+"SUBJECT:"+i['subjecct']+"\t"+"TIME:"+i["Time"]+"<br>"
	
	return result_str
