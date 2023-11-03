#include "GameObject.h"

void RenderGameObject(GameObject object)
{
    char *video_buffer = (char*) 0xA0000;
    for(int x = (int)object.x; x < object.width; x++)
    {
        for(int y = (int)object.y; y < object.height; y+=320)
        {
            int i = x + y;
            *(video_buffer + i) = object.color;
        }
    }
}