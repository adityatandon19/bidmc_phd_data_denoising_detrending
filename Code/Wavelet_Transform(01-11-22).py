# Denoising PPG Signal:
    
import pywt
from skimage.restoration import denoise_wavelet
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

detrended_df = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Detrend_Signal(01-11-22).csv', index_col = 0)

# Level = 1:
    
# RESP Signal:
x1 = detrended_df['RESP'].values.flatten()
x1_denoise = denoise_wavelet(x1, method='VisuShrink', mode='soft', wavelet_levels=10, wavelet='sym8', rescale_sigma='True')
plt.figure(figsize=(20, 10), dpi=100)
plt.xlim([0, 60000]);
plt.plot(x1_denoise)
plt.grid
plt.show()

# PLETH Signal:
# x2 = detrended_df.loc[:, ['PLETH']].values.flatten()
x2 = detrended_df['PLETH'].values.flatten()
x2_denoise = denoise_wavelet(x2, method='VisuShrink', mode='soft', wavelet_levels=10, wavelet='sym8', rescale_sigma='True')
plt.figure(figsize=(20, 10), dpi=100)
# plt.xlim([0, 1000]);
plt.plot(x2_denoise)
plt.show()

# V Signal:
# x3 = detrended_df.loc[:, ['V']].values.flatten()
x3 = detrended_df['V'].values.flatten()
x3_denoise = denoise_wavelet(x3, method='VisuShrink', mode='soft', wavelet_levels=10, wavelet='sym8', rescale_sigma='True')
plt.figure(figsize=(20, 10), dpi=100)
# plt.xlim([0, 1000]);
plt.plot(x3_denoise)
plt.show()  

# AVR Signal:
# x4 = detrended_df.loc[:, ['AVR']].values.flatten()
x4 = detrended_df['AVR'].values.flatten()
x4_denoise = denoise_wavelet(x4, method='VisuShrink', mode='soft', wavelet_levels=10, wavelet='sym8', rescale_sigma='True')
plt.figure(figsize=(20, 10), dpi=100)
# plt.xlim([0, 1000]);
plt.plot(x4_denoise)
plt.show()

# II Signal:
# x5 = detrended_df.loc[:, ['II']].values.flatten()
x5 = detrended_df['II'].values.flatten()
x5_denoise = denoise_wavelet(x5, method='VisuShrink', mode='soft', wavelet_levels=10, wavelet='sym8', rescale_sigma='True')
plt.figure(figsize=(20, 10), dpi=100)
# plt.xlim([0, 1000]);
plt.plot(x5_denoise)
plt.show()

wavelet_tf = pd.DataFrame([x1_denoise, x2_denoise, x3_denoise, x4_denoise, x5_denoise])
wavelet_tf = wavelet_tf.T
wavelet_tf.rename(columns = {0:'RESP', 1:'PLETH', 2:'V', 3:'AVR', 4:'II'}, inplace=True)

# os.chdir('/home/soft23/soft23/soft23/python/Dataset-PPG')
# wavelet_tf.to_csv('Wavelet_TF_Signal(01-11-22).csv')



# Crest Factor:
def crest_factor(x):
    return np.max(np.abs(x))/np.sqrt(np.mean(np.square(x)))

cf = crest_factor(wavelet_tf)




