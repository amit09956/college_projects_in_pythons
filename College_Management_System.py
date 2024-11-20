
students = {}  
courses = {}   


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    department = input("Enter Department: ")
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = {
            'name': name,
            'age': age,
            'department': department,
            'courses': []
        }
        
        print(f"Student {name} added successfully!")


def view_students():
    if not students:
        print("No students available.")
    else:
        print("\nStudent Details:")
        for student_id, details in students.items():
            print(f"ID: {student_id}\n Name: {details['name']}\nAge: {details['age']}\n "
                  f"Department: {details['department']}\n Courses: {', '.join(details['courses'])}")

 
def remove_student():
    student_id = input("Enter Student ID to remove: ")
    if student_id in students:
        del students[student_id]
        print("Student removed successfully")
    else:
        print("Student ID not found")

 
def add_course():
    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")
    if course_id in courses:
        print("Course ID already exists")
    else:
        courses[course_id] = course_name
        print(f"Course {course_name} added successfully")


def view_courses():
    if not courses:
        print("No courses available.")
    else:
        print("\nAvailable Courses:")
        for course_id, course_name in courses.items():
           print(f"ID: {course_id}, Name: {course_name}")

    
def remove_course():
    course_id = input("Enter Course ID to remove: ")
    if course_id in courses:
        del courses[course_id]
        print("Course removed successfully!")
    else:
        print("Course ID not found!")

def assign_course():
    student_id = input("Enter Student ID: ")
    course_id = input("Enter Course ID: ")
    if student_id not in students:
        print("Student ID not found!")
    elif course_id not in courses:
        print("Course ID not found!")
    else:
        students[student_id]['courses'].append(courses[course_id])
        print(f"Course {courses[course_id]} assigned to {students[student_id]['name']}!")


def display_all():
    print("\n--- College Management System Information ---")
    view_students()
    view_courses()



while True:
    print("\n--- College Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Add Course")
    print("5. View Courses")
    print("6. Remove Course")
    print("7. Assign Course to Student")
    print("8. Display All Information")
    print("9. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        add_course()
    elif choice == '5':
        view_courses()
    elif choice == '6':
        remove_course()
    elif choice == '7':
        assign_course()
    elif choice == '8':
        display_all()
    elif choice == '9':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")