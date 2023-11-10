#include <iostream>
#include "../glad/glad.h"
#include <GLFW/glfw3.h>

#include "../include/App.hpp"


int main()
{
    App app = App();

    std::cout << "Hello VATTUBOY!" << std::endl;

    if(!glfwInit())
    {
        std::cout << "FUCK" << std::endl;
        return -1;
    }

    GLFWwindow* window = glfwCreateWindow(800, 600, "Lab3", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    if(!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
    {
        std::cout << "Failed to load opengl" << std::endl;
        return -1;
    }

    return 0;
}