
# 🎵 Python Music Player 🎶

## Overview

A simple yet functional desktop music player built using **Python**, **Tkinter**, and **Pygame**. This project allows users to load `.mp3` songs, play, pause, stop, and navigate through their music with an interactive GUI.

## Features

- 🔊 Play, Pause, Stop, Previous, and Next song controls.
- 📁 Load single or multiple `.mp3` files.
- 📜 Playlist view using a scrollable Listbox.
- ⏱ Real-time song progress slider and timestamp.
- 🎵 Automatically loads songs from a `songs/` folder.
- 🎨 Custom control buttons using image icons.

## 🖥 GUI Preview

> GUI has buttons for control and a slider at the bottom for tracking or seeking through the song. Playlist is displayed as a list.

## 📂 Folder Structure
project/  
&nbsp; ├── songs/  
&nbsp; &nbsp; &nbsp; Directory containing your .mp3 songs   
&nbsp; ├── buttons/  
&nbsp; &nbsp; &nbsp; Contains control button images (play.png, pause.png, etc.)  
&nbsp; ├── main.py  
&nbsp; &nbsp; &nbsp; Main application code  
&nbsp; ├── README.md 

## 🛠 Requirements

- Python 3.x
- Required Libraries:
  - `pygame`
  - `mutagen`
  - `tkinter` (built-in with Python)


## Installation
### Prerequisites
- Python 3.x installed on your machine.
- Pip (Python package installer).

### Steps

#### 1. Clone the repository:

```bash
git clone https://github.com/viru757pan/Music-Player.git
```

#### 2. Navigate to the project directory:

```bash
cd music-player
```

#### 3. Run the game:

```bash
python main.py
```

## Usage

Once the installation is complete, you can run the game and start playing. Follow these steps to play the game:

#### 1. Running the Game:

After navigating to the project directory and activating the virtual environment (if used), run the following command to start the game:

```bash
python main.py
```

## How It Works
- Uses pygame.mixer for audio playback.
- mutagen is used to get metadata like song length.
- Tkinter's Listbox and ttk.Scale manage the playlist and progress bar.
- The slider is updated in real-time only when the song is playing.



## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please contact **[panchalviresh757@gmail.com]**.
