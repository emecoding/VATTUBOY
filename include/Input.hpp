#pragma once

#include <GLFW/glfw3.h>

class Input
{
    public:
        Input(GLFWwindow* glfw_window);

        bool key_pressed(unsigned int key);

    private:
        GLFWwindow* m_GlfwWindow;
};