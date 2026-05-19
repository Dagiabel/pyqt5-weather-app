# PyQt5 Desktop Weather Application

A clean, responsive desktop application built with Python and PyQt5 that displays real-time weather information using the OpenWeatherMap REST API. 

## Features
* **Live Data Fetching:** Fetches temperature, weather conditions, and icons globally.
* **Smart Day/Night Detection:** Automatically toggles between daytime (☀️) and nighttime (🌙) emojis based on the target city's local time.
* **Robust Error Handling:** Handles timeouts, network disconnections, and invalid city names (HTTP 404 errors) gracefully without crashing.
* **Modern QSS Styling:** Custom desktop interface styled with CSS-like stylesheet rules.

## Tech Stack
* **Language:** Python 3
* **GUI Framework:** PyQt5
* **Networking:** Requests (HTTP Library)
 


## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dagiabel/pyqt5-weather-app.git
   ```


2. Install dependencies:
   ```bash
   pip install PyQt5 requests
   ```
3. Run the application:
   ```bash
   python weather_app.py
   ```

