# final mark + course marl
total1 = 0.0
total2 = 0.0
total3 = 0.0
total4 = 0.0
total5 = 0.0
total6 = 0.0

# ABCDF
gradePoint1 = 0.0
gradePoint2 = 0.0
gradePoint3 = 0.0
gradePoint4 = 0.0
gradePoint5 = 0.0
gradePoint6 = 0.0

# gradecredit
gradecedit1 = 0.0
gradecedit2 = 0.0
gradecedit3 = 0.0
gradecedit4 = 0.0
gradecedit5 = 0.0
gradecedit6 = 0.0

# course
course1 = 0.0
course2 = 0.0
course3 = 0.0
course4 = 0.0
course5 = 0.0
course6 = 0.0

final1 = 0.0
final2 = 0.0
final3 = 0.0
final4 = 0.0
final5 = 0.0
final6 = 0.0

letter1 = "error"
letter2 = "error"
letter3 = "error"
letter4 = "error"
letter5 = "error"
letter6 = "error"

courseName1 = "course1"
courseName2 = "course2"
courseName3 = "course3"
courseName4 = "course4"
courseName5 = "course5"
courseName6 = "course6"

credit1 = 0.0
credit2 = 0.0
credit3 = 0.0
credit4 = 0.0
credit5 = 0.0
credit6 = 0.0

print("Welcome to Carlyon GPA Calculator\n")

while True:
    try:
        # input data 1
        courseName1 = str(input("\n\nEnter Course name: "))
        credit1 = float(input("\nEnter Credit: "))
        final1 = float(input("Enter Final exam mark: "))
        course1 = float(input("Enter Course mark: "))

        if (credit1 >= 0) and (credit1 <= 100) and (final1 >= 0) and (final1 <= 100) and (course1 >= 0) and (
                course1 <= 100):
            check = float("1")
        else:
            check = float("t")
        break

    except ValueError:
        print(
            "ERROR\nInvalid Inputted: \n1)Inputed mark is less than 0 or more than 100 \n2)Letters and characters were entered in the wrong area")
        continue

while True:
    try:
        # input data 2
        courseName2 = str(input("\n\nEnter Course name: "))
        credit2 = float(input("\nEnter Credit: "))
        final2 = float(input("Enter Final exam mark: "))
        course2 = float(input("Enter Course mark: "))
        # end
        # check2
        if (credit2 >= 0) and (credit2 <= 100) and (final2 >= 0) and (final2 <= 100) and (course2 >= 0) and (
                course2 <= 100):
            check = float("2")
        else:
            check = float("t")
        break
        # end
    except ValueError:
        print(
            "ERROR\nInvalid Inputted: \n1)Inputed mark is less than 0 or more than 100 \n2)Letters and characters were entered in the wrong area")
        continue

while True:
    try:
        # input data 3
        courseName3 = str(input("\n\nEnter Course name: "))
        credit3 = float(input("\nEnter Credit: "))
        final3 = float(input("Enter Final exam mark: "))
        course3 = float(input("Enter Course mark: "))
        # end
        # check3
        if (credit3 >= 0) and (credit3 <= 100) and (final3 >= 0) and (final3 <= 100) and (course3 >= 0) and (
                course3 <= 100):
            check = float("3")
        else:
            check = float("t")
        break
        # end
    except ValueError:
        print(
            "ERROR\nInvalid Inputted: \n1)Inputed mark is less than 0 or more than 100 \n2)Letters and characters were entered in the wrong area")
        continue

while True:
    try:
        # input data 4
        courseName4 = str(input("\n\nEnter Course name: "))
        credit4 = float(input("\nEnter Credit: "))
        final4 = float(input("Enter Final exam mark: "))
        course4 = float(input("Enter Course mark: "))
        # end
        # check4
        if (credit4 >= 0) and (credit4 <= 100) and (final4 >= 0) and (final4 <= 100) and (course4 >= 0) and (
                course4 <= 100):
            check = float("4")
        else:
            check = float("t")
        break
        # end
    except ValueError:
        print(
            "ERROR\nInvalid Inputted: \n1)Inputed mark is less than 0 or more than 100 \n2)Letters and characters were entered in the wrong area")
        continue

while True:
    try:
        # input data 5
        courseName5 = str(input("\n\nEnter Course name: "))
        credit5 = float(input("\nEnter Credit: "))
        final5 = float(input("Enter Final exam mark: "))
        course5 = float(input("Enter Course mark: "))
        # end
        # check5
        if (credit5 >= 0) and (credit5 <= 100) and (final5 >= 0) and (final5 <= 100) and (course5 >= 0) and (
                course5 <= 100):
            check = float("5")
        else:
            check = float("t")
        break
        # end

    except ValueError:
        print(
            "ERROR\nInvalid Inputted: \n1)Inputed mark is less than 0 or more than 100 \n2)Letters and characters were entered in the wrong area")
        continue

