#pragma once

#include <iostream>
#include <GLFW/glfw3.h>
#include "Color.hpp"

class Window
{
    public:
        Window(const char* caption, unsigned int width, unsigned int height);

        unsigned int get_width();
        unsigned int get_height();

        bool window_should_close();

        void swap_buffers();
        void poll_events();
        void clear();
        void set_bg_color(float r, float g, float b, float a);
        void process_window_related_input();
        void set_window_should_close(bool value);

    private:
        unsigned int m_Width, m_Height;
        const char* m_Caption;

        Color m_BGColor;
        GLFWwindow* m_GLFWWindow;

        void initialize_window();
        void set_window_hints();
};