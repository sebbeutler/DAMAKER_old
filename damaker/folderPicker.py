import PySimpleGUI as sg
sg.theme("DarkTeal2")


def getFolder(text="Choose a folder:"):
    layout = [[sg.T("")], [sg.Text(text), sg.Input(), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]
    window = sg.Window('Folder Picker', layout, size=(600,150))
    folder = ""
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            folder = values["-IN-"]
            print(folder)
            window.close()
            break
    return folder