while True:
    try:
        # input data 6
        courseName6 = str(input("\n\nEnter Course name: "))
        credit6 = float(input("\nEnter Credit: "))
        final6 = float(input("Enter Final exam mark: "))
        course6 = float(input("Enter Course mark: "))
        # end
        # check6
        if (credit6 >= 0) and (credit6 <= 100) and (final6 >= 0) and (final6 <= 100) and (course6 >= 0) and (
                course6 <= 100):
            check = float("6")
        else:
            check = float("t")

        break
        # end
    except ValueError:
        print(
            "ERROR\nInvalid Inputted: \n1)Inputed mark is less than 0 or more than 100 \n2)Letters and characters were entered in the wrong area")
        continue

# cal per
course11 = course1 * 0.6
final11 = final1 * 0.4
course22 = course2 * 0.6
final22 = final2 * 0.4
course33 = course3 * 0.6
final33 = final3 * 0.4
course44 = course4 * 0.6
final44 = final4 * 0.4
course55 = course5 * 0.6
final55 = final5 * 0.4
course66 = course6 * 0.6
final66 = final6 * 0.4
# end

# cal total
total1 = course11 + final11
total2 = course22 + final22
total3 = course33 + final33
total4 = course44 + final44
total5 = course55 + final55
total6 = course66 + final66
# end


# cal gradePoint1
# gradePoint1  
if (total1 > 94) and (total1 <= 100):
    gradePoint1 = 4.00
    letter1 = "A+"
elif (total1 > 84) and (total1 <= 94):
    gradePoint1 = 3.75
    letter1 = "A"
elif (total1 > 79) and (total1 <= 84):
    gradePoint1 = 3.67
    letter1 = "A-"
elif (total1 >    74) and (total1 <= 79):
    gradePoint1 = 3.33
    letter1 = "B+"
elif (total1 > 69) and (total1 <= 74):
    gradePoint1 = 3.00
    letter1 = "B"
elif (total1 > 64) and (total1 <= 69):
    gradePoint1 = 2.75
    letter1 = "B-"
elif (total1 >  59) and (total1 <= 64):
    gradePoint1 = 2.67
    letter1 = "C+"
elif (total1 >  54) and (total1 <= 59):
    gradePoint1 = 2.33
    letter1 = "C"
elif (total1 > 49) and (total1 <= 54):
    gradePoint1 = 2.00
    letter1 = "C-"
elif (total1 > 44) and (total1 <= 49):
    gradePoint1 = 1.67
    letter1 = "D+"
elif (total1 > 39) and (total1 <= 44):
    gradePoint1 = 1.33
    letter1 = "D"
elif (total1 >= 0) and (total1 <= 39):
    gradePoint1 = 0.00
    letter1 = "F"

# gradePoint2
if (total2 > 94) and (total2 <= 100):
    gradePoint2 = 4.00
    letter2 = "A+"
elif (total2 > 84) and (total2 <= 94):
    gradePoint2 = 3.75
    letter2 = "A"
elif (total2 > 79) and (total2 <= 84):
    gradePoint2 = 3.67
    letter2 = "A-"
elif (total2 > 74) and (total2 <= 79):
    gradePoint2 = 3.33
    letter2 = "B+"
elif (total2 > 69) and (total2 <= 74):
    gradePoint2 = 3.00
    letter2 = "B"
elif (total2 > 64) and (total2 <= 69):
    gradePoint2 = 2.75
    letter2 = "B-"
elif (total2 >  59) and (total2 <= 64):
    gradePoint2 = 2.67
    letter2 = "C+"
elif (total2 >  54) and (total2 <= 59):
    gradePoint2 = 2.33
    letter2 = "C"
elif (total2 > 49) and (total2 <= 54):
    gradePoint2 = 2.00
    letter2 = "C-"
elif (total2 > 44) and (total2 <= 49):
    gradePoint2 = 1.67
    letter2 = "D+"
elif (total2 > 39) and (total2 <= 44):
    gradePoint2 = 1.33
    letter2 = "D"
elif (total2 >= 0) and (total2 <= 39):
    gradePoint2 = 0.00
    letter2 = "F"

# gradePoint3 
if (total3 > 94) and (total3 <= 100):
    gradePoint3 = 4.00
    letter3 = "A+"
