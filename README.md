# Voice Assistant

A powerful and efficient voice assistant built using Python that recognizes voice commands to perform a variety of tasks such as opening and closing applications, searching Wikipedia, taking screenshots, and shutting down the system. This project demonstrates the integration of speech recognition, text-to-speech synthesis, and automation tools to create a hands-free experience.

## Features 🚀
- 🎤 **Voice Command Recognition**: Uses Google Speech Recognition to process spoken commands.
- 🖥️ **Open Applications**: Launches Chrome, Notepad, and Microsoft Word using voice commands.
- ❌ **Close Applications**: Terminates running instances of Chrome, Notepad, and Microsoft Word.
- 📸 **Screenshot Capture**: Takes a screenshot and saves it automatically.
- 🔍 **Wikipedia Search**: Retrieves brief summaries from Wikipedia based on voice queries.
- 🖥️ **System Shutdown**: Allows users to shut down their system via voice command.

## Technologies Used 🛠️
- `SpeechRecognition` – Converts spoken language into text.
- `pyttsx3` – Converts text to speech for verbal responses.
- `wikipedia` – Fetches Wikipedia summaries.
- `pyautogui` – Automates GUI interactions (e.g., taking screenshots).
- `pyaudio` – Handles audio input from the microphone.

## Installation 📥
Ensure you have Python installed on your system. Then, install the required dependencies using:

```sh
pip install SpeechRecognition pyttsx3 wikipedia pyautogui pyaudio
```

If you face issues installing `pyaudio`, follow these platform-specific instructions:

- **Windows:** Download the correct `.whl` file from [this site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
  ```sh
  pip install path/to/downloaded/file.whl
  ```
- **Mac/Linux:**
  ```sh
  brew install portaudio
  pip install pyaudio
  ```

## How to Use 🎙️
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo-name
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the script:
   ```sh
   python filename.py
   ```

## Commands and Functionality 🗣️
| Command               | Action Performed |
|-----------------------|-----------------|
| "open Chrome"        | Launches Google Chrome |
| "open Notepad"       | Opens Notepad |
| "open Word"          | Starts Microsoft Word |
| "close Chrome"       | Terminates Chrome process |
| "close Notepad"      | Closes Notepad |
| "close Word"         | Closes Microsoft Word |
| "take a screenshot"  | Captures and saves a screenshot |
| "search <query>"     | Retrieves Wikipedia summary for `<query>` |
| "shutdown"           | Shuts down the computer |

## Notes 📝
- Ensure your microphone is properly configured and working.
- Some commands may not execute if the required applications are not installed.
- Wikipedia searches require an internet connection.

## Future Enhancements 🔮
- Implement natural language processing (NLP) for more intuitive command recognition.
- Add support for opening and closing additional applications.
- Integrate AI-based voice responses for a more interactive experience.


---
Feel free to contribute to this project by submitting pull requests or reporting issues! 🚀

