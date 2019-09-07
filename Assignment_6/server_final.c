#include <stdio.h>      /* perror(), fprintf(), sprintf() */
#include <stdlib.h>     /* for atoi() */
#include <string.h>     /* for memset() */
#include <sys/socket.h> /* socket(), bind(), listen(), accept(),
                           recv(), send(), htonl(), htons() */
#include <arpa/inet.h>  /* for sockaddr_in */
#include <unistd.h>     /* for close() */
#include <string.h>
#define MAXPENDING 5    /* Max outstanding connection requests */
#define RCVBUFSIZE 256  /* Size of receive buffer */
#define ERR_EXIT(msg) { perror(msg); exit(1); }
int main(int argc, char *argv[]) {
    int rv_sock, s_sock, port_num, msg_len;
    char buffer[RCVBUFSIZE];
    char buffer_cpy[RCVBUFSIZE];
    char buffer_cpy2[RCVBUFSIZE];
    char data[RCVBUFSIZE];
    struct sockaddr_in serv_addr;

    if (argc != 2) {  /* Test for correct number of arguments */
        char msg[64];  memset((char *) &msg, 0, 64);
        sprintf(msg, "Usage: %s server_port\n", argv[0]);
        ERR_EXIT(msg);
    }

rv_sock =socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (rv_sock < 0) ERR_EXIT("ERROR opening socket");
    memset((char *) &serv_addr, 0, sizeof(serv_addr));
    port_num = atoi(argv[1]);  /* First arg: server port num. */
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(port_num);
    if (
	bind(rv_sock, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        ERR_EXIT("ERROR on binding");
    if (
	listen(rv_sock, MAXPENDING) < 0)
        ERR_EXIT("ERROR on listen");

while ( 1 ) {                      /* Server runs forever */
        fprintf(stdout, "\nWaiting for client to connect...\n");
        s_sock = accept(rv_sock, NULL, NULL);
	if (s_sock < 0) ERR_EXIT("ERROR on accept new client");
	fprintf(stdout, "client connected\n");


label:

      memset(buffer, 0, RCVBUFSIZE);
      msg_len = recv(s_sock, buffer, RCVBUFSIZE - 1, 0);
      if (msg_len < 0) ERR_EXIT("ERROR reading from socket");
	//msg_len = recv(s_sock, cmd, RCVBUFSIZE - 1, 0);
	//fprintf(stdout, "command: %s\n", cmd);

      memset(buffer_cpy, 0, RCVBUFSIZE);
      strncpy(buffer_cpy,buffer,(strlen(buffer)-1) );//for removing the \n from the end

      memset(buffer_cpy2, 0, RCVBUFSIZE);
      strncpy(buffer_cpy2,buffer,(strlen(buffer)-1) );//for removing the \n from the end

char *tk;
tk=strtok(buffer_cpy2,"$");//getting the command

printf("Command received: %s\n",tk);
if(strcmp(tk,"GET")==0)
{
    char f_name[100];
    strcpy(f_name,(buffer_cpy+strlen(tk)+1));
    FILE *fptr;
    fptr = fopen(f_name, "r");
    if (fptr == NULL)
    {
    msg_len = send(s_sock,"File does not exist",19, 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    goto label;
    }

    char chunk[RCVBUFSIZE];
    // Read contents from file
     printf("data in file:\n");
    while (!feof(fptr))
    {
       fgets(chunk,256,fptr);
       printf("%s",chunk);
       msg_len = send(s_sock, chunk, strlen(chunk), 0);
       if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    }
    fclose(fptr);
    goto label;
}

else if(strcmp(tk,"BOUNCE")==0)
{
    strcpy(data,buffer_cpy+strlen(tk)+1);
    if(strlen(data)==0)
    {msg_len = send(s_sock,"Nothing to bounce",17 , 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    goto label;
    }
    else
    {msg_len = send(s_sock, data, strlen(data), 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    goto label;
    }
}

else if(strcmp(tk,"EXIT")==0)
{
    strcpy(data,buffer_cpy+strlen(tk)+1);
    if(strlen(data)==0)
    {
    msg_len = send(s_sock,"Normal exit",11 , 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    close(s_sock);
    }
    else
    {printf("exit code: %s\n",data);
    msg_len = send(s_sock, data, strlen(data), 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    close(s_sock);
    }
}

else
{
    msg_len = send(s_sock,"You have entered wrong command",30, 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    goto label;
}

}    /* NOT REACHED, because the server runs forever */
}
