#include "../include/Shader.hpp"

Shader::Shader(const char* vertex_path, const char* fragment_path)
{
    std::string vertex_file_data = this->read_data_from_shader_file(vertex_path);
    std::string fragment_file_data = this->read_data_from_shader_file(fragment_path);


    unsigned int vertex_shader = this->create_shader(GL_VERTEX_SHADER, vertex_file_data.c_str());
    unsigned int fragment_shader = this->create_shader(GL_FRAGMENT_SHADER, fragment_file_data.c_str());

    this->m_ID = this->create_shader_program(vertex_shader, fragment_shader);
}

std::string Shader::read_data_from_shader_file(const char* path)
{
    std::ifstream shader_file;
    std::string shader_code;
    const char* data;

    try
    {
        shader_file.open(path);
        std::stringstream shader_stream;

        shader_stream << shader_file.rdbuf();  

        shader_file.close();        

        shader_code = shader_stream.str();
        data = shader_code.c_str();
    }
    catch(std::ifstream::failure& e)
    {
        std::cout << "Error in shader '" << path << "': " << e.what() << std::endl;
    }

    return data;
}

unsigned int Shader::create_shader(unsigned int shader_type, const char* shader_data)
{
    unsigned int shader = glCreateShader(shader_type);
    glShaderSource(shader, 1, &shader_data, NULL);
    glCompileShader(shader);

    int success;
    char infoLog[512];
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if(!success)
    {
        glGetShaderInfoLog(shader, 512, NULL, infoLog);
        std::cout << "Failed to compile shader '" << shader_type << "', :" << infoLog << std::endl; 
    }

    return shader;
}

unsigned int Shader::create_shader_program(unsigned int vertex_shader, unsigned int fragment_shader)
{
    unsigned int program = glCreateProgram();
    glAttachShader(program, vertex_shader);
    glAttachShader(program, fragment_shader);
    glLinkProgram(program);

    int success;
    char infoLog[512];

    glGetProgramiv(program, GL_LINK_STATUS, &success);
    if(!success)
    {
        glGetProgramInfoLog(program, 512, NULL, infoLog);
        std::cout << "Failed to link shader: " << infoLog << std::endl;
    }

    glDeleteShader(vertex_shader);
    glDeleteShader(fragment_shader);

    return program;
}

unsigned int Shader::get_ID() { return this->m_ID; }