# Python Trading Strategy Project

## Project Overview

This project implements a simple stock trading strategy using technical indicators such as Bollinger Bands and Relative Strength Index (RSI). It automatically fetches historical stock data, computes technical indicators, applies a trading strategy, visualizes the results, and generates reports.

The goal of the project is to allow easy exploration of strategy performance across different parameters:
- **Bollinger Band window sizes (`w_bb`)**
- **RSI window sizes (`w_rsi`)**
- **Bollinger Band factors**

Users can visualize how different settings affect strategy returns.

> **Important:** This project is **heavily based** on the initial work presented by **Ubey Ozcan** in one of his courses available here: [UbeyOzcan's UCLouvain LSM Python Finance GitHub Repository](https://github.com/UbeyOzcan/UCLouvain-LSM-Python-Finance/tree/main). We are extremely grateful for his contribution to the educational community.

> **Main Contribution:** This project expands upon the original work by providing an **in-depth analysis** of how the parameters of the algorithm affect the overall return achieved by the trading strategy. Parameter sweeps and visualizations have been added to better understand the impact of Bollinger Band window sizes, RSI window sizes, and band factors.

## Project Structure

```bash
project_root/
├── Data/       # Data download (Yahoo Finance)
├── Plot/       # Visualization tools (matplotlib)
├── Reporting/  # Report generation (Excel, JSON)
├── Strategy/   # Trading logic (Buy/Sell signals)
├── TI/         # Technical Indicators (MA, Volatility, Bollinger Bands, RSI)
├── main.py     # Main script to execute the whole pipeline
└── README.md   # This file
```

## Main Features

- Download stock data using **yfinance**
- Compute technical indicators using **pandas** and **ta**
- Apply a Bollinger Band + RSI trading strategy
- Visualize results:
  - Entry/Exit points
  - Bollinger Bands and Closing Prices
  - RSI evolution
- Generate reports:
  - Excel file with full data
  - JSON file with transaction details
- Perform parameter grid searches to optimize the strategy
- Create 3D surface plots of returns versus parameter combinations

## Requirements

- Python 3.8+
- Required libraries:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `ta`

Install all dependencies via pip:
```bash
pip install yfinance pandas numpy matplotlib ta
```

## Running the Project

Simply run `main.py`:

```bash
python main.py
```

By default, it will:
- Download Apple's historical stock data.
- Compute indicators.
- Apply the trading strategy.
- Plot and save results.
- Generate Excel and JSON reports.

You can also run parameter grid searches by calling dedicated functions inside `main.py`.

---

**Again, full credit to [Ubey Ozcan](https://github.com/UbeyOzcan) for the initial project inspiration!**

---

## Disclaimer

This project is for **educational purposes only**. It does not constitute financial advice. Trading and investing involve significant financial risk.

