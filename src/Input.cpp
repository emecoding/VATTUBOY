#include "../include/Input.hpp"

Input::Input(GLFWwindow* glfw_window)
{
    this->m_GlfwWindow = glfw_window;
}

bool Input::key_pressed(unsigned int key)
{
    return glfwGetKey(this->m_GlfwWindow, key) == GLFW_PRESS;
}