#!/bin/sh

BIN_DIR="bin"

GCC_FLAGS="-m32 -ffreestanding"
LD_FALGS="-Ttext 0x1000 $BIN_DIR/entry.bin $BIN_DIR/kernel.o $BIN_DIR/IDT.bin"

SYSTEM_ARCH="i386"
QEMU_FLAGS="-drive format=raw,file=$BIN_DIR/kernel.img"

nasm boot.s -f bin -o $BIN_DIR/bootsect.bin
nasm kernel-entry.s -f elf -o $BIN_DIR/entry.bin
nasm IDT.s -f elf -o $BIN_DIR/IDT.bin

gcc $GCC_FLAGS -c *.c -o $BIN_DIR/kernel.o

ld -T NUL -o $BIN_DIR/kernel.img $LD_FALGS

qemu-system-$SYSTEM_ARCH $QEMU_FLAGS