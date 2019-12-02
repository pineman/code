// gcc -o countFuelThreads countFuelThreads.c -lgmp -pthread -O3 -Ofast
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <pthread.h>

// GNU Multiple Precision library
// Link with -lgmp
#include <gmp.h>

#define MAX_SIZE (1000000 * 47)

struct task {
    char *buffer;
    size_t start;
    size_t end;
    mpz_t result;
    mpz_t result_all;
};

void count_fuel(mpz_t result, mpz_t weight) {
    mpz_fdiv_q_ui(result, weight, 3);
    mpz_sub_ui(result, result, 2);
}

void count_all_fuel(mpz_t result, mpz_t weight) {
    mpz_t partial;
    mpz_init(partial);
    count_fuel(partial, weight);
    while (mpz_cmp_ui(partial, 0) > 0) {
        mpz_add(result, result, partial);
        count_fuel(partial, partial);
    }
}

void *perform_fuel_task(void *arg) {
    struct task task = *((struct task *) arg);

    mpz_t sum;
    mpz_init(sum);
    mpz_t sum_all;
    mpz_init(sum_all);
    size_t start = task.start;
    size_t end = start + 39;

    if (start > 0 && (task.buffer[start] != '\n' || task.buffer[start] != '\0')) {
        while (task.buffer[start] != '\n' && task.buffer[start] != '\0') {
            start++;
        }
        start++;
        end = start + 39;
    }

    while (start < task.end) {
        while (task.buffer[end] != '\n' && task.buffer[end] != '\0') {
            end++;
        }

        task.buffer[end] = '\0';

        mpz_t weight;
        mpz_init_set_str(weight, task.buffer + start, 10);
        count_fuel(weight, weight);
        mpz_add(sum, sum, weight);
        count_all_fuel(weight, weight);
        mpz_add(sum_all, sum_all, weight);

        start = end + 1;
        end = start + 39;
    } 

    mpz_set(((struct task *)arg)->result, sum);
    mpz_set(((struct task *)arg)->result_all, sum_all);
    pthread_exit(0);
}

int main() {
    int bigboy_fd = open("./bigboyinput", O_RDONLY);
    char *buffer = malloc(MAX_SIZE);
    ssize_t bytes_read = read(bigboy_fd, buffer, MAX_SIZE);

    if (bytes_read < 0) {
        printf("failed to read\n");
        exit(1);
    }

    pthread_t threads[4];
    struct task tasks[4];

    for (int i = 0; i < 4; i++) {
        tasks[i].buffer = buffer;
        tasks[i].start = i * (bytes_read / 4);
        tasks[i].end = (i + 1) * (bytes_read / 4) - 1;
        mpz_init(tasks[i].result);
        mpz_init(tasks[i].result_all);
    }
    tasks[3].end = bytes_read;

    for (int i = 0; i < 4; i++) {
        int ret = pthread_create(&threads[i], NULL, perform_fuel_task, (void *) &tasks[i]);
        if (ret != 0) {
            printf("failed to create pthread\n");
            exit(1);
        }
    }

    for (int i = 0; i < 4; i++) {
        int ret = pthread_join(threads[i], NULL);

        if (ret != 0) {
            printf("failed to join\n");
            exit(1);
        }
    }

    mpz_t total;
    mpz_init(total);
    for (int i = 0; i < 4; i++) {
        mpz_add(total, total, tasks[i].result);
    }

    mpz_t total_all;
    mpz_init(total_all);
    for (int i = 0; i < 4; i++) {
        mpz_add(total_all, total_all, tasks[i].result_all);
    }

    printf("part 1: %s\n", mpz_get_str(NULL, 10, total));
    printf("part 2: %s\n", mpz_get_str(NULL, 10, total_all));
}