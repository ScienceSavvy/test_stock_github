import pandas as pd
from Company import Company
from Stock import Stock
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use("fivethirtyeight")

totalWorthStart = 0;
totalWorthNow = 0;
buying_power = 0;
current_day = 0;

#GUI global variables
graph_time_label_text = "Ex: Week 1 - 12/20/17"
company_display_label_text = "Ex: APPL"

# May want to use adjusted close price instead of regular close price

df_goog = pd.read_excel(
    "C:\Justin\PYTHON\Stock Project\Historical Data Excel\GOOG_Data.xlsx"
)
df_amzn = pd.read_excel(
    "C:\Justin\PYTHON\Stock Project\Historical Data Excel\AMZN_Data.xlsx"
)
df_ford = pd.read_excel(
    "C:\Justin\PYTHON\Stock Project\Historical Data Excel\FORD_Data.xlsx"
)


goog_company = Company(
    "GOOG",
    pd.to_datetime(df_goog["Date"]).dt.date.tolist(),
    df_goog["Adj Close"].tolist(),
    df_goog["Volume"].tolist(),
)

amzn_company = Company(
    "AMZN",
    pd.to_datetime(df_amzn["Date"]).dt.date.tolist(),
    df_amzn["Adj Close"].tolist(),
    df_amzn["Volume"].tolist(),
)

ford_company = Company(
    "FORD",
    pd.to_datetime(df_ford["Date"]).dt.date.tolist(),
    df_ford["Adj Close"].tolist(),
    df_ford["Volume"].tolist(),
)


company_list = [goog_company, amzn_company, ford_company]

#GUI initialization

#Creates the window
root = tk.Tk()
root.title("Test Widget for Stock Program")
tab_control = ttk.Notebook(root)

tabMain = ttk.Frame(tab_control)
tabData = ttk.Frame(tab_control)

tab_control.add(tabMain, text='Main Tab')
tab_control.add(tabData, text='Data Tab')

tab_control.pack(expand=1, fill="both")

#Create GUI for Main Tab
    #Create top frame that will contain a grid of individual frames
top_frame = tk.Frame(tabMain, height=100, width=500, bg="red")
top_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    #Create the bottom frame that will contain the matplotlib plot only
bottom_frame = tk.Frame(tabMain, height=100, width=500, bg="blue")
bottom_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    #Create the frame that will contain the controls for SMA
moving_avg_frame = tk.Frame(top_frame, height=100, width=200, bg="cyan")
moving_avg_frame.grid(row=0, column=0)
        #Create SMA small label
sma_small_label = tk.Label(moving_avg_frame, text="Enter SMA small").grid(row=0, column=0)
        #Create SMA small entry
sma_small_entry = tk.Entry(moving_avg_frame).grid(row=0, column=1)
        #Create SMA large label
sma_large_label = tk.Label(moving_avg_frame, text="Enter SMA large").grid(row=1, column=0)
        #Create SMA large entry
sma_large_entry = tk.Entry(moving_avg_frame).grid(row=1, column=1)

    #Create the frame that will contain the run button
run_button_frame = tk.Frame(top_frame, height=100, width=200, bg="green")
run_button_frame.grid(row=0, column=1)
        #Create run button (PLACE RUN COMMAND AFTER fg="Green")
button = tk.Button(run_button_frame, text="RUN", fg="Green").pack()

    #Create the frame that will contain the graph controls for stock price vs gain/loss
graph_type_control_frame = tk.Frame(top_frame, height=100, width=200, bg="yellow")
graph_type_control_frame.grid(row=0, column=2)
        #Create button to display stock price on graph
stock_price_control_button = tk.Button(graph_type_control_frame, text="View Stock Price").grid(row=0)
        #Create button to display Gain/Loss price on graph
gain_loss_control_button = tk.Button(graph_type_control_frame, text="View Gain/Loss").grid(row=1)

    #Create the frame that will contain the time scale graph controls
time_scale_control_frame = tk.Frame(top_frame, height=100, width=200, bg="orange")
time_scale_control_frame.grid(row=1, column=0)
        #Create Week time scale button
week_scale_button = tk.Button(time_scale_control_frame, text="Week").grid(row =0, column=0)
        #Create Month time scale button
month_scale_button = tk.Button(time_scale_control_frame, text="Month").grid(row=0, column=1)
        #Create Year time scale button
year_scale_button = tk.Button(time_scale_control_frame, text="Year").grid(row=0, column=2)

    #Create the frame that will contain the time graph controls
time_control_frame = tk.Frame(top_frame, height=100, width=200, bg="magenta")
time_control_frame.grid(row=1, column=1)
    #Create graph time label (gets text for label from global variable up top)
graph_time_label = tk.Label(time_control_frame, text=graph_time_label_text).grid(row=0, column=1)
    #Create graph time left button
graph_time_left_button = tk.Button(time_control_frame, text="<---").grid(row=0, column=0)
    #Create graph time right button
graph_time_right_button = tk.Button(time_control_frame, text="--->").grid(row=0, column=2)

    #Create the frame that will contain the company graph controls
company_control_frame = tk.Frame(top_frame, height=100, width=200, bg="pink")
company_control_frame.grid(row=1, column=2)
    #Create company display label (gets text for label from global variable up top)
company_display_label = tk.Label(company_control_frame, text=company_display_label_text).grid(row=0, column=1)
    #Create company display left button
company_display_left_button = tk.Button(company_control_frame, text="<---").grid(row=0, column=0)
    #Create graph time right button
company_display_right_button = tk.Button(company_control_frame, text="--->").grid(row=0, column=2)

#Insert matplotlib GUI stuff here



root.mainloop()



def run():
    for i in range(0, company_list[0].date.len):
        global current_day
        current_day = i
        day()






#FIX THIS TO CHECK EACH COMPANY STOCK LIST

def ownStock(ticker):
    for i in range(0, company_list.len):
        if ticker == company_list[i].ticker:
            for j in range(0, company_list[i].stockList.len):
                if company_list[i].stockList[j].saleClosed == False:
                    return True
                else:
                    return False

def sell_stock(ticker):


def buy_stock(ticker):




def day():

    #Do we own stock in a company?
    for i in range(0, company_list.len):

        if ownStock(company_list[i].ticker) == True:
        #Check if owned stock is still viable
            if company_list[i].movingavg(10)[current_day] <= company_list[i].movingavg(50)[current_day]:
            sell_stock(company_list[i].ticker)
            #Otherwise do nothing because the stock is still going up
        else:
            #Check if we should buy a stock
            if company_list[i].movingavg(10)[current_day] > company_list[i].movingavg(50)[current_day]:
                buy_stock(company_list[i].ticker)
        #Otherwise do nothing because the stock is not going up

#Comment2
#Comment2
















