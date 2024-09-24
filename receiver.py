import socket
from threading import Thread
from taipy import Gui

HOST = "127.0.0.1"
PORT = 5050
state_id_list = []

def on_init(state):
    state_id = gui.get_state_id(state)
    if (state_id := gui.get_state_id(state)) is not None:
        state_id_list.append(state_id)
def client_handler(gui, state_id_list: list):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, _ = s.accept()
    while True:
        if data := conn.recv(1024):
            print(f"Data received: {data.decode()}")
            if hasattr(gui, "_server") and state_id_list:
                gui.invoke_callback(
                    gui, state_id_list[0], update_received_data, (int(data.decode()),)
                )
        else:
            print("Connection closed")
            break


def update_received_data(state, val):
    state.received_data = val

received_data = 0

md = """
Received Data: <|{received_data}|>
"""
gui = Gui(page=md)

t = Thread(
    target=client_handler,
    args=(
        gui,
        state_id_list,
    ),
)
t.start()

gui.run(title="Receiver Page")