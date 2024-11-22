# Happy Weather Woman

## Overview
Happy Weather Woman is a fun and interactive weather application built using Python. It provides real-time weather updates for any city using the OpenWeatherMap API, integrates text-to-speech functionality to read out the weather conditions, and includes animated visuals for an engaging user experience.

## Features
- Real-time weather updates for any city.
- Text-to-speech functionality to announce the weather.
- Animated interface with images to simulate speaking.

## Prerequisites
To run this application, ensure you have the following installed:

- Python 3.7 or above
- `pip` (Python package installer)
- An OpenWeatherMap API key

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your_username/happy-weather-woman.git
   cd happy-weather-woman
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r woman_requirements.txt
   ```

3. Place the required image files in the project directory:
   - `woman_stays.PNG`: Static image for idle state.
   - `woman_talks.PNG`: Speaking image for animation.

4. Set up your OpenWeatherMap API key as an environment variable:
   - On Linux/MacOS:
     ```bash
     export OPENWEATHER_API_KEY="your_api_key"
     ```
   - On Windows:
     ```cmd
     set OPENWEATHER_API_KEY="your_api_key"
     ```

   Replace `your_api_key` with your OpenWeatherMap API key.

## Usage

1. Run the application:
   ```bash
   python weather_woman.py
   ```

2. Enter the name of a city in the input field and press the `Enter` key.

3. The app will fetch the weather details, display them, and read them aloud using text-to-speech.

## File Structure
```
.
├── woman_stays.PNG        # Static image for idle state
├── woman_talks.PNG        # Speaking image for animation
├── weather_woman.py       # Main application script
├── woman_requirements.txt # Dependencies list
├── woman_readme.md        # Instructions for usage
```

## Dependencies
The app requires the following Python libraries:

- `tkinter`: Built-in Python library for GUI development.
- `Pillow`: For image handling.
- `requests`: To fetch weather data from OpenWeatherMap API.
- `pyttsx3`: For text-to-speech functionality.

## Contributing
Contributions are welcome! Feel free to submit a pull request r create an issue for any bugs or feature suggestions.

## License
This project is licensed under the Harbour Space University.

---

Happy Weather Woman makes weather updates more fun and engaging. Enjoy exploring the weather with a smile!

