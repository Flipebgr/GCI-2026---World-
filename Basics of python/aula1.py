score  = [10, 20 ,15 ,79, 12, 32] 
students_aproved = []

average = sum(score) / len(score) 
# sum is function for calculating the sum of the list 
# and len is function for calculating the length of the list
print(f"The average of the scores is {average}")

if average > 10:
    print("The average is greater than 10")
elif average < 10:
    print("The average is less than 10")
else: 
    print("The average is equal to 10")

i = 2
names_and_score_list = []
for i in range(i):
    name_of_student = input("Enter the name of the student: ")
    if name_of_student == "":
            print("The name of the student is empty")
            break
    score_of_student = float(input("Enter the score of the student: "))
    if score_of_student < 0 or score_of_student > 10: 
        print ("The score are is invalid, please insert a score between 0 and 10")
    else:
        names_and_score_list.append((name_of_student, score_of_student)) # The list append one value ot the following mode list = [(name1, score1), (name2, score2), (name3, score3)]
        # -> There is a list of list 
for name, score in names_and_score_list:
    if score >= 7:
        students_aproved.append((name, score))
    else:
        print(f"{name}is not approved with score {score}")



print(f"The students approver are: {students_aproved}")