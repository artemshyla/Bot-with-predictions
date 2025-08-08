# Bot-with-predictions

![Project Status](https://img.shields.io/badge/status-under%20development-yellow) 

A Telegram bot for stock price forecasting using LSTM neural networks. The project is currently in active development.

## ✨ Features

- **LSTM-based predictions** for stock prices
- **Telegram bot interface** for user interaction
- **Weekly model retraining** (planned via Airflow)
- **User database** (in development)
- **Multi-model support** architecture

## 🚧 Current Development Status

I am currently focused on:
- Finding the optimal LSTM model architecture
- Improving prediction speed and accuracy
- Building core bot functionality

## 📂 Project Structure

Bot-with-predictions/
├── app/
│ ├── handlers.py # Bot message handlers
│ ├── keyboards.py # Custom Telegram keyboards
│ ├── predictions.py # Price prediction functions
│ └── models/ # Trained LSTM models storage
├── lstm_learning.ipynb # Model development notebook
├── main.py # Main application entry point
├── requirements.txt # Python dependencies
├── LICENSE
└── README.md

## 🔧 Planned Improvements

- [ ] Implement user database
- [ ] Integrate with Airflow for scheduled retraining
- [ ] Add multi-stock support
- [ ] Optimize model performance
- [ ] Implement prediction confidence indicators

⚠️ Note: This project is under active development. The architecture and features may change significantly during development.