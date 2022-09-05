#!/usr/bin/env python
# coding: utf-8

# In[41]:
"""
Lets say you are a teacher and you have different student record containing id of a student and the marks list in
each subject where different students have taken different number of subjects. All these record are in hard copy. You
want to enter all the data in computer and want to compute rhe average marks of each student and display.
"""

#write function to collect data
def getData():
    dict = {}
    while True:
        studentId = int(input("Enter student ID: "))
        marks = input("Enter marks for each subject separated by commas : ")
        addStudent = input('Enter "no" to quit, else other words to continue: ')
        
        #check if studentID has already been entered
        if studentId in dict:
            print(studentId, " already exists.")
        else:
            dict[studentId] = marks.split(",")
            
            #exit if user enters no
        if addStudent.lower() == "no":
            return dict


studentData = getData()


#fucntion to get average marks for each student
def getAvrg(dict):
    avrgMarks = {}
    for m in dict:
        mark = dict[m]
        i =0
        s= 0
        for L in range(len(mark)):
            s += int(L)
            i +=1 
            avrg = s/(len(mark))
        avrgMarks[m] = avrg
        
    return avrgMarks
            



average = getAvrg(studentData)




for m in average:
    print("Student", m, "got", average[m], "marks")





