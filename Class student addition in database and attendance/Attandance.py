import mysql.connector as sqlcon
conObject = sqlcon.connect(host = "localhost", user="root", passwd="your password here", database="name_of_the_database")
cursor1 = conObject.cursor()

day = int(input("Enter the day = "))
cursor1.execute(f"create table day{day}(roll_no integer(3), name varchar(20),status varchar(7))")
conObject.commit()

#students , balak
st2="""SELECT roll_no FROM name_of_table ORDER BY roll_no DESC LIMIT 1;"""
cursor1.execute(st2)
R = cursor1.fetchone()

for i in range(R[0]):
    rollNo = int(input("Enter the Roll no. = "))
    preStatus = input("Present / Absent = ")
    if preStatus=="P" or preStatus=="p":
        status="Present"
    else:
        status="Absent"

    st1="INSERT INTO day{} (roll_no, name, status) SELECT {}, name, '{}' FROM name_of_table WHERE roll_no = {}".format(day, rollNo, status, rollNo)
    cursor1.execute(st1)
    conObject.commit()
    
    

print("Thank You")    
cursor1.close()
conObject.close()