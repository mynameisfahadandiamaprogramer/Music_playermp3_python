from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Initialize Tkinter window and Pygame mixer
root = Tk()
mixer.init()

# Function to create the widgets
def create_widgets():
    # Track label
    track_label = Label(root, text="Select Audio Track", bg="lightskyblue", font=("Arial", 15))
    track_label.grid(row=0, column=0, padx=20, pady=20)

    # Entry field for track path
    global entry
    entry = Entry(root, font=("Arial", 15), width=35)
    entry.grid(row=0, column=1, padx=20, pady=20)

    # Search button to browse files
    browse_button = Button(root, text="Search", bg="deeppink", font=("Arial", 15), width=20, bd=5, activebackground="green", command=browse_file)
    browse_button.grid(row=0, column=2, padx=20, pady=20)

    # Play button
    play_button = Button(root, text="Play", bg="deeppink", font=("Arial", 15), width=20, bd=5, activebackground="green", command=play_music)
    play_button.grid(row=1, column=0, padx=20, pady=20)

    # Pause button
    pause_button = Button(root, text="Pause", bg="deeppink", font=("Arial", 15), width=20, bd=5, activebackground="green", command=pause_music)
    pause_button.grid(row=1, column=1, padx=20, pady=20)

    # Volume up button
    volume_up_button = Button(root, text="Volume Up", bg="deeppink", font=("Arial", 15), width=20, bd=5, activebackground="green", command=volume_up)
    volume_up_button.grid(row=1, column=2, padx=20, pady=20)

    # Stop button
    stop_button = Button(root, text="Stop", bg="deeppink", font=("Arial", 15), width=20, bd=5, activebackground="green", command=stop_music)
    stop_button.grid(row=2, column=0, padx=20, pady=20)

    # Volume down button
    volume_down_button = Button(root, text="Volume Down", bg="deeppink", font=("Arial", 15), width=20, bd=5, activebackground="green", command=volume_down)
    volume_down_button.grid(row=2, column=2, padx=20, pady=20)

# Function to browse and select a file
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if filename:
        entry.delete(0, END)
        entry.insert(0, filename)

# Function to play the selected music file
def play_music():
    track = entry.get()
    if track:
        mixer.music.load(track)
        mixer.music.play()

# Function to pause the music
def pause_music():
    mixer.music.pause()

# Function to stop the music
def stop_music():
    mixer.music.stop()

# Function to increase the volume
def volume_up():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(min(volume + 0.1, 1.0))  # Limit volume to 1.0

# Function to decrease the volume
def volume_down():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(max(volume - 0.1, 0.0))  # Limit volume to 0.0

# Set up the main window
root.title("Simple Music Player")
root.geometry("1100x500")
root.resizable(False, False)
root.configure(bg="lightskyblue")

# Add slider text
ss = "Developed by Fahad"
slider_label = Label(root, text=ss, bg="lightskyblue", font=("Arial", 15))
slider_label.grid(row=3, column=0, padx=20, pady=20, columnspan=3)

# Call the function to create widgets
create_widgets()

# Run the Tkinter event loop
root.mainloop()
