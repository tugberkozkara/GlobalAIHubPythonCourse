#Homework-2
#CV application
#Create 5 dictionaries. Each dictionary should represent a CV.
#Create a CV containing the information of the 5 created people.
#Print the information on CVs created on the screen.

cv_1 = {'name':'Jane Bergham','jobtitle':'IOS Developer','yearsofexperience':'5','currentcompany':'Amazon','lastgradschool':'University of Waterloo'}
cv_2 = {'name':'Rob River','jobtitle':'Unity Developer','yearsofexperience':'3','currentcompany':'Ubisoft','lastgradschool':'University of British Columbia'}
cv_3 = {'name':'Amanda Riley','jobtitle':'Data Scientist','yearsofexperience':'3','currentcompany':'Udemy','lastgradschool':'University of California, Berkeley'}
cv_4 = {'name':'Craig Wiser','jobtitle':'ML Engineer','yearsofexperience':'4','currentcompany':'Oracle','lastgradschool':'Stanford University'}
cv_5 = {'name':'Wilma Claire','jobtitle':'Software Engineer','yearsofexperience':'7','currentcompany':'Google','lastgradschool':'Massachusetts Institute of Technology'}
cvs = (cv_1, cv_2, cv_3, cv_4, cv_5)

for i in cvs:
    for x in i:
        print(x, ':', i[x])
    print(" ")
