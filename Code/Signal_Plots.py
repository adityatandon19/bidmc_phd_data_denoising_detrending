import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

# data = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/BIDMC dataset/bidmc-ppg-and-respiration-dataset-1.0.0/bidmc_csv/bidmc_01_Signals.csv', index_col=None)
data = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/BIDMC dataset/bidmc-ppg-and-respiration-dataset-1.0.0/bidmc_csv/bidmc_01_Signals.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
data.index
data1 = data.iloc[0:59996, :]
lms_fil = pd.read_csv ('/home/soft23/soft23/soft23/python/Dataset-PPG/LMS_Filtered(01-11-22).csv', index_col=data.index)
lms_fil.index=data1.index
detrended_df = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Detrend_Signal(01-11-22).csv', index_col = 0)
detrended_df.index=lms_fil.index
wave_tf = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Wavelet_TF_Signal(01-11-22).csv', index_col = 0)
wave_tf.index=lms_fil.index

data.plot()
plt.xlim(0,5)
plt.title('Raw_Signals vs Time')
pyplot.show()

# plot the dataframe
# data.plot(x=data['Time [s]'], y=[" RESP", " PLETH", " V", " AVR", ' II'], kind="line", figsize=(9, 8))
 
data[' RESP'].plot()
plt.xlim(0, 60000)
pyplot.show()

data[' PLETH'].plot()
plt.xlim(0, 10)
pyplot.show()

data[' V'].plot()
plt.xlim(0, 5000)
plt.title('Raw_V_Sisnal', 2)
pyplot.show()

data[' AVR'].plot()
plt.xlim(0, 10)
pyplot.show()

data[' II'].plot()
plt.xlim(0, 10)
pyplot.show()

lms_fil.plot()
plt.xlim(0,5)
plt.title('LMS_Filtered_Signal')
pyplot.show()


detrended_df.plot()
plt.xlim(0,5)
plt.title('Detrended_Signal')
pyplot.show()


wave_tf.plot()
plt.xlim(0,100)
plt.title('Wavelet_Transform_Signal')
pyplot.show()


plt.subplot(5, 2, 1)
data[' RESP'].plot()
plt.xlim(0,5)
plt.legend('RESP', prop={'size':5})

plt.subplot(5, 2, 2)
data[' PLETH'].plot()
plt.xlim(0,5)
plt.legend('PLETH', prop={'size':5})

plt.subplot(5, 2, 3)
data[' V'].plot()
plt.xlim(0,5)
plt.legend('V', prop={'size':5})

plt.subplot(5, 2, 4)
data[' AVR'].plot()
plt.xlim(0,5)
plt.legend('AVR', prop={'size':5})

plt.subplot(5, 2, 5)
data[' II'].plot()
plt.xlim(0,5)
plt.legend('II', prop={'size':5})

plt.suptitle("Raw_Signal")





plt.subplot(5, 2, 1)
lms_fil['RESP'].plot()
plt.xlim(0,5)
plt.legend('RESP', prop={'size':5})

plt.subplot(5, 2, 2)
lms_fil['PLETH'].plot()
plt.xlim(0,5)
plt.legend('PLETH', prop={'size':5})

plt.subplot(5, 2, 3)
lms_fil['V'].plot()
plt.xlim(0,5)
plt.legend('V', prop={'size':5})

plt.subplot(5, 2, 4)
lms_fil['AVR'].plot()
plt.xlim(0,5)
plt.legend('AVR', prop={'size':5})

plt.subplot(5, 2, 5)
lms_fil['II'].plot()
plt.xlim(0,5)
plt.legend('II', prop={'size':5})

plt.suptitle("LMS_Filtered_Signal")




plt.subplot(5, 2, 1)
detrended_df['RESP'].plot()
plt.xlim(0,5)
plt.legend('RESP', prop={'size':5})

plt.subplot(5, 2, 2)
detrended_df['PLETH'].plot()
plt.xlim(0,5)
plt.legend('PLETH', prop={'size':5})

plt.subplot(5, 2, 3)
detrended_df['V'].plot()
plt.xlim(0,5)
plt.legend('V', prop={'size':5})

plt.subplot(5, 2, 4)
detrended_df['AVR'].plot()
plt.xlim(0,5)
plt.legend('AVR', prop={'size':5})

plt.subplot(5, 2, 5)
detrended_df['II'].plot()
plt.xlim(0,5)
plt.legend('II', prop={'size':5})

plt.suptitle("Detrended_Signal")


# fig, axes = plt.subplots(3, 2, sharex=True, figsize=(16,8))
plt.subplot(5, 2, 1)
wave_tf['RESP'].plot()
plt.xlim(0,100)
plt.legend('RESP', prop={'size':5})
# fig, axes = plt.subplots(2, 1, sharex=True, figsize=(16,8))
plt.subplot(5, 2, 2)
wave_tf['PLETH'].plot()
plt.xlim(0,100)
plt.legend('PLETH', prop={'size':5})

plt.subplot(5, 2, 3)
wave_tf['V'].plot()
plt.xlim(0,100)
plt.legend('V', prop={'size':5})

plt.subplot(5, 2, 4)
wave_tf['AVR'].plot()
plt.xlim(0,100)
plt.legend('AVR', prop={'size':5})

plt.subplot(5, 2, 5)
wave_tf['II'].plot()
plt.xlim(0,100)
plt.legend('II', prop={'size':5})

plt.suptitle("Wavelet_Transformed_Signal")