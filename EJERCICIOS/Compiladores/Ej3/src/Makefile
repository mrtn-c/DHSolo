BUILD = ../build
LDIR = ../libs
DEPS = main.c $(LDIR)/sumar.c $(LDIR)/sumar.h
CFLAGS = -Wall

all : pc 

main.o: main.c
		gcc -c $(CFLAGS) main.c

sumar.o: sumar.h
		gcc -c $(CFLAGS) sumar.h

exec: main.o sumar.o
		gcc main.o sumar.o

pc: $(DEPS)
	mkdir -p $(BUILD)
	gcc $(CFLAGS) -o $(BUILD)/pc -I$(LDIR) main.c $(LDIR)/sumar.c
		
clean:
	rm -rf $(BUILD)