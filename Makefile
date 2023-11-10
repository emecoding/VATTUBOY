GPP_FLAGS = -std=c++11 -lglfw -lGL -ldl -L $(FILES_TO_BUILD_INCLUDE)

FINAL_EXECUTABLE_FILE = VATTUBOY

FILES_TO_BUILD_SRC := $(wildcard src/*.cpp)
FILES_TO_BUILD_GLAD := $(wildcard glad/*.c)
FILES_TO_BUILD_INCLUDE := $(wildcard include/*.hpp)

run:
	./$(FINAL_EXECUTABLE_FILE)

build:
	g++ $(FILES_TO_BUILD_SRC) $(FILES_TO_BUILD_GLAD) -o $(FINAL_EXECUTABLE_FILE) $(GPP_FLAGS) 

all:
	make build
	echo -----------------
	make run
	
