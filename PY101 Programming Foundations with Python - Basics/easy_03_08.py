# input: 3 numbers as scores
# output: string 'A', 'B', 'C' 'D', 'F' based on average scores as
#         below:
#           90 <= score <= 100: 'A'
#           80 <= score < 90: 'B'
#           70 <= score < 80: 'C'
#           60 <= score < 70: 'D'
#           0 <= score < 60: 'F'
# Test Cases:
#   print(get_grade(95, 90, 93) == "A")      # True
#   print(get_grade(50, 50, 95) == "D")      # True
# Data Structure and Algorithm:
#   a. initialize average score = average of three scores
#   b. Check average:
#           if greater than equal to 0 and less than 60
#               return 'F'
#           if greater than equal to 60 and less than 70
#               return 'D'
#           if greater than equal to 70 and less than 80
#               return 'C'
#           if greater than equal to 80 and less than 90
#               return 'B'
#           else
#               return 'A'


# def get_grade(score1, score2, score3):
    # average_score = (score1 + score2 + score3) / 3
    # if average_score >= 0 and average_score < 60:
        # return 'F'
    # elif average_score >= 60 and average_score < 70:
        # return 'D'
    # elif average_score >= 70 and average_score < 80:
        # return 'C'
    # elif average_score >= 80 and average_score < 90:
        # return 'B'
    # else:
        # return 'A'

def get_grade(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3

    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True