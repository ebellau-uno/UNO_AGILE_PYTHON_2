import json

import sys
import PySimpleGUI as psg
import requests


def add(name, description, date, importance):
    response = requests.get(
        f"http://ebellau.pythonanywhere.com/v1/add?name={name}&description={description} \
            &date={date}&importance={importance}")


def update(app_id, name, description, date, importance):
    response = requests.get(
        f"http://ebellau.pythonanywhere.com/v1/update?id={app_id}&name={name} \
            &description={description}&date={date}&importance={importance}")


def delete(app_id):
    response = requests.get(
        f"http://ebellau.pythonanywhere.com/v1/delete?id={app_id}")


def fetch():
    response = requests.get(
        "http://ebellau.pythonanywhere.com/v1/all")
    data = response.json()
    todo = []
    todo.append("\n")
    for key, value in data.items():
        todo.append(key)
        for _, val in value.items():
            todo.append(str(val))
        todo.append("\n")
    data = " ".join(todo)
    return data

def refresh_all(window, data):
    try:
        window['-DATA-'].update(data)
        window['-ID-'].update("")
        window['-NAME-'].update("")
        window['-DESCRIPTION-'].update("")
        window['-DATE-'].update("")
        window['-IMPORTANCE-'].update("")
        return
    except Exception as err:
        raise Exception from err





def start_app():
    data = fetch()

    layout = [[psg.Text("Todo Items"), psg.Text(
        size=(12,1), key='-DISPLAY-')],
        [psg.Text(data, key='-DATA-')],
        [psg.Text("ID", size=(12,1)), psg.Input(key='-ID-')],
        [psg.Text("NAME", size=(12,1)), psg.Input(key='-NAME-')],
        [psg.Text("DESCRIPTION", size=(12,1)), psg.Input(key='-DESCRIPTION-')],
        [psg.Text("DATE", size=(12,1)), psg.Input(key='-DATE-')],
        [psg.Text("IMPORTANCE", size=(12,1)), psg.Input(key='-IMPORTANCE-')],
        [psg.Text("")],
        [psg.Button("Add"), psg.Button("Update"), psg.Button("Delete"), psg.Button("EXIT")]
    ]

    # Create a window
    window = psg.Window('TODO App', layout)

    # Create an event loop
    while True:
        event, values = window.read()
        if event == "EXIT" or event == psg.WIN_CLOSED:
            sys.exit()
        if event == "Add":
            add(values["-NAME-"], values["-DESCRIPTION-"], values["-DATE-"], values["-IMPORTANCE-"])
        if event == "Update":
            update(values["-ID-"], values["-NAME-"], values["-DESCRIPTION-"], \
                 values["-DATE-"], values["-IMPORTANCE-"])
        if event == "Delete":
            delete(values["-ID-"])
        data = fetch()
        refresh_all(window, data)
    window.close()


if __name__ == "__main__":
    start_app()
