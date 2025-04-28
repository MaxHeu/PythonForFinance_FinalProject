from src.TI import TechInd
from src.Strategy import Strategy
from src.Plot import Plot
from src.Reporting import Report
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from src.TI import TechInd
from src.Strategy import Strategy

w_bb = 20
w_rsi = 6

def grid_search_returns_with_band(ticker: str, start_date: str, end_date: str):
    w_bb_values = range(5, 41)  # 5 to 40
    w_rsi_values = range(2, 16) # 2 to 15
    band_factors = np.linspace(0.5, 3.5, 7)  # 7 steps between 0.5 and 3.5

    for band_factor in band_factors:
        returns_matrix = np.zeros((len(w_bb_values), len(w_rsi_values)))

        for i, w_bb in enumerate(w_bb_values):
            for j, w_rsi in enumerate(w_rsi_values):
                TI = TechInd(ticker=ticker, start_date=start_date, end_date=end_date, window_bb=w_bb, window_rsi=w_rsi)
                df = TI.moving_average(df=TI.df)
                df = TI.rolling_vol(df=df)
                df = TI.bollinger_band(df=df, band_factor=band_factor)
                df = TI.rsi(df=df)

                ST = Strategy()
                result, _ = ST.bb_rsi(df=df, lower_rsi=30, upper_rsi=70)

                returns_matrix[i, j] = result['Return']

        # Now plot for this band_factor
        W_RSI, W_BB = np.meshgrid(w_rsi_values, w_bb_values)

        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(W_RSI, W_BB, returns_matrix, cmap='plasma')

        ax.set_xlabel('w_rsi')
        ax.set_ylabel('w_bb')
        ax.set_zlabel('Observed Return')
        ax.set_title(f'Return Surface for band_factor={band_factor:.2f}')
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.savefig(f'ReturnSurface_band_{band_factor:.2f}.png')
        plt.close()

def grid_search_returns(ticker: str, start_date: str, end_date: str):
    w_bb_values = range(5, 41)   # from 5 to 40
    w_rsi_values = range(2, 16)  # from 2 to 15

    returns_matrix = np.zeros((len(w_bb_values), len(w_rsi_values)))

    for i, w_bb in enumerate(w_bb_values):
        for j, w_rsi in enumerate(w_rsi_values):
            TI = TechInd(ticker=ticker, start_date=start_date, end_date=end_date, window_bb=w_bb, window_rsi=w_rsi)
            df = TI.moving_average(df=TI.df)
            df = TI.rolling_vol(df=df)
            df = TI.bollinger_band(df=df)
            df = TI.rsi(df=df)

            ST = Strategy()
            result, _ = ST.bb_rsi(df=df, lower_rsi=30, upper_rsi=70)

            returns_matrix[i, j] = result['Return']

    # Now plot
    W_RSI, W_BB = np.meshgrid(w_rsi_values, w_bb_values)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(W_RSI, W_BB, returns_matrix, cmap='viridis')

    ax.set_xlabel('w_rsi')
    ax.set_ylabel('w_bb')
    ax.set_zlabel('Observed Return')
    ax.set_title('Return Surface over w_rsi and w_bb')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.savefig('ReturnSurface.png')
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TI = TechInd(ticker='AAPL', start_date='2019-01-01', end_date='2025-04-14', window_bb=w_bb, window_rsi=w_rsi)
    df = TI.moving_average(df=TI.df)
    df = TI.rolling_vol(df=df)
    df = TI.bollinger_band(df=df)
    df = TI.rsi(df=df)
    ST = Strategy()
    result, df = ST.bb_rsi(df=df, lower_rsi=30, upper_rsi=70)
    Plot = Plot(df=df, result=result)
    Plot.scatter()
    Plot.plot_closing()
    Plot.plot_rsi()
    R = Report(df=df, result=result)
    R.ExcelReport()
    R.JsonReport()

    #grid_search_returns(ticker='AAPL', start_date='2019-01-01', end_date='2025-04-14')
    grid_search_returns_with_band(ticker='AAPL', start_date='2019-01-01', end_date='2025-04-14')

