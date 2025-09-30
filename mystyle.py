import plotly.express as px
import pandas as pd

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