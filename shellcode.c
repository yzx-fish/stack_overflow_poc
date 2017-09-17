int main()
{
        __asm__(
        "jmp S2\n\t"
"S1:pop %esi\n\t"
    "movl %esi,0x13(%esi)\n\t"
        "xorl %edx,%edx\n\t"
        "movl %edx,0x1b(%esi)\n\t"
        "movl %edx,0x17(%esi)\n\t"
        "movb %dl,0x12(%esi)\n\t"

        "xor %eax,%eax\n\t"
        "movb $0xb,%al\n\t"  //eax
        "mov %esi,%ebx\n\t"  //ebx
        "lea 0x13(%esi),%ecx\n\t" //ecx, and edx=0
        "int $0x80\n\t"      //execve

        "movb $0x01,%al\n\t"
        "mov %edx,%ebx\n\t"
        "int $0x80\n\t"    //exit(0)

"S2:call S1\n\t"
        ".string \"/usr/bin/touch ttt aaaabbbbcccc\"");
}