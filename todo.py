#making the list name tasks

my_task=[]
 
#match case

def case(value):
        match value:
            case 1:
               print("ADD Task")
               task=input("ENTER THE TASK YOU WANT TO ADD : ")
               my_task.append(task)
               print(" Task added Successfully !")
               #print(my_task)
            
            
            case 2:
               print("VIEW Task")
               i=1
               if  len(my_task) == 0:
                     print(" EMPTY TO DO LIST")
                
               else:
                   for task in my_task:
                        print(i,":  ",task)
                        i=i+1
                  

            case 3:
               print("DELETE Task")
               del_task= input("ENTER THE TASK TO DELETE : ")
               if del_task in my_task:
                   my_task.remove(del_task)
                   print("TASK DELETED SUCCESSFULLY")
               else:
                   print("NO SUCH MATCH FOUND!!")   

            case 4:
               print("UPDATE TASK")
               upd_task= input("ENTER THE TASK TO update : ")
               if upd_task in my_task:
                    update_value=input("ENTER THE VALUE FOR UPDTAED TASK :")
                    pos=my_task.index(upd_task)
                    my_task[pos]=update_value
                    print("TASK UPDATED SUCCESSFULLY")
               else:
                   print("NO SUCH A MATCH FOUND ")

            case 5:
               print("EXIT LIST")
               
            case _:
               print("invalid input")  


while True:
#TO DO MENU
     print("-----------TO DO TASK MENU----------")
     print(" 1: ADD TASK")
     print(" 2: VIEW TASK")
     print(" 3: DELETE TASK")
     print(" 4: UPDATE TASK")
     print(" 5: EXITS LIST")

     value=int(input("enter your choice  : "))
     case(value)
     if value == 5:
         break
  
        