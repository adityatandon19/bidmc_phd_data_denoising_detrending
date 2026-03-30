import pandas as pd
import matplotlib.pyplot as plt
wave_tf = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Wavelet_TF_Signal(01-11-22).csv', index_col = 0)

# for i in wave_tf.columns:
#     prin
    
wave_tf['RESP'].max()   # 0.3112027748631237
wave_tf['PLETH'].max()  # 0.0643487298809005
wave_tf['V'].max()  # 0.0760797587055057
wave_tf['AVR'].max()  # 0.067699242404729
wave_tf['II'].max() # 0.0702111132971398

# PLI Removal:

# RESP Signal:
alpha_resp = 4.659949/4.647780  # (CFi/CF1, CFi = Crest Factor at level 10, CF1 = Crest Factor at level 1)
# 1.0026182392454033

delta_resp = 1.0026182392454033 * 0.3112027748631237
# 0.31201757818154874

# PLETH Signal:
alpha_pleth = 3.389277/4.402593
0.7698365485976104

delta_pleth = 0.7698365485976104 * 0.0643487298809005
# 0.04953800411815236

# V Signal:
alpha_v = 3.643198/5.104240
# 0.7137591492563046

delta_v = 0.7137591492563046 * 0.0760797587055057
# 0.054302623849266686

# AVR Signal:
alpha_avr = 3.694459/4.977636
# 0.7422115638829355

delta_avr = 0.7422115638829355 * 0.067699242404729
# 0.05024716057890385

# II Signal:
alpha_ii = 3.347672/4.491948
# 0.7452606307998223

delta_ii = 0.7452606307998223 * 0.0702111132971398    
# 0.052325578584984204


pli_resp_1 = []
pli_resp_2 = []
for i in range(len(wave_tf['RESP'])):
    if delta_resp <= wave_tf['RESP'][i]:
        # i+=1
        pli_resp_1.append(wave_tf['RESP'][i])
    else:
        pli_resp_2.append(wave_tf['RESP'][i])

    
pli_pleth_1 = []    
pli_pleth_2 = []    
for i in range(len(wave_tf['PLETH'])):
    if delta_pleth <= wave_tf['PLETH'][i]:
        # i+=1
        pli_pleth_1.append(wave_tf['PLETH'][i])
    else:
        pli_pleth_2.append(wave_tf['PLETH'][i])
        
    
pli_v_1 = []    
pli_v_2 = []    
for i in range(len(wave_tf['V'])):
    if delta_v <= wave_tf['V'][i]:
        # i+=1
        pli_v_1.append(wave_tf['V'][i])
    else:
        pli_v_2.append(wave_tf['V'][i])
  
    
pli_avr_1 = []
pli_avr_2 = []   
for i in range(len(wave_tf['AVR'])):
    if delta_avr <= wave_tf['AVR'][i]:
        # i+=1
        pli_avr_1.append(wave_tf['AVR'][i])
    else:
        pli_avr_2.append(wave_tf['AVR'][i])
 
    
pli_ii_1 = []
pli_ii_2 = []
for i in range(len(wave_tf['II'])):
    if delta_ii <= wave_tf['II'][i]:
        # i+=1
        pli_ii_1.append(wave_tf['II'][i])
    else:
        pli_ii_2.append(wave_tf['II'][i])
       
        
pli_1 = pd.DataFrame([pli_resp_1, pli_pleth_1, pli_v_1, pli_avr_1, pli_ii_1])
pli_1 = pli_1.T
pli_1.rename(columns = {0:'RESP', 1:'PLETH', 2:'V', 3:'AVR', 4:'II'}, inplace=True)

pli_2 = pd.DataFrame([pli_resp_2, pli_pleth_2, pli_v_2, pli_avr_2, pli_ii_2])
pli_2 = pli_2.T
pli_2.rename(columns = {0:'RESP', 1:'PLETH', 2:'V', 3:'AVR', 4:'II'}, inplace=True)




# PLI Removed Visualization:
# plt.xlim(0, 30000)
# plt.plot(pli_ii_2)

plt.subplot(5, 2, 1)
plt.plot(pli_resp_1)
plt.xlim(0,1500)
plt.legend('RESP', prop={'size':5})

plt.subplot(5, 2, 2)
plt.plot(pli_pleth_1)
plt.xlim(0,1500)
plt.legend('PLETH', prop={'size':5})

plt.subplot(5, 2, 3)
plt.plot(pli_v_1)
plt.xlim(0,1500)
plt.legend('V', prop={'size':5})

plt.subplot(5, 2, 4)
plt.plot(pli_avr_1)
plt.xlim(0,1500)
plt.legend('AVR', prop={'size':5})

plt.subplot(5, 2, 5)
plt.plot(pli_ii_1)
plt.xlim(0,1500)
plt.legend('II', prop={'size':5})

plt.suptitle("PLI_Removed_Signal")

