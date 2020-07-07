#Analysis of the Dow Jones Industrial Average
#https://stooq.com/q/d/?s=^dji

import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_csv("dji_d.csv", parse_dates =["Date"]) # note that parse_dates is a  List

p = figure(width = 800, height = 500, x_axis_type = "datetime")
dodgerblue4 = "#104E8B" # custom color
p.title.text="Historical Values of the Dow Jones Industrial Average through Jun 2020"
p.title.text_color=dodgerblue4
p.title.text_font="times"
p.title.text_font_style="italic"
p.title.align = "center"
p.title.text_font_size = '16px'

p.line(df["Date"], df["Close"], color = "Orange", alpha = 0.5)

output_file("Historical_DJIA_Timeseries.html")
show(p)