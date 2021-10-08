import math

import matplotlib.pyplot as plt
import mne
import matplotlib
import numpy
import pathlib

import numpy as np

for path in pathlib.Path("Signals").iterdir():
    if path.is_file():
        data = mne.io.read_raw(path)
        data_signal = data.get_data()
        data.plot()
        data.load_data()
        data_fft = np.fft.fft(data_signal[0])
        data_fft_real = data_fft.real
        data_fft_imag = data_fft.imag
        data_fft_real2 = data_fft_real.tolist()
        data_fft_imag2 = data_fft_imag.tolist()
        amp = []
        max_amp = 0
        freq_max = 0
        for i in range(len(data_fft_real2)):
            x = data_fft_imag2[i]
            y = data_fft_real2[i]
            amp.append(math.sqrt(x * x + y * y))
            if amp[i] > max_amp:
                max_amp = amp[i]
                freq_max = math.acos(x / math.sqrt(x * x + y * y))
        print(min(freq_max, 0.1))
        data_filter = data.copy().filter(l_freq=freq_max / (2 * 3.14), h_freq=20)
        data_filter.plot()

plt.show()
