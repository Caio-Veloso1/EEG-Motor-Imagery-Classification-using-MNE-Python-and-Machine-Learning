import mne 
from mne.datasets import eegbci

def preprocess(subject, runs):
    file = eegbci.load_data(subject, runs)
    raw = mne.io.read_raw_edf(file[0], preload=True) #poupando memoria
    raw.plot
    raw.filter(7,30)

    return raw