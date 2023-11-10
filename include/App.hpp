#pragma once

#define DEFAULT_WINDOW_WIDTH 800
#define DEFAULT_WINDOW_HEIGHT 600

#include <iostream>

#include "../glad/glad.h"
#include <GLFW/glfw3.h>

#include "Window.hpp"
#include "Color.hpp"

class App
{
    public:
        App();

        void run();
        void terminate();

        Window* get_window();

    private:
        void initialize_glfw();
        void initialize_glad();
         

        Window* m_Window;
};