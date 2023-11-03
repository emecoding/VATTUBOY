#include "Display.h"

void FillBackground(int color)
{
    char *video_buffer = (char*) 0xA0000;
    for(int x = 0; x < 320; x++)
    {
        for(int y = 0; y < 200; y++)
        {
            int i = x + y;
            *(video_buffer + i) = color;
        }
    }
}