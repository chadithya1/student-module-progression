#import graphicwindow,color,point from graphic file
from graphics import *

#define the histogram chart using def function
def histogram_chart(progress, module_retrive, module_trailer, exclude):
    #create a window and background colour
    win = GraphWin("Histrogram Results",700,700)
    win.setBackground(color="#FFFFFF")

    #balance the height using student variable
    Students = progress + module_retrive + module_trailer + exclude
    histo_width = 50

    my_heading = Text(Point(100, 30), 'Histogram Result')
    height = 200 / Students
    
    #progress colomn
    colomn_1 = Rectangle(Point(100,450), Point(100 + histo_width, 450 - (progress * height)))
    colomn_1.setFill('red')
    colomn_1.draw(win)
    colomn_name = Text(Point(100 + histo_width/2,470), f"progress - {progress}")
    colomn_name.draw(win)

    #module_trailer colomn
    colomn_2 = Rectangle(Point(200,450), Point(200 + histo_width, 450 - ( module_trailer * height)))
    colomn_2.setFill('green')
    colomn_2.draw(win)
    colomn_name = Text(Point(200 + histo_width/2,470), f"trailer - {module_trailer}")
    colomn_name.draw(win)

    #module_retrive colomn
    colomn_3 = Rectangle(Point(300,450), Point(300 + histo_width, 450 - (module_retrive * height)))
    colomn_3.setFill('yellow')
    colomn_3.draw(win)
    colomn_name = Text(Point(300 + histo_width/2,470), f"retrive - {module_retrive}")
    colomn_name.draw(win)

    #exclude colomn
    colomn_4 = Rectangle(Point(400,450), Point(400 + histo_width, 450 - (exclude * height)))
    colomn_4.setFill('blue')
    colomn_4.draw(win)
    colomn_name = Text(Point(400 + histo_width/2,470), f"exclude- {exclude}")
    colomn_name.draw(win)

    total_name = Text(Point(350,600), f"Total students - {Students}")
    total_name.draw(win)

    #open text file and write the final output in records.txt
    my_heading.draw(win)
    with open("records.txt","w") as record_file:
        for output in result:
            record_file.write(f"{output[3]} - {output[0]}, {output[1]}, {output[2]}")

    #close the window
    win.getMouse()
    win.close()
    
#define variables
result = []
progress = 0
module_retrive = 0
module_trailer = 0
exclude = 0
is_break=False


while True:
    
    try:   
        #Get pass credits from the user 
        pass_credits = int(input("Please enter your pass credits: "))
        if pass_credits not in [0,20,40,60,80,100,120]:
            print ("Out of range")
            continue
        #Get defer credits from the user
        defer_credits = int(input("Please enter your defer credits: "))    
        if defer_credits not in [0,20,40,60,80,100,120]:
            print ("Out of range")
            continue
        #Get fail credits from the user
        fail_credits = int(input("Please enter your fail credits: "))    
        if fail_credits not in [0,20,40,60,80,100,120] :
            print ("Out of range")
            continue

        #display total incorrect when sum of credits are not equal 120
        elif pass_credits + defer_credits + fail_credits != 120:
            print ("Total incorrect")
    
        #display progress   
        elif pass_credits == 120 and defer_credits == 0 and fail_credits == 0 :
            print("progress")
            outcome = "progress"
            
        #display progress(module trailer) 
        elif  pass_credits == 100 and defer_credits == 20 and fail_credits == 0 or\
              pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
            print("progress(module trailer)")
            outcome = "progress(module trailer)"

        #display Do not progress - module retrive     
        elif pass_credits == 80 and defer_credits == 40 and fail_credits == 0 or\
             pass_credits == 80 and defer_credits == 20 and fail_credits == 20 or\
             pass_credits == 80 and defer_credits == 0 and fail_credits == 40 or\
             pass_credits == 60 and defer_credits == 60 and fail_credits == 0 or\
             pass_credits == 60 and defer_credits == 40 and fail_credits == 20 or\
             pass_credits == 60 and defer_credits == 20 and fail_credits == 40 or\
             pass_credits == 60 and defer_credits == 0 and fail_credits == 60 or\
             pass_credits == 40 and defer_credits == 80 and fail_credits == 0 or\
             pass_credits == 40 and defer_credits == 60 and fail_credits == 20 or\
             pass_credits == 40 and defer_credits == 40 and fail_credits == 40 or\
             pass_credits == 40 and defer_credits == 20 and fail_credits == 60 or\
             pass_credits == 20 and defer_credits == 100 and fail_credits == 0 or\
             pass_credits == 20 and defer_credits == 80 and fail_credits == 20 or\
             pass_credits == 20 and defer_credits == 60 and fail_credits == 40 or\
             pass_credits == 20 and defer_credits == 40 and fail_credits == 60 or\
             pass_credits == 0 and defer_credits == 120 and fail_credits == 0 or\
             pass_credits == 0 and defer_credits == 100 and fail_credits == 20 or\
             pass_credits == 0 and defer_credits == 80 and fail_credits == 40 or\
             pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
            print("Do not progress - module retrive")
            outcome = "Do not progress - module retrive"
            
        #display("Exclude")
        elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80 or\
             pass_credits == 20 and defer_credits == 20 and fail_credits == 80 or\
             pass_credits == 20 and defer_credits == 0 and fail_credits == 100 or\
             pass_credits == 0 and defer_credits == 40 and fail_credits == 80 or\
             pass_credits == 0 and defer_credits == 20 and fail_credits == 100 or\
             pass_credits == 0 and defer_credits == 0 and fail_credits == 120:
            print("Exclude")
            outcome = "Exclude"
            

        #result.append((pass_credits, defer_credits, fail_credits, outcome))
        
        if outcome == "progress":
            progress += 1
        elif outcome == "progress(module trailer)":
            module_trailer += 1
        elif outcome == "Do not progress - module retrive":
            module_retrive += 1
        elif outcome == "Exclude":
            exclude += 1
        
        #ask the user like to enter another set of data        
        while True:
            #display as a list            
            result.append((pass_credits, defer_credits, fail_credits, outcome))
            repeat=input("would you like to enter another set of data ?\nEnter \"y\" for yes or \"q\" to quit and view results: ")
            #"y" means yes and continue
            if repeat.lower() == "y":
                break

            #"q" means quit and it will break
            elif repeat.lower() == "q":
                for output in result:
                    print(f"{output[3]} - {output[0]}, {output[1]}, {output[2]}")

                histogram_chart(progress, module_retrive, module_trailer, exclude)

            #if user input != q or y print that
            else:
                print("use suitable character(y/q)")

                    
    except ValueError:
        print("Integer required")





