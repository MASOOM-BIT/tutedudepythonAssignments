#Creates a dictionary where student names are keys and their marks are values.

student_dict = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}
#Asks the user to input a student's name.

Student_name = input("Enter student Name : ")

if Student_name in student_dict:
    print(f'{Student_name} Marks is {student_dict[Student_name]}')
else:
    print('Student Not Found')