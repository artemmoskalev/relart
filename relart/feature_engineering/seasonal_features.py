import numpy as np
import pandas as pd

# This function create fourier feature pairs
# @n_row - number of time stamps
# @n_fourier_pairs - number of fourier pair components
# @period - fourier seasonality
# @Value - returns a DataFrame with n_row rows and n_fourier_pairs x 2 columns,
#          where each column contains fourier features for specific scale of sin/cos feature
def create_fourier_features(n_row, n_fourier_pairs, period):
    col_dict = {}
    for fourier_inx in range(1, n_fourier_pairs + 1):
        fsin_new = __create_fourier_feature(n_row, np.sin, fourier_inx, period)
        fcos_new = __create_fourier_feature(n_row, np.cos, fourier_inx, period)
        
        col_dict[f"sin_{period}_{fourier_inx}"] = fsin_new
        col_dict[f"cos_{period}_{fourier_inx}"] = fcos_new
    
    return pd.DataFrame.from_dict(col_dict)

def __create_fourier_feature(n, trig_func, fourier_pair_inx, period):
    fourier_value_arr = [trig_func(2 * np.pi * fourier_pair_inx * i / period) for i in range(n)]
    return np.array(fourier_value_arr)