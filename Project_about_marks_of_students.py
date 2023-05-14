no_of_student = int(input("enter the number of student: ")) # number of student
subject = input("enter the name of subject: ") # name of subjecf
count = 1 # counter for loop
count1 = 1 # counter for number of student in type subject lab
count2 = 1 # counter for number of student in type subject theorm
percentage_lab = 0 
percentage_theorm = 0
while count <= no_of_student:
    type_of_subject = input("enter the type of subject lab or theorm: ") # type of subject if lab or theor
    if type_of_subject == "lab":
        score1 = int(input("enter the score practical: ")) # practical
        score2 = int(input("enter the score mid_term: ")) # mid_term
        score3 = int(input("enter the score final: ")) # final
        mark_renge = score1 + score2 + score3 # total for all marks in lab
        if mark_renge >=0 and mark_renge <=39:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade fail")
        elif mark_renge >=40 and mark_renge <=59:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade pass")
        elif mark_renge >= 60 and mark_renge <= 79:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade good")
        elif mark_renge >= 80 and mark_renge <=89:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade very Good")
        elif mark_renge >=90 and mark_renge <=100:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade Excellent")
        percentage_lab = percentage_lab + mark_renge 
        count1 += 1
    elif type_of_subject == "theorm":
        score11 = int(input("enter the score practical: ")) # practical
        score22 = int(input("enter the score mid_term: ")) # mid_term
        score33 = int(input("enter the score final: ")) # final
        mark_renge2 = score11 + score22 + score33 # total for all marks in theorm
        if mark_renge2 <= 75:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade fail")
        elif mark_renge2 >= 76 and mark_renge2 <= 97:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade pass")
        elif mark_renge2 >= 98 and mark_renge2 <=119:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade Good")
        elif mark_renge2 >= 120 and mark_renge2 <= 134:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade Very Good")
        elif mark_renge2 >= 135 and mark_renge2 <= 150:
            print(f"the subject: {subject}\n the course: {type_of_subject}\n you Grade Excellent")
        percentage_theorm = percentage_theorm + mark_renge2
        count2 += 1
    else: 
        print(f"this type of subject not found in this program please try again")
        break
    count = count + 1
average1 = percentage_lab / count1
average2 = percentage_theorm / count2
re = input("report press r: ")
if re == "r":
    print(f" Number of student: {no_of_student}\n percentage lab: {average1}%\n"
          f" percentage theorm: {average2}%")
    print(f"thank you")
else:
    print("Finshed")
