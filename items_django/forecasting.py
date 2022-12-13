from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import pandas as pd
from pandas import read_csv
from pandas import datetime
from sklearn.metrics import mean_squared_error
import numpy.random as rn
import statsmodels.api as sm
from itertools import product
import warnings
warnings.filterwarnings('ignore')
from scipy import stats
import matplotlib.pyplot as plt

def run_2(name):


  def data_preparation(_data):
   return pd.read_csv(_data)
#   data.head()
  data = data_preparation(name)
#   data.tail()
  
  data['date'] = pd.to_datetime(data['date'],format="%d.%m.%Y")
  data = data.set_index(data['date'])
  
  
  
#   print("Критерий Дики-Фуллера: p=%f" % sm.tsa.stattools.adfuller(data.data)[1])
  
  def invboxcox(y,lmbda):
     if lmbda == 0:
        return(np.exp(y))
     else:
        return(np.exp(np.log(lmbda*y+1)/lmbda))
  
  np.log(data['data'])
  
  data['data'], lmbda = np.log(data['data']), 0
  
  
#   data
  
#   ad_fuller_result = adfuller(data['data'])
#   print(f'ADF Statistic: {ad_fuller_result[0]}')
#   print(f'p-value: {ad_fuller_result[1]}')
  
  
  
  
  
#   data['date'].max()
  
  forecast_date = pd.date_range(start=data['date'].max(), end=pd.to_datetime(100, unit='D', origin=data['date'].max()))
  forecast_date
  
  
  
  pd.to_datetime(100, unit='D', origin=data['date'].max())
  
  ad_fuller_result = adfuller(data['data'])
  print(f'ADF Statistic: {ad_fuller_result[0]}')
  print(f'p-value: {ad_fuller_result[1]}')
  
  data = data.reset_index(drop=True)
def making_prediction_SARIMA(x_data):
 return SARIMAX(data['data'], order=(0, 1, 2), seasonal_order=(0, 1, 2, 4)).fit(dis=-1)
def making_prediction_ARMA(x_data) :
 return  ARIMA(x_data, order=(2, 0, 1)).fit()

 best_model =  making_prediction_SARIMA(data['data'])
 ARMA_model = making_prediction_ARMA(data['data'])
#   print(best_model.summary())
  
  ARMA_model = ARIMA(data['data'], order=(2, 0, 1)).fit()
  
  yhat = ARMA_model.predict(start=data.shape[0], end=data.shape[0] + 100)
#   print(yhat)
  
  
  
  data['sarima_model'] = best_model.fittedvalues
  data['sarima_model'][:4+1] = np.NaN
  
  
  
  forecast = best_model.predict(start=data.shape[0], end=data.shape[0] + 100)
  forecast = data['sarima_model'].append(forecast)

  future_forecast_SARIMA = forecast[ data.shape[0]-1:].reset_index(drop=True)
  
  future_forecast_SARIMA = invboxcox(future_forecast_SARIMA,0)
  
  future_forecast_SARIMA
  
  plt.figure(figsize=(17, 10.5))
 
  plt.plot(forecast, color='r', label='model')
  plt.axvspan(data.index[-1], forecast.index[-1], alpha=0.5, color='lightgrey')
  plt.plot(data['data'], label='actual')
  plt.legend()
  
#   x = np.array(range(len(forecast)))
  x = np.array(range(round(len(forecast)/5)+1))
  plt.xticks(x, [x.strftime("%d-%m-%Y") for x in pd.concat([data['date'], pd.Series(forecast_date)])][::5] ,rotation=90)
#  [x.strftime("%d-%m-%Y") for x in pd.concat([data['date'], pd.Series(forecast_date)])][::5]
  plt.locator_params(axis='x', nbins=len(forecast)/5)
  plt.savefig('../hotels_vue/src/assets/foo.png')



  data['arma_model'] = ARMA_model.fittedvalues
  data['arma_model'][:4+1] = np.NaN
  
  forecast = ARMA_model.predict(start=data.shape[0], end=data.shape[0] + 100)
  forecast = data['arma_model'].append(forecast)
  


  
  
  future_forecast_ARMA = forecast[ data.shape[0]-1:].reset_index(drop=True)
  
  future_forecast_ARMA = invboxcox(future_forecast_ARMA,0)
  
