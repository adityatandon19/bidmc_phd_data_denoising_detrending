import pandas as pd
wave_tf = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Wavelet_TF_Signal(01-11-22).csv', index_col = 0)


from numpy import sqrt, mean, absolute, real, conj


def rms_flat(a):
    return sqrt(mean(absolute(a)**2))


def rms_fft(spectrum):
    return rms_flat(spectrum)/sqrt(len(spectrum))


def rms_rfft(spectrum, n=None):
    if n is None:
        n = (len(spectrum) - 1) * 2
    sq = real(spectrum * conj(spectrum))
    if n % 2:  # odd-length
        mean = (sq[0] + 2*sum(sq[1:])           )/n
    else:  # even-length
        mean = (sq[0] + 2*sum(sq[1:-1]) + sq[-1])/n
    root = sqrt(mean)
    return root/sqrt(n)


if __name__ == "__main__":
    from numpy.random import randn
    from numpy.fft import fft, ifft, rfft, irfft

    n = 10
    x = wave_tf.copy()
    X = fft(x)
    rX = rfft(x)

    print(rms_flat(x))
    print(rms_flat(ifft(X)))
    print(rms_fft(X))
    print()

    # Accurate for odd n:
    print(rms_flat(irfft(rX, n)))
    print(rms_rfft(rX, n))
    print()

    # Only approximate for odd n:
    print(rms_flat(irfft(rX)))
    print(rms_rfft(rX))
    


pt_resp_1 = []
pt_resp_2 = []
for i in range(len(wave_tf['RESP'])):
    if rms_flat(x['RESP']) <= wave_tf['RESP'][i]:
        i+=1
        pt_resp_1.append(wave_tf['RESP'][i])
    else:
        pt_resp_2.append(wave_tf['RESP'][i])

  
pt_pleth_1 = []     
pt_pleth_2 = []     
for i in range(len(wave_tf['PLETH'])):
    if rms_flat(x['PLETH']) <= wave_tf['PLETH'][i]:
        i+=1
        pt_pleth_1.append(wave_tf['PLETH'][i])
    else:
        pt_pleth_2.append(wave_tf['PLETH'][i])

        
pt_v_1 = []        
pt_v_2 = []        
for i in range(len(wave_tf['V'])):
    if rms_flat(x['V']) <= wave_tf['V'][i]:
        i+=1
        pt_v_1.append(wave_tf['V'][i])
    else:
        pt_v_2.append(wave_tf['V'][i])

    
pt_avr_1 = []
pt_avr_2 = []
for i in range(len(wave_tf['AVR'])):
    if rms_flat(x['AVR']) <= wave_tf['AVR'][i]:
        i+=1
        pt_avr_1.append(wave_tf['AVR'][i])
    else:
        pt_avr_2.append(wave_tf['AVR'][i])

    
pt_ii_1 = []
pt_ii_2 =[]     
for i in range(len(wave_tf['II'])):
    if rms_flat(x['II']) <= wave_tf['II'][i]:
        i+=1
        pt_ii_1.append(wave_tf['II'][i])
    else:
        pt_ii_2.append(wave_tf['II'][i])

    
    
