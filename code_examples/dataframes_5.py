import pandas as pd

def test_run():
	start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    df1 = pd.DataFrame(index=dates)	# build empty dataframe
    
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
    
    df1 = df1.join(dfSPY)
    
    print df1
    
// This is fo example 7
	df1 = df1.join(dfSPY,how='inner')
    
// fo example 8
	dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    df1 = df1.join(dfSPY,how='inner')
    
    symbols = ['GOOG','IBM','GLD']
    for symbol in symbols:
    	df_tmp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        
        # rename to prevent name clash (multiple columns with same name)
        df_tmp = df_tmp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df_tmp, how='inner')

// fo example 9
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df,columns,start_ind,end_ind):
	print df.ix[start_ind:end_ind,columns]
	plot_data(df.ix[start_ind:end_ind,columns])

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

def plot_data(df, title="Stock prices"):
	ax = df.plot(title=title,fontsize=12)
	ax.set_xlabel("Date")
	ax.set_ylabel("Closing price")

	plt.show()

def test_run():
	dates = pd.date_range('2010-01-01','2010-12-31')

	symbols = ['IBM','GLD']

	df = get_data(symbols,dates)

	print df
	plot_selected(df,['SPY','IBM'],'2010-03-01','2010-04-01')

if __name__ == "__main__":
	test_run()
    
 // for example 10
 
 def normalize_data(df):
 	df = df/df.ix[0,:]
    return df