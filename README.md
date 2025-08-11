# 🌧 Rain Alert

**Rain Alert** is a simple Python script that fetches real-time weather data from an API and sends you an SMS notification about the current temperature and weather conditions.  
It uses the **Twilio API** for messaging and supports customizable locations and weather code descriptions.

---

## 📌 Features
- ✅ Fetches live weather data from a weather API  
- ✅ Parses weather codes and translates them into human-readable conditions  
- ✅ Sends SMS alerts directly to your phone via Twilio  
- ✅ Easy configuration with environment variables (no hardcoding API keys)  

---

## 🛠 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Thunderer9506/Rain_alert.git
cd Rain_alert
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**`requirements.txt`** should include:
```
requests
twilio
python-dotenv
```

### 3. Set up environment variables  
Create a `.env` file in the project root with:
```env
SID=your_twilio_account_sid
TOKEN=your_twilio_auth_token
FROM=your_twilio_phone_number
TO=recipient_phone_number
API_KEY=your_weather_api_key
LOC=your_location_code_or_coordinates
LINK=full_weather_api_request_url
```

---

## 📂 Project Files
- **`main.py`** – Core script to fetch weather data and send SMS  
- **`weather code.json`** – A mapping of weather codes to human-readable descriptions  
- **`.env`** – Your API keys, Twilio credentials, and configuration variables (not committed to GitHub)  

---

## 🚀 Usage
Run the script:
```bash
python main.py
```

The script will:
1. Load your credentials and API URL from `.env`
2. Request real-time weather data from the given API
3. Extract **temperature** and **weather code**
4. Match the weather code to a description from `weather code.json`
5. Send an SMS via Twilio with the formatted weather update

---

## 🔍 How It Works
1. **Environment Variables** – API keys and sensitive data are stored in `.env` for security.  
2. **API Request** – Sends a GET request to your specified weather API endpoint.  
3. **JSON Parsing** – Extracts `temperature` and `weatherCode` from the API response.  
4. **Weather Code Translation** – Looks up the code in `weather code.json` to get a readable description.  
5. **SMS Notification** – Formats a message and sends it via the Twilio API.  

**Example SMS Output:**
```
Hey Shaurya!
The current temperature is
Temp: 25°C
Weather code: 1000 (Clear Sky).
```

---

## ⚠️ Notes
- Make sure you have a Twilio account and a verified phone number.  
- The `weather code.json` file must match the codes returned by your chosen API.  
- You can schedule this script to run periodically using **cron jobs** (Linux/Mac) or **Task Scheduler** (Windows) to get regular updates.  

---

## 📄 License
This project is licensed under the MIT License.