#   future_forecast_ARMA
  
  
  
  testdata = data
  
  testdata = testdata.drop(index=testdata.index[:5], 
          axis=0).reset_index(drop=True)
  
  testdata['data']
  
  testdata['sarima_model']
  

 def calculate_error(predicted, real):
   return  mean_squared_error(invboxcox(real,0),invboxcox(predicted,0)), np.sqrt(mean_squared_error(invboxcox(predicted,0),invboxcox(predicted,0)))
  
  ARMA_mse = calculate_error(testdata['sarima_model'], testdata['data']) 
  SARIMA_mse = calculate_error(testdata['arma_model'], testdata['data']) 
  
  if  SARIMA_mse > ARMA_mse:
    final_mse = ARMA_mse
    final_rmse = np.sqrt(ARMA_mse)
    future_prediction_function =future_forecast_ARMA
  else:
    final_mse = SARIMA_mse
    final_rmse = np.sqrt(SARIMA_mse)
    future_prediction_function =future_forecast_SARIMA
  
  
  
  def annealing_simulation(random_start_state,
predicted_function, random_next, chance_of_acceptance, change_temperature, maxsteps=1000)
:
      """ Optimize the black-box function 'cost_function' with the simulated annealing algorithm."""
      state = random_start()
      cost = cost_function(state)
      states, costs = [state], [cost]
      for step in range(maxsteps):
          fraction = step / float(maxsteps)
          T = temperature(fraction)
          new_state = random_neighbour(state, fraction)
          new_cost = cost_function(new_state)
          if debug: print("Step #{:>2}/{:>2} : T = {:>4.3g}, state = {:>4.3g}, cost = {:>4.3g}, new_state = {:>4.3g}, new_cost = {:>4.3g} ...".format(step, maxsteps, T, state, cost, new_state, new_cost))
          if acceptance_probability(cost, new_cost, T) > rn.random():
              state, cost = new_state, new_cost
              states.append(state)
              costs.append(cost)
              # print("  ==> Accept it!")
          # else:
          #    print("  ==> Reject it...")
      return state, cost_function(state), states, costs
  
  interval = (0, len(future_prediction_function)-2)
  # len(testdata.index)
  def f(x):
      return future_prediction_function[round(x)]
  
  def clip(x):
      a, b = interval
      return max(min(x, b), a)
  
  def random_start_state():
      a, b = interval
      return a + (b - a) * rn.random_sample()
  
  def predicted_function(x):
      return f(x)
  
  def random_next(x, fraction=1):
      amplitude = (max(interval) - min(interval)) * fraction / 10
      delta = (-amplitude/2.) + amplitude * rn.random_sample()
      return clip(x + delta)
  
  def chance_of_acceptance(cost, new_cost, temperature):
      if new_cost < cost:
          # print("    - Acceptance probabilty = 1 as new_cost = {} < cost = {}...".format(new_cost, cost))
          return 1
      else:
          p = np.exp(- (new_cost - cost) / temperature)
          # print("    - Acceptance probabilty = {:.3g}...".format(p))
          return p
  
  def change_temperature(fraction):
      """ Example of temperature dicreasing as the process goes on."""
      return max(0.01, min(1, 1 - fraction))
  
  state, c, states, costs = annealing(random_start, cost_function, random_neighbour, acceptance_probability, temperature, maxsteps=1000, debug=False);
  
  
  print(c)
  print(forecast_date[round(state)].strftime("%d-%m-%Y"))
  
  return  round(final_mse, 3),round(final_rmse,3), round(c), forecast_date[round(state)].strftime("%d-%m-%Y")
