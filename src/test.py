import neurokit2 as nk
import matplotlib.pyplot as plt

eog_signal = nk.data('eog_100hz.csv')
eog_cleaned = nk.eog_clean(eog_signal, sampling_rate=100, method='neurokit')

nk.signal_plot(eog_cleaned)
nk.signal_plot(eog_signal)
plt.show()