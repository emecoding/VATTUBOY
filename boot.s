[org 0x7c00]
[bits 16]

; bootloader

mov bx, 0x1000
mov ah, 0x02
mov al, 30
mov ch, 0x00
mov dh, 0x00
mov cl, 0x02

int 0x13

; switch to graphics mode

mov ah, 0x00
mov al, 0x13
int 0x10

; Switch to proteced mode

cli
lgdt [GDT_DESC]

mov eax, cr0
or eax, 0x1
mov cr0, eax

; Jump to 32 bit code

jmp CODE_SEG:INIT_PM

[bits 32]

INIT_PM:
mov ax, DATA_SEG
mov ds, ax
mov ss, ax
mov es, ax
mov fs, ax
mov gs, ax

mov ebp, 0x90000
mov esp, ebp


call 0x1000
jmp $

GDT_BEGIN:

GDT_NULL_DESC:
    dd 0x0
    dd 0x0

GDT_CODE_SEG:
    dw 0xffff
    dw 0x0
    db 0x0
    db 10011010b
    db 11001111b
    db 0x0

GDT_DATA_SEG:
    dw 0xffff
    dw 0x0
    db 0x0
    db 10010010b
    db 11001111b
    db 0x0

GDT_END:

GDT_DESC:
    dw GDT_END - GDT_BEGIN -1
    dd GDT_BEIN

CODE_SEG equ GDT_CODE_SEG - GDT_BEGIN
DATA_SEG equ GDT_DATA_SEG - GDT_BEGIN

times 510-($-$$) db 0
dw 0xaa55