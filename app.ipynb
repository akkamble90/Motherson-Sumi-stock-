{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "194f24c0-527a-476a-b3a1-8c3f96de18a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import mplfinance as mpf\n",
    "import pandas_ta as ta\n",
    "import streamlit as st\n",
    "from io import BytesIO\n",
    "\n",
    "# Title\n",
    "st.title(\"Motherson Sumi Live Chart (CSV Interaction)\")\n",
    "\n",
    "# File uploader\n",
    "uploaded_file = st.file_uploader(\"Upload CSV\", type=\"csv\")\n",
    "\n",
    "if uploaded_file:\n",
    "    # Load CSV\n",
    "    df = pd.read_csv(uploaded_file)\n",
    "    df['Date'] = pd.to_datetime(df['Date'])\n",
    "    df.set_index('Date', inplace=True)\n",
    "\n",
    "    # Calculate indicators\n",
    "    df['EMA_20'] = ta.ema(df['Close'], length=20)\n",
    "    df['RSI'] = ta.rsi(df['Close'], length=14)\n",
    "\n",
    "    # Plot chart\n",
    "    ema_plot = mpf.make_addplot(df['EMA_20'], color='blue')\n",
    "    rsi_plot = mpf.make_addplot(df['RSI'], panel=1, color='purple', ylabel='RSI')\n",
    "\n",
    "    buf = BytesIO()\n",
    "    mpf.plot(df, type='candle', style='yahoo', addplot=[ema_plot, rsi_plot], volume=True, figsize=(12,8), savefig=buf)\n",
    "    st.image(buf)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
