#pragma once

#include "../glad/glad.h"
#include <GLFW/glfw3.h>

class Renderer
{
    public:
        Renderer();

        unsigned int generate_triangle();

        void use_vertex_array(unsigned int VAO);
        void render_vertex_array(unsigned int mode, unsigned int first_vertex, unsigned int last_vertex);
};