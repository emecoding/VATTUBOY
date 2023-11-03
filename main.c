#include "GameObject.h"
#include "Display.h"

int start()
{
    struct GameObject my_object;
    my_object.x = 100.0f;
    my_object.y = 100.0f;
    my_object.width = 32.0f;
    my_object.height = 32.0f;
    my_object.color = 0x00++;

    FillBackground(0x00+=3);
    RenderGameObject(my_object);
}