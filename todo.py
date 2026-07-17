#making the list name tasks

my_task=[]
 

#function for the add list
def add_task():
      print("\n╔═══════════════════════════════╗")
      print("║           ADD TASK             ║")
      print("╚═══════════════════════════════╝")
      task=input("ENTER THE TASK YOU WANT TO ADD : ").strip()
      if task == "":
         print("TASK CANT BE EMPTY")
      else:    
         my_task.append(task)
         print("✅ Task added Successfully !")
               #print(my_task)

#function to view list
def view_task():
    print("\n╔═══════════════════════════════╗")
    print("║           VIEW TASKS           ║")
    print("╚═══════════════════════════════╝")
    i=1
    if  len(my_task) == 0:
          print("📭 EMPTY TO DO LIST")
                
    else:
         print("-" * 35)
         for task in my_task:
             print(f" {i} :  {task}")
             i=i+1
         print("-" * 35)


#function to delete
def del_task():
       print("\n╔═══════════════════════════════╗")
       print("║          DELETE TASK           ║")
       print("╚═══════════════════════════════╝")
       del_task= input("ENTER THE TASK TO DELETE : ")
       found = False
       for task in my_task:
         if del_task.lower() == task.lower():
          my_task.remove(task)
          print("🗑️  TASK DELETED SUCCESSFULLY")
          found=True
       if not found:
             print("NO SUCH MATCH FOUND!!")  

#function to update
def update_task():
      print("\n╔═══════════════════════════════╗")
      print("║          UPDATE TASK           ║")
      print("╚═══════════════════════════════╝")
      upd_task= input("ENTER THE TASK TO update : ")
      if upd_task in my_task:
         update_value=input("ENTER THE VALUE FOR UPDTAED TASK :")
         pos=my_task.index(upd_task)
         my_task[pos]=update_value
         print("✏️  TASK UPDATED SUCCESSFULLY")
      else:
         print("NO SUCH A MATCH FOUND ")

#menu for to do list
def menu(value):
        match value:
            case 1:
               add_task()
            
            case 2:
               view_task()

            case 3:
               del_task()  

            case 4:
              update_task()
            case 5:
               print("\nEXIT LIST")
               
            case _:
               print("invalid input")  


while True:
#TO DO MENU
     print("\n╔══════════════════════════════════╗")
     print("║      📝  TO DO TASK MENU  📝      ║")
     print("╠══════════════════════════════════╣")
     print("║  1 : ➕ ADD TASK                  ║")
     print("║  2 : 👀 VIEW TASK                 ║")
     print("║  3 : 🗑️  DELETE TASK               ║")
     print("║  4 : ✏️  UPDATE TASK               ║")
     print("║  5 : 🚪 EXIT LIST                 ║")
     print("╚══════════════════════════════════╝")
     try:
       value=int(input("ENTER THE CHOICE : "))
     except ValueError:   
       print("ENTER THE VALID CHOICE ")
       continue


     menu(value)
     if value == 5:
         break