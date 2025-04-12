.section .data
msg:
    .asciz "Hello, RISC-V!\n"

.section .text
.global _start
_start:
    # Write system call
    li a7, 64       # syscall write
    li a0, 1        # stdout
    la a1, msg       # load message address
    li a2, 15       # message length (corrected)
    ecall           # make syscall

    # Exit system call
    li a7, 93       # syscall exit
    li a0, 0        # exit code
    ecall
