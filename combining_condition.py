gpa = float(input("GPA :"))
score = float(input("SCORE :"))
if (gpa < 0 or 4 < gpa ) or (0 > score or score > 100):
    print("Error")
else:    
    if gpa >= 3.5:
      if score >= 80:
        print ("Eligible for Honors")
      else:
        print("GPA good, but score needs improvement")    
    else:
        print("Need higher GPA")  



      