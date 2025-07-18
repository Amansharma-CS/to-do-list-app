import PySimpleGUI as sg

label = sg.Text("Type in a To do")
input_box = sg.InputText(tooltip="Enter a To do")
add_button = sg.Button("Add")

windows = sg.Window('TO DO APP', layout=[[label],[input_box,add_button]])
windows.read()
print("hari om")
windows.close()

