from pynput import mouse, keyboard

def on_move(x, y):
    print("Mouse is moving.")

def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    pass

def on_press(key):
    pass

def on_release(key):
    pass

# Create instances of the mouse listener and keyboard listener
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listeners
with mouse_listener, keyboard_listener:
    # Keep the main thread running to continuously check if the mouse is moving
    keyboard_listener.join()
