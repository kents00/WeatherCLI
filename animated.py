import time
import os

# Define your ASCII art frames
frames = [
    """
    (•_•)
    <) )╯   First frame
    / \\
    """,
    """
    ( •_•)
    /( (>   Second frame
    / \\
    """,
    """
    (•_•)
    <) )╯   Third frame
    / \\
    """
]

# Clear the console


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print frames


def print_frame(frame):
    clear()  # Clear the console
    print(frame)  # Print the frame

# Function to animate frames


def animate(frames, delay=0.1):
    for frame in frames:
        print_frame(frame)
        time.sleep(delay)


# Call the animate function
animate(frames)
