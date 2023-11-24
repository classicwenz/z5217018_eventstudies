""" download.py

Utilities to download data from Yahoo Finance
"""
import yfinance as yf

from event_study import config as cfg

# --------------------------------------------------------
#   Function to download recommendations
# --------------------------------------------------------
def yf_rec_to_csv(tic, pth,
                  start=None,
                  end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    c = yf.Ticker(tic)
    c.history(start=start, end=end).tz_localize(None)
    # Make sure we only relevant dates
    if start is not None and end is not None:
        df = c.recommendations.loc[start:end]
    elif start is not None:
        df = c.recommendations.loc[start:]
    elif end is not None:
        df = c.recommendations.loc[:end]
    else:
        df = c.recommendations
    df.to_csv(pth)

