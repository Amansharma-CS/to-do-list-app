import PySimpleGUI as sg
todos=[]

label = sg.Text("Type in a To do")
input_box = sg.InputText(tooltip="Enter a To do", key="todo")
add_button = sg.Button("Add")

windows = sg.Window('TO DO APP', layout=[[label],[input_box,add_button]],
                    font=('Comic Sans MS',16))
while True:
    event, values = windows.read()
    print(event)
    print(values)
    match event:
        case "Add":
            with open("todos.txt",'r') as file:
                file.readlines()
                file.close()
                z=str(values)
                todos.append(z)
            with open("todos.txt",'w') as file:
                file.writelines(todos)


windows.close()

