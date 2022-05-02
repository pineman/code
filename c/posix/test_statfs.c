#include <stdio.h>
#include <errno.h>
#include <sys/vfs.h>

int main(int argc, char *argv[]) {
	struct statfs buf;
	int ret = statfs("/home/pineman/.local/share/containers/storage/overlay", &buf);
	unsigned int type = (unsigned int) buf.f_type;
	printf("ret = %d\n", ret);
	if (ret != 0 ) {
		perror("");
	}
	printf("type = %lx\n", buf.f_type);
	return 0;
}
