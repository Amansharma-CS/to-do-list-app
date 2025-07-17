
todos=[]
while True:
    user_prompt =input( "enter add, show, exit, compelete : ")
    user_prompt=user_prompt.strip()

    match user_prompt:
        case 'add':
         todo= input("enter a todo : ") + "\n"

         file = open("todos.txt",'r')
         todos = file.readlines()
         file.close()

         todos.append(todo)

         file = open('todos.txt', 'w')
         file.writelines(todos)

        case 'show':
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()
            for index,item in enumerate(todos):
                row = f"{index+1}:{item}"
                print(row)
        case 'compelete':
             number = int(input("which one : "))
             number = number - 1
             file = open("todos.txt", 'r')
             todos = file.readlines()
             file.close()
             todos.pop(number)
        case'exit':
             break
        case 'edit':
            number = int(input("which one : "))
            number = number - 1
            new_todo = input("new todo : ")
            todos[number] = new_todo
        case _:
            print("wrong command h wapas daal")




