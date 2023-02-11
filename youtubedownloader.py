import PySimpleGUI as sg
import pickle

sg.change_look_and_feel('Dark')
filename = 'vacas.pkl'

try:
    with open(filename, 'rb') as f:
        vacas_inscritas = pickle.load(f)
except:
    vacas_inscritas = []

layout = [
    [sg.Image("C:\\Users\\leona\\Downloads\\breve.png",)],
    [sg.Text("En la casilla numero puedes agregar o buscar tu vaquita")],
    [sg.Text('numero'), sg.InputText(key='numero')],
    [sg.Text('Fecha de nacimiento'), sg.InputText(key='fecha_nacimiento')],
    [sg.Text('Fecha de vacunación'), sg.InputText(key='fecha_vacunacion')],
    [sg.Text('Cantidad de partos'), sg.InputText(key='cantidad_partos')],
    [sg.Text("                           ingeniero leonardo contacto +57 3105660092")],
    [sg.Button('Agregar vaca'), sg.Button('Buscar vaca')]
]

window = sg.Window('Vacas', layout, size=(450, 600))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Agregar vaca':
        vacas_inscritas.append(values)
        sg.popup(f"Vaca agregada: {values}")
    if event == 'Buscar vaca':
        numero = values['numero']
        found = False
        for vaca in vacas_inscritas:
            if 'numero' in vaca and vaca['numero'] == numero:
                sg.popup(f"La vaca seleccionada es \n"
                         f" {vaca}")
                found = True
                break
        if not found:
            sg.popup(f"No se encontró una vaca con el número {numero}")
with open(filename, 'wb') as f:
    pickle.dump(vacas_inscritas, f)

window.close()