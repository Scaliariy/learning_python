import PySimpleGUI as sg
from convertors14 import convert

label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(key="inches")

button = sg.Button("Convert")
output = sg.Text(key="output", text_color="yellow")

window = sg.Window("Convertor",
                   layout=[[label1, input_box1],
                           [label2, input_box2],
                           [button, output]])

while True:
    event, values = window.read()
    print(event, values)
    value = convert(values["feet"], values["inches"])
    value = str(value) + ' m'
    window["output"].update(value=value)

    if event == sg.WINDOW_CLOSED:
        break
window.close()