elif (total3 > 84) and (total3 <= 94):
    gradePoint3 = 3.75
    letter3 = "A"
elif (total3 >   79) and (total3 <= 84):
    gradePoint3 = 3.67
    letter3 = "A-"
elif (total3 >    74) and (total3 <= 79):
    gradePoint3 = 3.33
    letter3 = "B+"
elif (total3 > 69) and (total3 <= 74):
    gradePoint3 = 3.00
    letter3 = "B"
elif (total3 > 64) and (total3 <= 69):
    gradePoint3 = 2.75
    letter3 = "B-"
elif (total3 >  59) and (total3 <= 64):
    gradePoint3 = 2.67
    letter3 = "C+"
elif (total3 >  54) and (total3 <= 59):
    gradePoint3 = 2.33
    letter3 = "C"
elif (total3 > 49) and (total3 <= 54):
    gradePoint3 = 2.00
    letter3 = "C-"
elif (total3 > 44) and (total3 <= 49):
    gradePoint3 = 1.67
    letter3 = "D+"
elif (total3 > 39) and (total3 <= 44):
    gradePoint3 = 1.33
    letter3 = "D"
elif (total3 >= 0) and (total3 <= 39):
    gradePoint3 = 0.00
    letter3 = "F"

# gradePoint4 
if (total4 > 94) and (total4 <= 100):
    gradePoint4 = 4.00
    letter4 = "A+"
elif (total4 > 84) and (total4 <= 94):
    gradePoint4 = 3.75
    letter4 = "A"
elif (total4 >   79) and (total4 <= 84):
    gradePoint4 = 3.67
    letter4 = "A-"
elif (total4 >    74) and (total4 <= 79):
    gradePoint4 = 3.33
    letter4 = "B+"
elif (total4 > 69) and (total4 <= 74):
    gradePoint4 = 3.00
    letter4 = "B"
elif (total4 > 64) and (total4 <= 69):
    gradePoint4 = 2.75
    letter4 = "B-"
elif (total4 >  59) and (total4 <= 64):
    gradePoint4 = 2.67
    letter4 = "C+"
elif (total4 >  54) and (total4 <= 59):
    gradePoint4 = 2.33
    letter4 = "C"
elif (total4 > 49) and (total4 <= 54):
    gradePoint4 = 2.00
    letter4 = "C-"
elif (total4 > 44) and (total4 <= 49):
    gradePoint4 = 1.67
    letter4 = "D+"
elif (total4 > 39) and (total4 <= 44):
    gradePoint4 = 1.33
    letter4 = "D"
elif (total4 >= 0) and (total4 <= 39):
    gradePoint4 = 0.00
    letter4 = "F"

# gradePoint5
if (total5 > 94) and (total5 <= 100):
    gradePoint5 = 4.00
    letter5 = "A+"
elif (total5 > 84) and (total5 <= 94):
    gradePoint5 = 3.75
    letter5 = "A"
elif (total5 >   79) and (total5 <= 84):
    gradePoint5 = 3.67
    letter5 = "A-"
elif (total5 >    74) and (total5 <= 79):
    gradePoint5 = 3.33
    letter5 = "B+"
elif (total5 > 69) and (total5 <= 74):
    gradePoint5 = 3.00
    letter5 = "B"
elif (total5 > 64) and (total5 <= 69):
    gradePoint5 = 2.75
    letter5 = "B-"
elif (total5 >  59) and (total5 <= 64):
    gradePoint5 = 2.67
    letter5 = "C+"
elif (total5 >  54) and (total5 <= 59):
    gradePoint5 = 2.33
    letter5 = "C"
elif (total5 > 49) and (total5 <= 54):
    gradePoint5 = 2.00
    letter5 = "C-"
elif (total5 > 44) and (total5 <= 49):
    gradePoint5 = 1.67
    letter5 = "D+"
elif (total5 > 39) and (total5 <= 44):
    gradePoint5 = 1.33
    letter5 = "D"
elif (total5 >= 0) and (total5 <= 39):
    gradePoint5 = 0.00
    letter5 = "F"

# gradePoint6
if (total6 > 94) and (total6 <= 100):
    gradePoint6 = 4.00
    letter6 = "A+"
elif (total6 > 84) and (total6 <= 94):
    gradePoint6 = 3.75
    letter6 = "A"
elif (total6 >   79) and (total6 <= 84):
    gradePoint6 = 3.67
    letter6 = "A-"
elif (total6 >    74) and (total6 <= 79):
    gradePoint6 = 3.33
    letter6 = "B+"
elif (total6 > 69) and (total6 <= 74):
    gradePoint6 = 3.00
    letter6 = "B"
