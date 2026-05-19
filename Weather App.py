print("*****Weather API App*****")
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,  QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class Weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.city_quest_label = QLabel("Enter a city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.weather_description = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_quest_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.weather_description)

        self.setLayout(vbox)

        self.city_quest_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.weather_description.setAlignment(Qt.AlignCenter)

        self.setObjectName("Main_window")
        self.city_quest_label.setObjectName("city_quest_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.weather_description.setObjectName("weather_description")

        self.setStyleSheet("""
                        #Main_window{
                           background-color: hsl(193, 14%, 48%)
                           }

                        QLabel, QPushButton {
                           font-family: calibri;
                           }

                        QLabel#city_quest_label {
                           font-size: 40px;
                           font-style: italic;
                           }

                        QLineEdit#city_input {
                           font-size: 40px;
                           background-color: hsl(194, 8%, 62%)
                           }

                        QPushButton#get_weather_button {
                           font-size: 30px;
                           font-weight: bold;
                           background-color: hsl(194, 8%, 62%)
                           }

                        QLabel#temperature_label{
                           font-size: 75px;
                           }

                        QLabel#emoji_label{
                           font-size: 100px;
                           font-family: segoe UI emoji;
                           }

                        QLabel#weather_description{
                           font-size: 50px;
                           }

        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "966773e235c44c8a4eaa6e817ab5b978"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request: \nPlease check your input")  
                case 401:
                    self.display_error("Unauthorized: \nInvalid API key")
                case 403:
                    self.display_error("Forbidden: \nAccess is denied")
                case 404:
                    self.display_error("Not found: \nCity not found")
                case 500:
                    self.display_error("Internal Server Error: \nPlease try again later")  
                case 502:
                    self.display_error("Bad Gateway: \nInvalid response from the server")  
                case 503:
                    self.display_error("Service Unavailable: \nServer is down")  
                case 504:
                    self.display_error("Gateway Timeout: \nNo response from the server")
                case _:
                    self.display_error(f"HTTP Error: \n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: \nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error: \nThe request timed out")

        except requests. exceptions.TooManyRedirects:
            self.display_error("Too many Redirects: \nCheck the URL")

        except requests. exceptions. RequestException as req_error:
            self.display_error(f"Request Error: \n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.weather_description.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15

        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"]
        weather_icon = data["weather"][0]["icon"]  # 1. Get the icon code (e.g., '01n')

        self.temperature_label.setText(f"{temperature_c: .0f}°C")
        # 2. Pass both the weather ID and icon string to the function
        self.emoji_label.setText(self.display_emoji(weather_id, weather_icon)) 
        self.weather_description.setText(weather_desc)


    @staticmethod
    def display_emoji(weather_id, weather_icon):
        is_night = weather_icon.endswith("n")  # Checks if it is night time

        if 200 <= weather_id <= 232:
            return "⛈️"
        
        elif 300 <= weather_id <= 321:
            return "🌦️"
        
        elif 500 <= weather_id <= 531:
            return "🌧️"
        
        elif 600 <= weather_id <= 622:
            return "❄️"
        
        elif 701 <= weather_id <= 741:
            return "🌫️"
        
        elif weather_id == 762:
            return "🌋"
        
        elif weather_id == 771:
            return "💨"
        
        elif weather_id == 781:
            return "🌪️"
        
        elif weather_id == 800:
            return "🌙" if is_night else "☀️"  # Moon if night, Sun if day
        
        elif 801 <= weather_id <= 804:
            return "☁️" if is_night else "☁️"   # Optional: "☁️" vs "⛅" for day
        
        else:
            return ""

    
def main():
    app = QApplication(sys.argv)
    weather_app = Weather_app()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()