global array_alloc:

section .text

array_alloc:
    ;  Total size =  elementSize * numElements
    mov rax, rdi        ; rax = element size
    mul rsi             ; rax = rax * rsi (total size)

    ; Prepare arguments for mmap syscall
    xor rdi, rdi        ; addr = NULL (let the system choose the address)
    mov rsi, rax        ; length = size (calculated above)
    mov rdx, 7          ; prot = PROT_READ | PROT_WRITE | PROT_EXEC
    mov r10, 0x22       ; flags = MAP_PRIVATE | MAP_ANONYMOUS
    mov r8, -1          ; fd = -1 (anonymous mapping, not backed by any file)
    xor r9, r9          ; offset = 0

    ; System call number for mmap (x86-64 Linux)
    mov rax, 9          ; syscall number for mmap
    syscall             ; call kernel

    ; Check for mmap error (returns -1 on error)
    cmp rax, 0xFFFFFFFFFFFFFFFF
        je array_alloc_error   ; Jump to error handling if allocation failed

    ret                 ; Return the pointer in rax

array_alloc_error:
    xor rax, rax        ; Return NULL pointer in case of error
    ret