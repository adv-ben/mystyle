import plotly.express as px
import pandas as pd
import math

###
# Ben's styles for plotly
# Highlights
# 
# 
# Todo
# Matplotlib style
# Upload to github
###

def line_plot(x, 
              y, 
            title = "Default Title",
            xaxis_title = "x",
            yaxis_title = "y",
            step=False):
    
    if not step:
        df = pd.DataFrame(zip(x, y), columns=[xaxis_title, yaxis_title])
        fig = px.line(data_frame=df,
                    x=xaxis_title, 
                    y=yaxis_title, 
                    title=title)
    else:
        df = pd.DataFrame(zip(x, y), columns=[xaxis_title, yaxis_title])
        fig = px.line(data_frame=df,
                    x=xaxis_title, 
                    y=yaxis_title, 
                    title=title,
                        line_shape='hv')
    
    # Restrict zooming to only on x axis
    fig.update_layout(
        yaxis=dict(fixedrange=True)
    )

    return fig

def multi_line_plot(x_lines, 
                    y_lines,
                    yaxis_names, 
                    title = "Default Title",
                    xaxis_title = "x",
                    yaxis_title = "y",
                    step=False):
    # Plot multiple lines

    assert len(x_lines) == len(y_lines)
    assert len(x_lines) == len(yaxis_names)

    x_data = []
    y_data = []
    names = []
    for i in range(len(y_lines)):
        for (x, y) in zip(x_lines[i], y_lines[i]):
            x_data.append(x)
            y_data.append(y)
            names.append(yaxis_names[i])
            
    df = pd.DataFrame({
        xaxis_title: x_data,
        yaxis_title: y_data,
        'name': names
    })

    if not step:
        fig = px.line(data_frame=df ,
                        x=xaxis_title, 
                        y=yaxis_title, 
                        color='name',
                        title=title)
    else:
            fig = px.line(data_frame=df ,
                        x=xaxis_title, 
                        y=yaxis_title, 
                        color='name',
                        title=title,
                        line_shape='hv')

    # Restrict zooming to only on x axis
    fig.update_layout(
        yaxis=dict(fixedrange=True)
    )

    return fig

def time_format(time_in_seconds):
    num_yrs = math.floor(time_in_seconds // (86400 * 365.2425))
    time_in_seconds -= num_yrs * (86400 * 365.2425)
    num_days = math.floor(time_in_seconds // 86400)
    time_in_seconds -= num_days * 86400
    num_hrs = math.floor(time_in_seconds // 3600)
    time_in_seconds -= num_hrs * 3600
    num_mins = math.floor(time_in_seconds // 60)
    time_in_seconds -= num_mins * 60
    num_secs = math.floor(time_in_seconds)
    
    if num_yrs > 0:
        return f"{num_yrs}y {num_days}d"
    elif num_days > 0:
        return f"{num_days}d {num_hrs}h"
    elif num_hrs > 0:
        return f"{num_hrs}h {num_mins}m"
    elif num_mins > 0:
        return f"{num_mins}m {num_secs}s"
    elif time_in_seconds >= 10:
        time_in_seconds = math.floor(10 * time_in_seconds) / 10
        if time_in_seconds % 10 == 0:
            return f"{time_in_seconds:.3g}.0s"
        else:
            return f"{time_in_seconds:.3g}s"
    elif time_in_seconds >= 1:
        return f"{time_in_seconds:.3g}s"
    elif time_in_seconds >= 1e-3:
        return f"{(1e3 * time_in_seconds):.3g}ms"
    elif time_in_seconds >= 1e-6:
        return f"{(1e6 * time_in_seconds):.3g}us"
    elif time_in_seconds >= 1e-9:
        return f"{(1e9 * time_in_seconds):.3g}ns"
    else:
        return f"0ns"