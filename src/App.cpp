

#include "../include/App.hpp"

#include <cmath>

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
    Shader shader = Shader("res/shaders/vertex_shader.vs", "res/shaders/fragment_shader.fs");

    float vertices[] = {
        0.5f, -0.5f, 0.0f,
        -0.5f, -0.5f, 0.0f,
        0.0f, 0.5f, 0.0f
    };

    unsigned int VBO, VAO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    
    glBindVertexArray(VAO);

    while(!this->m_Window->window_should_close())
    {
        this->m_Window->process_window_related_input();

        this->m_Window->clear();

        glUseProgram(shader.get_ID());

        double time = glfwGetTime();
        float green = static_cast<float>(sin(time) / 2.0 + 0.5);

        int color_loc = glGetUniformLocation(shader.get_ID(), "color");
        glUniform4f(color_loc, 0.0f, green, 0.0f, 1.0f);

        glDrawArrays(GL_TRIANGLES, 0, 3);

        this->m_Window->swap_buffers();
        this->m_Window->poll_events();
    }
}

void App::terminate()
{
    glfwTerminate();
}

Window* App::get_window() { return this->m_Window; }