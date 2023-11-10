

#include "../include/App.hpp"

App::App()
{
    this->initialize_glfw();

    this->m_Window = new Window("VATTUBOY", DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT);
    this->m_Window->set_bg_color(0.2f, 0.3f, 0.3f, 1.0f);

    this->initialize_glad();
}

void App::initialize_glfw()
{
    if(!glfwInit())
    {
        std::cout << "Failed to initialize glfw" << std::endl;
    }
}

void App::initialize_glad()
{
    if(!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress))
    {
        std::cout << "Failed to initialize glad" << std::endl;
    }
}

void App::run()
{
    while(!this->m_Window->window_should_close())
    {
        this->m_Window->clear();

        this->m_Window->process_window_related_input();

        this->m_Window->swap_buffers();
        this->m_Window->poll_events();
    }
}

void App::terminate()
{
    glfwTerminate();
}

Window* App::get_window() { return this->m_Window; }