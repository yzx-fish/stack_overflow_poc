// example.c for shellcode

// gcc -fno-stack-protector -z execstack -o example example1.c
// echo 0 > /proc/sys/kernel/randomize_va_space


#include <stdio.h>
#include <string.h>

void example1(char* pstr);

int main(int argc, char **argv) {

    if (argc < 2) return 1;
    example1(argv[1]);
    return 0;
}
void example1(char* pstr)
{
    char buf[100] ={0};
    strncpy(buf, pstr,strlen(pstr));
    printf("hello: %s\n", buf);
}
