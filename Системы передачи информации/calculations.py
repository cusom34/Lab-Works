import numpy as np
from math import erfc
from math import erf
import matplotlib.pyplot as plt

def Q(x):
    return 0.5*erfc(x/np.sqrt(2))


# L = 256
# print(2*(1-1/l)/8*q(np.sqrt(3*8/(l**2-1)*2)))
# print(0.5*np.exp(-1))

# Шкала eb/n0 в дб
SNR_dB = [i for i in range(-8,4)]

# Измеренные BER для BPSK и 16-PSK(с кодировкой Грея)
BPSK_ber = [2.89e-1, 2.63e-1, 2.38e-1, 2.13e-1, 1.87e-1, 1.60e-1, 1.32e-1, 1.04e-1, 7.85e-2, 5.65e-2, 3.70e-2, 2.10e-2]
PSK16_ber = [3.43e-1, 3.23e-1, 3.07e-1, 2.86e-1, 2.63e-1, 2.42e-1, 2.20e-1, 1.95e-1, 1.75e-1, 1.53e-1, 1.33e-1, 1.14e-1]

# Мощность шума для BPSK и 16-PSK
n = [25/2/10**(snr/10) for snr in SNR_dB]

# График
plt.plot(SNR_dB, BPSK_ber, marker='.', label='BPSK', )
plt.plot(SNR_dB, PSK16_ber, marker='.', label='16-PSK(Gray coding)')
plt.xticks(SNR_dB)
plt.grid(which='major')
plt.minorticks_on()
plt.grid(which='minor', alpha=0.3)
plt.yscale('log')
plt.xlabel('Eb/N0, дБ')
plt.ylabel('BER')
plt.legend(loc="best")
plt.show()
