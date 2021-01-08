from socket import *
import socket
import pickle
import threading


#creating a socket
client = socket.socket(AF_INET, SOCK_STREAM)

ipAddress=input("Enter the application IP address (127.0.0.1): ")
portNumber=input("Enter the application port number(5000): ")
port=5000

username = input("Enter your username: ")


client.connect((ipAddress, port))


data = (16, 32, username, "conn")
data = pickle.dumps(data)
client.send(data )


#recieving data from the server
def recieve():
    while True:
        try:
            data = client.recv(1024)
            data = pickle.loads(data)
            if data[1] != 0:
                print( data[2], ": ", data[3])
                print("\n")
        except:
            print("\n Disconnected from the server")
            print("\n")
            client.close()
        

#sending data to the server
def write():
      while True:
        try:
            userInput = input("you: ")
            UNAMEL= (len(username))
            MESSAGEL = len(userInput)
            USERNAME = username
            MESSAGE= userInput
            DATA= (UNAMEL, MESSAGEL, USERNAME, MESSAGE)
            data = pickle.dumps(DATA)
            client.send(data)
        except:
            print("Disconnected from the server")
            print("\n")
            client.close()
           


thread_recieve=threading.Thread(target=recieve)
thread_recieve.start()
thread_write=threading.Thread(target=write)
thread_write.start()









