from pynput.keyboard import Key, Listener
import threading
import time

# Flags to control the looping action and process termination
is_looping = False
exit_program = False

def perform_looping_action():
    """Function to perform the desired looping action."""
    global is_looping
    while is_looping:
        # Placeholder for the actual looping action
        print("Performing looping action...")
        time.sleep(1)  # Simulating work with a sleep

def on_press(key):
    """Handle key press event."""
    global is_looping, exit_program

    # Start the looping action with a specific shortcut, e.g., Ctrl+L
    if key == Key.ctrl_l:  # Assuming 'L' key starts the loop
        if not is_looping:
            is_looping = True
            # Starting the looping action in a separate thread
            threading.Thread(target=perform_looping_action).start()

    # Stop the looping action with the spacebar
    elif key == Key.space:
        is_looping = False

    # Exit the program with the Esc key
    elif key == Key.esc:
        is_looping = False
        exit_program = True
        return False  # Stop listening

def on_release(key):
    """Handle key release event."""
    # This function is required by the Listener but doesn't need additional logic for this script

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# After exiting the listener, check if the program should terminate
if exit_program:
    print("Exiting program.")
