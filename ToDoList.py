#To Do List Application
class ToDoList:
    def __init__(self):
        self.l1=[]
    def add(self,task):
        self.l1.append(task)
        print("Task Added successfully...")
    def update(self,old_task,new_task):
        for t in self.l1:
            if t==old_task.lower():
                i=self.l1.index(old_task)
                self.l1.remove(old_task)
                self.l1.insert(i,new_task)
                return 1
    def view(self):
        print("Tasks are :")
        for t in self.l1:
            print(f"{t}")
    def delete(self,task):
        for t in self.l1:
            if t==task.lower():
                self.l1.remove(task)
                return 1
if __name__=="__main__":
    to=ToDoList()
    while(True):
        print("1.Add \n2.update \n3.view \n4.delete")
        op=int(input("Enter your option :"))
        if op==1:
            task=input("Enter the task :")
            to.add(task)
        elif op==2:
            old_task=input("Enter the old Task :")
            new_task=input("Enter new Task :")
            if to.update(old_task,new_task):
                print("Task updated successfully...")
            else:
                print("old task not in list!")
        elif op==3:
            to.view()
        elif op==4:
            task=input("Enter the task to delete :")
            if to.delete(task):
                print("Task deleted successfully...")
            else:
                print("Task not present in list!")
        c=input("Do you want to continue(Y/N) :")
        if c.lower()=="y":
            continue
        else:
            break
        
