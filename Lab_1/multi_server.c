//
//
//
//
//
//
//

#include <arpa/inet.h>
#include <errno.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/_types/_socklen_t.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#define PORT 8080

int main(int argc, const char* argv[]) {
    /*
    PART 1 - SOCKET CREATION
    */
    int server_socket = socket(AF_INET, SOCK_STREAM,
                               0);  // Create server socket with IPv4 and TCP
    if (server_socket == -1) {
        perror("Socket creation failed...");  // Error message if socket creation
                                              // failure
        exit(1);
    }
    printf("Server socket successfully created...");  // Successful socket
                                                      // creation message

    /*
    PART 2 - BIND SOCKET
    */
    struct sockaddr_in host_address;                             // Create address to bind socket to
    int                host_addr_length = sizeof(host_address);  // Get address length
    host_address.sin_family             = AF_INET;               // Always set to AF_INET
    host_address.sin_port               = htons(PORT);           // Convert Port address
                                                                 // to network byte order
    host_address.sin_addr.s_addr = htonl(INADDR_ANY);            // Translates to "0.0.0.0"
    if (bind(server_socket, (struct sockaddr*)&host_address, host_addr_length) != 0) {
        perror("Bind failure...");
        exit(1);
    }
    printf("Server socket successfully bound...");

    /*
    PART 3 - MAKE SOCKET LISTEN
    */
    if (listen(server_socket, SOMAXCONN) != 0) {  // SOMAXCONN = system specific maximum connections
        perror("Listening failure...");
        exit(1);
    }
    printf("Socket server listening for connections");

    /*
    PART 4 - ACCEPT
    */
    while (TRUE) {
        int new_connection = accept(server_socket, (struct sockaddr*)&host_address,
                                    (socklen_t*)&host_addr_length);
        if (new_connection != 0) {
            perror("Connection acceptance failded...");
            continue;
        }
        printf("Connection accepted...");
        close(new_connection);  // Close new connection
    }

    /*
        PART 5 - READ/WRITE
    */

    return 0;
}
