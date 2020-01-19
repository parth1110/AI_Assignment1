#conditional statements which are in use to solve this problem:
a="I am Human Being."
b="Good graders study well."
c="Every human does not study well."
x="Is every human good grader?."  # To check this statement
#boolean values are:
a_truth_value=0
b_truth_value=0
c_truth_value=0
x_truth_value=0
x_truth_values=[]

answer=1   #list to store truth values.
a_truth_value=0
for a_truth_value in range(2):
    b_truth_value=0
    for b_truth_value in range(2):             #generating truth table
        c_truth_value=0
        for c_truth_value in range(2):
            x_truth_value=0
            for x_truth_value in range(2):
                answer=((not((a_truth_value)and(b_truth_value and c_truth_value ))) or (x_truth_value))  #Logic.
                x_truth_values.append(bool(answer))
                x_truth_value+=1
            c_truth_value+=1
        b_truth_value+=1
    a_truth_value+=1

for t in x_truth_values:
    answer*=t #to access elements of list.
    print(t)
    
print(x)    #to check this statement.    
if(answer==0):
    print("ANSWER IS NO\n")     #condition of answers.
elif(answer==1):
    print("ANSWER IS YES\n")
    