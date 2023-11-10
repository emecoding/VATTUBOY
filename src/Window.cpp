#include "../include/Window.hpp"

Window::Window(const char* caption, unsigned int width, unsigned int height)
{
    this->m_Caption = caption;
    this->m_Width = width;
    this->m_Height = height;

    this->initialize_window();
}

void Window::initialize_window()
{
    this->set_window_hints();

    this->m_GLFWWindow = glfwCreateWindow(this->m_Width, this->m_Height, this->m_Caption, NULL, NULL);
    if (this->m_GLFWWindow == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
    }

    glfwMakeContextCurrent(this->m_GLFWWindow);
}

void Window::set_window_hints()
{
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
}

void Window::clear()
{
    glClearColor(this->m_BGColor.r, this->m_BGColor.g, this->m_BGColor.b, this->m_BGColor.a);
    glClear(GL_COLOR_BUFFER_BIT);
}

void Window::set_bg_color(float r, float g, float b, float a)
{ 
    this->m_BGColor.r = r;
    this->m_BGColor.g = g;
    this->m_BGColor.b = b;
    this->m_BGColor.a = a;
}

void Window::process_window_related_input()
{
    if(glfwGetKey(this->m_GLFWWindow, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        this->set_window_should_close(true);
}

void Window::set_window_should_close(bool value) { glfwSetWindowShouldClose(this->m_GLFWWindow, value); }

void Window::swap_buffers() { glfwSwapBuffers(this->m_GLFWWindow); }

void Window::poll_events() { glfwPollEvents(); }

bool Window::window_should_close() { return glfwWindowShouldClose(this->m_GLFWWindow); }

unsigned int Window::get_width() { return this->m_Width; }

unsigned int Window::get_height() { return this->m_Height; }

