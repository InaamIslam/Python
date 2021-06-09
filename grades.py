# Create a new python file. 
# In that file create a program that works out 
# a grade based on marks with the use of functions.
# The program should take the students name, 
# Homework(/25) score, 
# Assessment(/50) 
# score and Final Exam(/100) score as inputs, 
# and output their name and final ICT grade as a percentage.
# Stretch goal: 
# Include grade boundaries such that the 
# program also outputs a grade for the student (A, B, etc.)

def grades(name, homework_score, assessment_score, final_exam_score):
    final_ict_score = (homework_score + assessment_score + final_exam_score)
    percent = (final_ict_score / 175) * 100
    return round(percent)

name = str(input("Enter your name: "))
homework_score = int(input("Enter your homework score: "))
assessment_score = int(input(" Enter your assessment score: "))
final_exam_score = int(input("Enter your final exam score: "))

result = grades(name, homework_score, assessment_score,final_exam_score)

print(f'{name} achieved a final score of {result}%')

# SO FAR THIS WORKS, BUT REQUIRES ADDITIONS 
# ADD LIMITS SO THAG ONLY THE APPROPRIATE AMOUNTS CAN BE INCLUDED
# ADD GRADING
# RUN TESTS

