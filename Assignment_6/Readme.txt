Platform-Ubuntu (64 bit) 14.04 LTS running on virtual box inside Windows 8.1

Copy all the files into the directory specified by the ls command in the Ubuntu.

Open two terminal windows.

In the first terminal window type the following command:-
gcc -o server server_final.c  and press enter
./server 5800

NOTE: You can select port to be anything between 5500 to 65535.
127.0.0.1 is the local host IP.
All the valid commands used here are case sensitive. 

The server will start running and the following message will be displayed:-
Waiting for client to connect...


In the second terminal window type the following command:-
gcc -o client client_final.c  and press enter
./client 127.0.0.1 5800

GET$test.txt
This command will display the following message on the client side:-
Server output: This is line 1 of the test document.
This is line 2 of the test document.
This is line 3 of the test document.
This is line 4 of the test document.

GET$lion.txt
This command will display the following message on the client side:-
Server output: File does not exist 

BOUNCE$bounce text1 
This command will display the following message on the client side:-
Server output: bounce text1

now
This command will display the following message on the client side:-
Server output: You have entered wrong command

EXIT 
This command will display the following message on the client side:-
Server output: Normal exit 

EXIT$2345 
This command will display the following message on the client side:-
Server output: 2345

