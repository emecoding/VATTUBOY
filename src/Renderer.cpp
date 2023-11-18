#include "../include/Renderer.hpp"

Renderer::Renderer()
{

}

unsigned int Renderer::generate_triangle()
{
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

    return VAO;
}

void Renderer::use_vertex_array(unsigned int VAO)
{
    glBindVertexArray(VAO);
}

void Renderer::render_vertex_array(unsigned int mode, unsigned int first_vertex, unsigned int last_vertex)
{
    glDrawArrays(GL_TRIANGLES, first_vertex, last_vertex);
}