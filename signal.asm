section .text  
  
global _start  
  
 _start:

     xor rax, rax
     add al, 0x3e ; sys_kill (syscall 62)
     xor rdi, rdi
     add rdi, 0xfbb3 ;insert PID here
     push 0x0a ; sigkill (code 09), sigusr1 (code 0a)
     pop rsi
     syscall