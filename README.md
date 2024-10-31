# Radio Control

## Description

Radio Control is an application designed for Raspberry Pi that enables you to play internet radio stations. By connecting an FM transmitter to the Raspberry Pi, you can listen to your favorite radio stations on a traditional FM radio in your vicinity. The application is user-friendly - simply log into the web interface hosted by the Raspberry Pi and select the station you want to play.

## Requirements

- Raspberry Pi with Raspbian or another Linux-based OS
- Connected FM transmitter
- Python 3
- Flask (to run the web server)
- Necessary libraries for FM transmitter support

## Installation

1. **Clone the repository to your Raspberry Pi:**
   ```bash
   git clone https://github.com/unknow1192/radio-control.git
   cd radio-control
   ```

2. **Install required packages:**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-flask vlc
   ```

3. **Configure the FM transmitter:**  
   Ensure that the FM transmitter is properly connected and configured. Refer to your transmitter’s documentation for the appropriate settings.

4. **Add radio stations:**  
   Edit the `stations.py` file to include your favorite radio stations. Make sure the format is compatible with the application.

## Running the Application

1. **Start the application:**
   ```bash
   python3 radio-control.py
   ```

2. **Visit the web interface:**
   Open a web browser on another device in the same network and navigate to:
   ```
   http://<Raspberry_Pi_IP_Address>:5000
   ```
   Replace `<Raspberry_Pi_IP_Address>` with the IP address of your Raspberry Pi. Run:
   ```bash
   hostname -I
   ```
   to get your IP

3. **Select a radio station:**  
   Choose a station from the list on the web page and click the button to start streaming. The radio should begin broadcasting on the FM frequency.

## Usage

- The application allows easy switching between different radio stations.
- You can enjoy music, shows, and news on your FM radio without needing a direct internet connection on the receiver.

## Support

If you encounter any issues or have questions about the application, feel free to open an issue in this repository or contact the author.

## License

This repository is licensed under the MIT License. Please refer to the `LICENSE` file for more details.

---

Thank you for using Radio Control! We’re excited to support your radio experience on Raspberry Pi!
