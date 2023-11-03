#include "Display.h"

struct GameObject
{
    float x, y;
    float width, height;
    Color color;
};

void RenderGameObject(GameObject object);