elif (total6 > 64) and (total6 <= 69):
    gradePoint6 = 2.75
    letter6 = "B-"
elif (total6 > 59) and (total6 <= 64):
    gradePoint6 = 2.67
    letter6 = "C+"
elif (total6 > 54) and (total6 <= 59):
    gradePoint6 = 2.33
    letter6 = "C"
elif (total6 > 49) and (total6 <= 54):
    gradePoint6 = 2.00
    letter6 = "C-"
elif (total6 > 44) and (total6 <= 49):
    gradePoint6 = 1.67
    letter6 = "D+"
elif (total6 > 39) and (total6 <= 44):
    gradePoint6 = 1.33
    letter6 = "D"
elif (total6 >= 0) and (total6 <= 39):
    gradePoint6 = 0.00
    letter6 = "F"
else:
    message = "error"

# end


# cal gradecedit

gradecedit1 = gradePoint1 * credit1
gradecedit2 = gradePoint2 * credit2
gradecedit3 = gradePoint3 * credit3
gradecedit4 = gradePoint4 * credit4
gradecedit5 = gradePoint5 * credit5
gradecedit6 = gradePoint6 * credit6

# end

# cal totals

totalgradePoint = gradePoint1 + gradePoint2 + gradePoint3 + gradePoint4 + gradePoint5 + gradePoint6
totalCredit = credit1 + credit2 + credit3 + credit4 + credit5 + credit6
totalgradecedit = gradecedit1 + gradecedit2 + gradecedit3 + gradecedit4 + gradecedit5 + gradecedit6

# end

# cal GPA

gpacal = totalgradecedit / totalCredit
gpa = (gpacal * 100.0) / 100.0

# end

# cal honor

if (gpa >= 3.00) and (gpa <= 3.39):
    honor = "Honor roll achieved\nHonor: Cum laude"
elif (gpa >= 3.40) and (gpa <= 3.69):
    honor = "Honor roll achieved\nHonor: Magna cum laude"
elif (gpa >= 3.70) and (gpa <= 4.0):
    honor = "Honor roll achieved\nHonor: Summa cum laude"
else:
    honor = "No Honor roll achieved\nHonor:unqualified"

# end


# print

# rep1
print("\n\n", courseName1)

print("\nCredits: ", credit1)
print("Final exam: ", final1)
print("Course work: ", course1)

# new1
print("Final score: ", total1, " %")
print("Letter grade: ", letter1)
print("grade points: ", "{:.2f}".format(gradecedit1))

# rep2
print("\n\n", courseName2)

print("\nCredits: ", credit2, " %")
print("Final exam: ", final2)
print("Course work: ", course2)

# new2
print("Final score: ", total2, " %")
print("Letter grade: ", letter2)
print("grade points: ", "{:.2f}".format(gradecedit2))

# rep3
print("\n\n", courseName3)

print("\nCredits: ", credit3)
print("Final exam: ", final3)
print("Course work: ", course3)

# new3
print("Final score: ", total3, " %")
print("Letter grade: ", letter3)
print("grade points: ", "{:.2f}".format(gradecedit3))

# rep4
print("\n\n", courseName4)

print("\nCredits: ", credit4)
print("Final exam: ", final4)
print("Course work: ", course4)

# new4
print("Final score: ", total4, " %")
print("Letter grade: ", letter4)
print("grade points: ", "{:.2f}".format(gradecedit4))

# rep5
print("\n\n", courseName5)

print("\nCredits: ", credit5)
print("Final exam: ", final5)
print("Course work: ", course5)

# new5
print("Final score: ", total5, " %")
print("Letter grade: ", letter5)
print("grade points: ", "{:.2f}".format(gradecedit5))

# rep6
print("\n\n", courseName6)

print("\nCredits: ", credit6)
print("Final exam: ", final6)
print("Course work: ", course6)

# new6
print("Final score: ", total6, " %")
print("Letter grade: ", letter6)
print("grade points: ", "{:.2f}".format(gradecedit6))

# end

# total

print("\n\nTotal grade points: ", letter1, ", ", letter2, ", ", letter3, ", ", letter4, ", ", letter5, ", ", letter6)
print("Total grade points: ", "{:.2f}".format(gradecedit1), ", ",
      "{:.2f}".format(gradecedit2), ", ", "{:.2f}".format(gradecedit3), ", ", "{:.2f}".format(gradecedit4), ", ",
      "{:.2f}".format(gradecedit5), ", ", "{:.2f}".format(gradecedit6))
print("GPA", "{:.2f}".format(gpa))
print(honor)

#end#end