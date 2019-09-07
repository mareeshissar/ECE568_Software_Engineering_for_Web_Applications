#include <stdio.h>      /* for perror(), fprintf(), sprintf() */
#include <stdlib.h>     /* for atoi() */
#include <string.h>     /* for memset(), memcpy(), strlen() */
#include <sys/socket.h> /* for sockaddr, socket(), connect(),
                           recv(), send(), htonl(), htons() */
#include <arpa/inet.h>  /* for sockaddr_in */
#include <netdb.h>      /* for hostent, gethostbyname() */
#include <unistd.h>     /* for close() */
#include <string.h>
#define RCVBUFSIZE 256 /* Size of receive buffer */
#define ERR_EXIT(msg) { perror(msg); exit(1); }

int main(int argc, char *argv[]) {
    int c_sock, port_num, msg_len;
    struct sockaddr_in serv_addr;
    struct hostent *serverIP;
    char buffer[RCVBUFSIZE];
    char buffer_cpy[RCVBUFSIZE];
    if (argc != 3) {   /* Test for correct number of arguments */
        char msg[64];  memset((char *) &msg, 0, 64);  /* erase */
        sprintf(msg, "Usage: %s serv_name serv_port\n", argv[0]);
        ERR_EXIT(msg);
    }

    serverIP = gethostbyname(argv[1]); /* 1st arg: server name */
    if (serverIP == NULL)
        ERR_EXIT("ERROR, server host name unknown");

    port_num = atoi(argv[2]);  /* Second arg: server port num. */
    //fprintf(stdout, "name: %s\n", serverIP->h_name);
    c_sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (c_sock < 0)  ERR_EXIT("ERROR opening socket");
    memset((char *) &serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
 //   memcpy((char *) &serv_addr.sin_addr.s_addr,
 //       (char *) &(inet_addr(serverIP->h_addr)), serverIP->h_length);
    serv_addr.sin_addr.s_addr=inet_addr(serverIP->h_name);
    serv_addr.sin_port = htons(port_num);

    if (connect(c_sock, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        ERR_EXIT("ERROR connecting");


    char *cmd;
while(1)
{
  //display menu
    printf("User, enter your command: \n");
    printf("GET$filename \n");
    printf("BOUNCE$text-to-bounce \n");
    printf("EXIT$exit code \n\n");
    memset(buffer, 0, RCVBUFSIZE);  /* erase */
    fgets(buffer, RCVBUFSIZE, stdin); /* read input */
    memset(buffer_cpy, 0, RCVBUFSIZE);  /* erase */
    strncpy(buffer_cpy,buffer,strlen(buffer)-1);//for removing the \n from the end

    cmd=strtok(buffer_cpy,"$");//get command

    //if command is EXIT
    if(strcmp(cmd,"EXIT")==0)
    {
    msg_len = send(c_sock, buffer, strlen(buffer), 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    memset(buffer, 0, RCVBUFSIZE);
    msg_len = recv(c_sock, buffer, RCVBUFSIZE - 1, 0);
    if (msg_len < 0) ERR_EXIT("ERROR reading from socket");
    fprintf(stdout, "Server output: %s\n\n", buffer);
    close(c_sock);
    break;
    }

    msg_len = send(c_sock, buffer, strlen(buffer), 0);
    if (msg_len < 0) ERR_EXIT("ERROR writing to socket");
    memset(buffer, 0, RCVBUFSIZE);
    msg_len = recv(c_sock, buffer, RCVBUFSIZE - 1, 0);
    if (msg_len < 0) ERR_EXIT("ERROR reading from socket");
    fprintf(stdout, "Server output: %s\n\n", buffer);


}//end of while
exit(0);
}
