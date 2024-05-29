import glfw
from OpenGL.GL import *
import numpy as np

# Global variable
type = GL_LINE_LOOP

def render(vertices):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glBegin(type)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global type

    if action == glfw.PRESS:
        if key == glfw.KEY_1:
            type = GL_POINTS
        elif key == glfw.KEY_2:
            type = GL_LINES
        elif key == glfw.KEY_3:
            type = GL_LINE_STRIP
        elif key == glfw.KEY_4:
            type = GL_LINE_LOOP
        elif key == glfw.KEY_5:
            type = GL_TRIANGLES
        elif key == glfw.KEY_6:
            type = GL_TRIANGLE_STRIP
        elif key == glfw.KEY_7:
            type = GL_TRIANGLE_FAN
        elif key == glfw.KEY_8:
            type = GL_QUADS
        elif key == glfw.KEY_9:
            type = GL_QUAD_STRIP
        elif key == glfw.KEY_0:
            type = GL_POLYGON

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480, 480, "2022031994-2-1", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.set_key_callback(window, key_callback)

    # Make the window's context current
    glfw.make_context_current(window)

    
    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Define dodecagon vertices
        center = (0, 0)
        radius = 1
        num_sides = 12
        angles = np.linspace(0, 2*np.pi, num_sides, endpoint=False)
        vertices = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]

        # Poll events
        glfw.poll_events()

        # Render here
        render(vertices)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()