import socket


def print_commands():
    print("\nBelow is the list of commands:\n"
          "/join <server_ip_add> <port>       | Connect to the server application\n"
          "/leave                             | Disconnect to the server application\n"
          "/register <handle>                 | Register a unique handle or alias\n"
          "/store <filename>                  | Send file to server\n"
          "/dir                               | Request directory file list from a server\n"
          "/get <filename>                    | Fetch a file from a server\n"
          "/?                                 | Request command help\n")


print("Hello, welcome to the File Exchange System. Type /? for a list of commands.")
while True:
    command = input("Enter your command: ")

    if command.startswith('/'):
        command_list = command.split()
        if command_list[0] == '/join' and len(command_list) == 3:
            # insert join function
            try:
                addr = (command_list[1], int(command_list[2]))
            except:
                print("Error: Command parameters do not match or is not allowed.")
            else:
                try:
                    client.connect(addr)
                    print("Connection to the File Exchange Server is successful!")
                except:
                    print("Error: Connection to the Server has failed! Please check IP Address and Port Number.")
                
        elif command_list[0] == '/leave':
            # insert leave function
            pass
        elif command_list[0] == '/register' and len(command_list) == 2:
            # insert register function
            pass
        elif command_list[0] == '/store' and len(command_list) == 2:
            # insert store function
            pass
        elif command_list[0] == '/dir':
            # insert dir function
            pass
        elif command_list[0] == '/get' and len(command_list) == 2:
            # insert get function
            pass
        elif command_list[0] == '/?':
            print_commands()
        else:
            print("Error: Command not found")
    else:
        print("Error: Command not found")
