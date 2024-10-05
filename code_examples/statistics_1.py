import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol,base_dir="data"):
	return os.path.join(base_dir,"{}.csv".format(str(symbol)))

def get_data(symbols,dates):
	df = pd.DataFrame(index=dates)
	print df

	if 'SPY' not in symbols:
		symbols.insert(0,'SPY')

	for symbol in symbols:
		tmp = pd.read_csv(symbol_to_path(symbol),index_col="Date",parse_dates=True,usecols=['Date','Close'],na_values=['nan'])
		tmp = tmp.rename(columns={'Close':symbol})

		df = df.join(tmp)
		if symbol == 'SPY':
			df = df.dropna(subset=['SPY'])

	return df

def get_bollinger_bands(rm,rstd):
	return rm + 2*rstd, rm - 2*rstd

def test_run():
	dates = pd.date_range('2010-01-01','2012-12-31')

	symbols = ['SPY']

	df = get_data(symbols,dates)
	
	ax = df['SPY'].plot(title="SPY Bollinger bands", label = "SPY")

	rm_SPY = pd.rolling_mean(df['SPY'], window=20)

	rstd_SPY = pd.rolling_std(df['SPY'],window=20)

	upper_band,lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

	rm_SPY.plot(label='Rolling mean', ax=ax)
	upper_band.plot(label='upper band', ax=ax)
	lower_band.plot(label='lower band', ax=ax)

	ax.set_xlabel("Date")
	ax.set_ylabel("Closing Price")
	ax.legend(loc='upper left')

	plt.show()

if __name__ == "__main__":
	test_run()