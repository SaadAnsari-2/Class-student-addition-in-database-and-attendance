import mysql.connector as mq
conObject=mq.connect(host = "localhost", user = "root", passwd = "your password here", database = "name_of_the_database")
cursor = conObject.cursor()
cursor.execute(f"create table name_of_table (roll_no integer(3), name varchar(20),section char(7), class integer(2))")
# balak
while True:
    roll_no = int(input("Enter the roll no. of student = "))
    name = input("Enter the name of student = ")
    section = input("Enter the section of student = ")
    std =int(input("Enter the standard of student = "))

    st = "insert into name_of_table (roll_no, name, section, class) values({},'{}','{}',{})".format(roll_no,name,section,std)
    cursor.execute(st)
    conObject.commit()
    print("Student details entered")
    x=input("PRESS any KEY to continue\nPRESS 'X' to exit the form ")
    if x=="X" or x=="x":
        break
    else:
        pass

print("Student list updated")