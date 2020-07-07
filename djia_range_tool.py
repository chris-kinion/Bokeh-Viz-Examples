# Implementation of bokeh range tool using time series csv
# File dji_dc.csv modified using MS Excel to limit time frame, columns and format dates
# https://docs.bokeh.org/en/latest/docs/gallery/range_tool.html
import pandas as pd

from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool
from bokeh.plotting import figure

#pandas dataframes
pdates = pd.read_csv('dji_dc.csv', usecols=['Date']).values
dates = (pdates[:,0])
dates = pd.to_datetime(dates) # enables use of Range1d datatype in p.x_range
pcloses = pd.read_csv('dji_dc.csv', usecols=['Close']).values
closes = pcloses[:,0]

source = ColumnDataSource(data=dict(date=dates, close=closes))

ubound = len(dates) - 1
lbound = ubound - 5000
p = figure(plot_height = 300, plot_width = 800, x_axis_type="datetime", x_axis_location="above",
          x_range=(dates[lbound], dates[ubound]))
p.title.text="Dow Jones Industrial Average Jan 1961 - Jun 2020"
p.title.text_color="firebrick"
p.title.text_font="times"
p.title.align = "center"
p.title.text_font_size = '1.5em'
p.line('date', 'close', source=source)
p.yaxis.axis_label = 'Close'

select = figure(title="Drag the middle and edges of the selection box to change the range above",
                plot_height=130, plot_width=800, y_range=p.y_range,
                x_axis_type="datetime", y_axis_type=None,
                tools="", toolbar_location=None, background_fill_color="#efefef")

range_tool = RangeTool(x_range=p.x_range)
range_tool.overlay.fill_color = "navy"
range_tool.overlay.fill_alpha = 0.2

select.line('date', 'close', source=source)
select.ygrid.grid_line_color = None
select.add_tools(range_tool)
select.toolbar.active_multi = range_tool

output_file("Historical_DJIA_RangeTool.html")
show(column(p, select))