# Stock Market Analyzer with Zerodha Kite API

This project is a stock market analyzer that utilizes the Zerodha Kite API for fetching real-time market data, historical data, and technical indicators. The analyzer provides insights into various technical indicators and also includes a pattern scanner to identify significant trends in the market.

## Table of Contents

- [Introduction](#introduction)
- [Technical Indicators](#technical-indicators)
- [Pattern Scanner](#pattern-scanner)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Stock Market Analyzer is built using the Zerodha Kite API, which allows fetching real-time data, historical data, and performing technical analysis on stocks. It aims to provide traders and investors with valuable insights into market trends, helping them make informed decisions.

## Technical Indicators

The project includes a set of commonly used technical indicators in the `/Technical Indicators` folder:

- **ADX (Average Directional Index):** Measures the strength of a trend in the market.
- **ATR (Average True Range):** Indicates market volatility and potential price movement.
- **Bollinger Bands:** Consists of a middle band (SMA) and upper/lower bands that represent price volatility.
- **MACD (Moving Average Convergence Divergence):** Shows the relationship between two moving averages.
- **RSI (Relative Strength Index):** Measures the speed and change of price movements.
- **Supertrend:** A trend-following indicator that helps identify potential buy/sell signals.

## Pattern Scanner

Apart from technical indicators, the project also includes a pattern scanner that utilizes the Zerodha Historical API. This scanner compares the trend of the previous week with the trend of the previous day for each instrument. It assigns a significance level (HIGH or LOW) to each instrument, helping traders identify relevant stocks of interest for the next trading day.

## Usage

1. Clone the repository and navigate to the project directory.
2. Set up your Zerodha Kite API credentials.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Explore the `/Technical Indicators` folder for individual indicator implementations.
5. Run the pattern scanner to identify significant trends using historical data.
6. Make use of the generated insights to make informed trading decisions.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or improvement.
3. Make your changes and write tests if necessary.
4. Test your changes thoroughly.
5. Create a pull request describing your changes and their benefits.

## License

This project is licensed under the [MIT License](LICENSE).
