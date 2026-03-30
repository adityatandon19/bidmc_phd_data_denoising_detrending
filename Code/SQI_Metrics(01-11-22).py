from vital_sqi.sqi.standard_sqi import perfusion_sqi, kurtosis_sqi, skewness_sqi, entropy_sqi, signal_to_noise_sqi
import pandas as pd
wave_tf = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Wavelet_TF_Signal(01-11-22).csv', index_col = 0)
data = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/BIDMC dataset/bidmc-ppg-and-respiration-dataset-1.0.0/bidmc_csv/bidmc_01_Signals.csv', index_col=None)


# RESP Signal:

kurt_resp = kurtosis_sqi(wave_tf['RESP'], axis=0, fisher=True, bias=True,
                 nan_policy='propagate')

skew_resp = skewness_sqi(wave_tf['RESP'], axis=0, bias=True, nan_policy='propagate')

entropy_resp = entropy_sqi(wave_tf['RESP'], qk=None, base=None, axis=0)

snr_resp = signal_to_noise_sqi(wave_tf['RESP'], axis=0, ddof=0)


# PLETH Signal:

kurt_pleth = kurtosis_sqi(wave_tf['PLETH'], axis=0, fisher=True, bias=True,
                 nan_policy='propagate')

skew_pleth = skewness_sqi(wave_tf['PLETH'], axis=0, bias=True, nan_policy='propagate')

entropy_pleth = entropy_sqi(wave_tf['PLETH'], qk=None, base=None, axis=0)

snr_pleth = signal_to_noise_sqi(wave_tf['PLETH'], axis=0, ddof=0)


# V Signal:

kurt_v = kurtosis_sqi(wave_tf['V'], axis=0, fisher=True, bias=True,
                 nan_policy='propagate')

skew_v = skewness_sqi(wave_tf['V'], axis=0, bias=True, nan_policy='propagate')

entropy_v = entropy_sqi(wave_tf['V'], qk=None, base=None, axis=0)

snr_v = signal_to_noise_sqi(wave_tf['V'], axis=0, ddof=0)


# AVR Signal:

kurt_avr = kurtosis_sqi(wave_tf['AVR'], axis=0, fisher=True, bias=True,
                 nan_policy='propagate')

skew_avr = skewness_sqi(wave_tf['AVR'], axis=0, bias=True, nan_policy='propagate')

entropy_avr = entropy_sqi(wave_tf['AVR'], qk=None, base=None, axis=0)

snr_avr = signal_to_noise_sqi(wave_tf['AVR'], axis=0, ddof=0)


# II Signal:

kurt_ii = kurtosis_sqi(wave_tf['II'], axis=0, fisher=True, bias=True,
                 nan_policy='propagate')

skew_ii = skewness_sqi(wave_tf['II'], axis=0, bias=True, nan_policy='propagate')

entropy_ii = entropy_sqi(wave_tf['II'], qk=None, base=None, axis=0)

snr_ii = signal_to_noise_sqi(wave_tf['II'], axis=0, ddof=0)


kurtosis = [0.5274703837906976, -0.0021504083807952767, 0.40412206362348124, 0.3124993269000962, 0.06010215080208425]
skew = [0.1281429154565273,  -0.49757044294750497, -0.5547604845180927, -0.571936245631584, -0.5059075695390007]
entropy = [10.97837247261234, 10.952624907723221, 10.959459619780933, 10.960537669018137, 10.95152158007521]
snr = [-0.00731698, -0.01095962, -0.00088948, -0.0071625, -0.00082194]



