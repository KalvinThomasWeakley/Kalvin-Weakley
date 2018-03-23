my_list = []

while (True):
    for i in range(5):
        x = input("What is your class? ")
        y = float(input("What is the grade for " + x + "? "))
        my_list.append(y)
        if y < 60:
            print ("Your grade is a U.")
        elif y > 60 and y < 70:
            print ("Your grade is a D.")
        elif y > 70 and y < 80:
            print ("Your grade is a C.")
        elif y > 80 and y < 90:
            print ("Your grade is a B.")
        elif y > 90 and y <= 100:
            print ("Your grade is an A.")
    y = my_list[0] + my_list[1] + my_list[2] + my_list[3] + my_list[4]
    print ("Your average grade is a " + str(y / 5) + ".")
    
    
