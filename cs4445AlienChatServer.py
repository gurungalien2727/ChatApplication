#######################   Chat Application : Built by  Alien Gurung and Quang Tran  ####################################### 

import threading
import socket
import pickle
import time
from socket import *




localhost="127.0.0.1"
port = 5000

#creating a socket to bind the IP address and Port number
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((localhost, port))

#listens for incoming connections upto 20
serverSocket.listen(20)

print("Server is listening on port 5000")

#lists to store the clients and users connected to the server
clients = []
users = []



#sends/broadcast the message to all the client that are currently connected to the server
def broadcast(message, socket):
    print(message[2], " : ", message[3])
    message = pickle.dumps(message)
    for client in clients:
        if socket != client:
            client.send(message)


#handles individual client
def handle(connection, address):
    try:
        data = connection.recv(1024)
        data = pickle.loads(data)
        conn = data[2] + " has entered the chatroom !"
        conn = (len("server"), len(conn), "server", conn)
        broadcast(conn, connection)
        c= (len("server"), len("You are Connected !"), "Server", "You are connected !")
        c= pickle.dumps(c)
        connection.send(c)
        users.append(data[2])

        while True:
            #recieve the message and broadcast the message to all other clients
            message = connection.recv(1024)
            message = pickle.loads(message)
            if message[1] == 0:
                break
            broadcast(message, connection)

        connection.close()
    except:
        #removes  the client from the chatroom
        removeClient = data[2] + " left the chatroom!"
        DATA = (16, 32, "server", removeClient)
        broadcast(DATA, connection)
        clients.remove(connection)
        users.remove(data[2]) 



#displays the name of the clients in the chatroom
def displayUsers():
    while True:
        usersList = " \n Users List:  "
        for user in users:
            usersList += (user + " ")
        UserDisT = (len("Server"), len(usersList), "Server", usersList)
        broadcast(UserDisT, "Server") 
        time.sleep(100)




thread_display = threading.Thread(target=displayUsers)
thread_display.start()   

#server accepting the connections all the time
while True:
    client, address = serverSocket.accept()
    clients.append(client)
        
    thread = threading.Thread(target=handle, args=(client,address))
    thread.start()






