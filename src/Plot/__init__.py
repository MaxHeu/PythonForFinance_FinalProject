import pandas as pd
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, df: pd.DataFrame, result:dict):
        self.df = df
        self.result = result

    def scatter(self):
        plt.plot(self.df['Close'])
        plt.scatter(self.df.loc[self.result['buydates']].index, self.df.loc[self.result['buydates']].Close, marker = '^', c = 'g')
        plt.scatter(self.df.loc[self.result['selldates']].index, self.df.loc[self.result['selldates']].Close, marker='v', c='r')
        plt.savefig('Strategy.png')
        plt.close()

    def plot_closing(self):
        '''
        Plot the closing prices of the stock with bollinger bands
        '''
        plt.plot(self.df['Close'])
        plt.plot(self.df['upper_bb'], label='Upper Bollinger Band', color='b')
        plt.plot(self.df['lower_bb'], label='Lower Bollinger Band', color='g')
        plt.savefig('Closing_bb.png')
        plt.close()
    
    def plot_rsi(self):
        '''
        Plot the RSI of the stock with lower and upper bands
        '''
        plt.plot(self.df['rsi'], label='RSI', color='b')
        plt.axhline(y=30, color='g', linestyle='--')
        plt.axhline(y=70, color='r', linestyle='--')
        plt.savefig('RSI_withBands.png')
        plt.close()

    
    