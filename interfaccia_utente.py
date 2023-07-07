import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import bot_promemoria
from tkinter import *
import win32com.client 
import sub_client
import socket
import sys

# Creazione oggetto Outlook come variabile globale
outlook = None

# Creazione oggetto window
window = tk.Tk()
window.title("AssistenteEventi")

# Creazione dell'area di visualizzazione dei messaggi
messages_area = scrolledtext.ScrolledText(window, width=50, height=20)
messages_area.pack(padx=10, pady=10)

# Creazione socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.40.1", 15000)

try:
    s.connect(server_address)
    socket_client = s
    print(f"Connessione al server {server_address} stabilita")
except socket.error as errore:
    print(f"Qualcosa è andato storto, sto uscendo...\n{errore}")
    sys.exit()

# Creazione input per user
input_area = tk.Entry(window, width=40)
input_area.pack(padx=10, pady=10)

# Messaggio che si visualizza all'inizio della chat
introduction = bot_promemoria.phrase_start()
messages_area.insert(tk.END, "ChatBot: " + introduction + "\n")

def createEventWindow():  # create a nuova finestra per definire data, ora , soggetto e durata di un evento
    global outlook
    window_event = tk.Toplevel()
    window_event.title("Evento")

    label_data = Label(window_event, text="Data (formato yyyy-mm-dd):")
    label_data.pack()
    input_area_data = tk.Entry(window_event, width=40)
    input_area_data.pack(padx=10, pady=10)

    label_ora = Label(window_event, text="Ora (formato hh:mm):")
    label_ora.pack()
    input_area_ora = tk.Entry(window_event, width=40)
    input_area_ora.pack(padx=10, pady=10)

    label_soggetto = Label(window_event, text="Soggetto:")
    label_soggetto.pack()
    input_area_soggetto = tk.Entry(window_event, width=40)
    input_area_soggetto.pack(padx=10, pady=10)

    label_durata = Label(window_event, text="Durata (minuti):")
    label_durata.pack()
    input_area_durata = tk.Entry(window_event, width=40)
    input_area_durata.pack(padx=10, pady=10)

    def saveEvent():
        global outlook
        data = input_area_data.get()
        ora = input_area_ora.get()
        soggetto = input_area_soggetto.get()
        durata = input_area_durata.get()

        if outlook is None:
            outlook = win32com.client.Dispatch("Outlook.Application")

        appt = outlook.CreateItem(1)  # Evento
        appt.Start = data + " " + ora  # Data e ora
        appt.Subject = soggetto  # Soggetto
        appt.Duration = durata  # Durata evento
        appt.Save()
        print("Evento memorizzato correttamente.")
        window_event.destroy()

    save_button = Button(window_event, text="Salva", command=saveEvent)
    save_button.pack(pady=10)
    window_event.bind('<Return>', lambda event: saveEvent())

def sendEmail():
    global outlook
    window_email=tk.Toplevel()
    window_email.title("Email")

    label_email = Label(window_email, text="email: ")
    label_email.pack()
    input_area_email = tk.Entry(window_email, width=40)
    input_area_email.pack(padx=10, pady=10)

    label_soggetto = Label(window_email, text="soggetto: ")
    label_soggetto.pack()
    input_area_soggetto = tk.Entry(window_email, width=40)
    input_area_soggetto.pack(padx=10, pady=10)

    label_corpo = Label(window_email, text="corpo email: ")
    label_corpo.pack()
    input_area_corpo = tk.Entry(window_email, width=40)
    input_area_corpo.pack(padx=10, pady=10)

    def saveSendEmail():
        email=input_area_email.get()
        soggetto=input_area_soggetto.get()
        corpo=input_area_corpo.get()
        Msg = outlook.CreateItem(0) # Email
        outlook = win32com.client.Dispatch("Outlook.Application")
        outlook.Session.Logon(emailUtente, password, True, True)
        emailUtente=""
        password=""
        Msg.To = email # you can add multiple emails with the ; as delimiter. E.g. test@test.com; test2@test.com;
        Msg.Subject = soggetto
        Msg.Body = corpo
        Msg.Send()

    send_button = Button(window_email, text="Salva", command=saveSendEmail)
    send_button.pack(pady=10)
    window_email.bind('<Return>', lambda event: saveSendEmail())

def changeEventWindow(): #funzione per rinominare evento
    global outlook
    window_change_event = tk.Toplevel()
    window_change_event.title("Cambiare evento")
    label_data = Label(window_change_event, text="Data (formato yyyy-mm-dd):")
    label_data.pack()
    input_area_data = tk.Entry(window_change_event, width=40)
    input_area_data.pack(padx=10, pady=10)

    label_ora = Label(window_change_event, text="Ora (formato hh:mm):")
    label_ora.pack()
    input_area_ora = tk.Entry(window_change_event, width=40)
    input_area_ora.pack(padx=10, pady=10)

    label_soggetto = Label(window_change_event, text="Soggetto:")
    label_soggetto.pack()
    input_area_soggetto = tk.Entry(window_change_event, width=40)
    input_area_soggetto.pack(padx=10, pady=10)

    label_durata = Label(window_change_event, text="Durata (minuti):")
    label_durata.pack()
    input_area_durata = tk.Entry(window_change_event, width=40)
    input_area_durata.pack(padx=10, pady=10)

    def saveChangeEvent():
        global outlook
        data = input_area_data.get()
        ora = input_area_ora.get()
        soggetto = input_area_soggetto.get()
        durata = input_area_durata.get()

        if outlook is None:
            outlook = win32com.client.Dispatch("Outlook.Application")

        # Recupera il calendario predefinito
        calendar = outlook.GetNamespace("MAPI").GetDefaultFolder(9)

        selection = calendar.GetSelection()
        if len(selection) == 1 and selection[0].Class == 26:
            event = selection[0]
            event.Start = data + " " + ora
            event.Subject = soggetto
            event.Duration = durata
            event.Save()
            print("Evento modificato correttamente.")
        else:
            messagebox.showwarning("Selezione non valida", "Seleziona un singolo evento valido da modificare.")
        window_change_event.destroy()

    save_button = Button(window_change_event, text="Rinomina", command=saveChangeEvent)
    save_button.pack(pady=10)
    window_change_event.bind('<Return>', lambda event: saveChangeEvent())


def send_message():
    user_input = input_area.get()
    messages_area.insert(tk.END, "Utente: " + user_input + "\n")

    # Invio del messaggio al server tramite il modulo sub_client
    sub_client.invia_comandi(socket_client, user_input)

    # Chiamata alla funzione di chat per ottenere la risposta
    response = bot_promemoria.response(user_input)
    messages_area.insert(tk.END, "ChatBot: " + response.text + "\n")

    # Pulizia dell'area di inserimento del messaggio
    input_area.delete(0, tk.END)

    # Scroll automatico all'ultima riga
    messages_area.see(tk.END)

    if user_input.startswith("rinominare"):
        changeEventWindow()
    elif user_input.startswith("memorizzare"):
        createEventWindow()
    elif response and "memorizzare" in response.text:
        createEventWindow()
    elif response and "rinominare" in response.text:
        changeEventWindow()
    elif user_input.startswith("email"):
        sendEmail()

def handle_enter_key(event):
    send_message()

window.bind('<Return>', handle_enter_key)

# Creazione pulsante invio
send_button = Button(window, text="Invia", command=send_message)
send_button.pack(pady=10)

# Avvio del ciclo principale di eventi di Tkinter
window.mainloop()