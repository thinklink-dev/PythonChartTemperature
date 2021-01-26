"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from PythonChartTemperature import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/chart')
def chart():
    from bokeh.plotting import figure, output_file, show, ColumnDataSource
    from bokeh.embed import components
    import pandas

    # Read CSV File Temperature data
    df = pandas.read_csv('PythonChartTemperature/temperature.csv')

    # Create DATASOURCE from data
    source = ColumnDataSource(df)

    # List
    box_list = source.data['Cajon'].tolist()

    p = figure(
        y_range = box_list,
        plot_width = 800,
        plot_height = 600,
        title = 'Temperatura de Cajones',
        x_axis_label = 'Temperatura',
        tools = "pan, box_select, zoom_in, zoom_out, save, reset"        
    )

    p.hbar(
        y = 'Cajon',
        right = 'Temperatura',
        left = 0,
        height = 0.4,
        color = 'orange',
        fill_alpha = 0.5,
        source = source
    )
    
    script, div = components(p)

    return render_template('chart.html', script=script, div=div)

