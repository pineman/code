// doesn't actually work on linux. accept doesn't return
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>

static int listen_fd;

void* accept_thread(void* arg) {
    printf("[Thread A] about to call accept() on fd=%d\n", listen_fd);
    int cfd = accept(listen_fd, NULL, NULL);
    if (cfd < 0) {
        printf("[Thread A] accept() error: %s\n", strerror(errno));
    } else {
        printf("[Thread A] accept() success, cfd=%d\n", cfd);
        close(cfd);
    }
    printf("[Thread A] done.\n");
    return NULL;
}

void* close_thread(void* arg) {
    sleep(1);
    printf("[Thread B] closing listen_fd=%d\n", listen_fd);
    close(listen_fd);
    printf("[Thread B] done.\n");
    return NULL;
}

int main(void) {
    // Create listening socket
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);

    // Bind to port 9999 on localhost
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port   = htons(9999);
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    bind(listen_fd, (struct sockaddr*)&addr, sizeof(addr));
    listen(listen_fd, 5);

    printf("[Main] listening on fd=%d\n", listen_fd);

    pthread_t ta, tb;
    pthread_create(&ta, NULL, accept_thread, NULL);
    pthread_create(&tb, NULL, close_thread, NULL);

    pthread_join(ta, NULL);
    pthread_join(tb, NULL);

    printf("[Main] finished.\n");
    return 0;
}
