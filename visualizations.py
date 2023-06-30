import pandas as pd
import plotly.graph_objects as go
import numpy as np
import re

def visualize_saliency(data, c_or_t):
    num_bins = 5
    category_bins_texture = pd.cut(data['texture saliency'], bins=num_bins)
    category_bins_color = pd.cut(data['color saliency'], bins=num_bins)


    # Create a new column in the DataFrame to represent the category bins
    data['category bin color'] = category_bins_color.astype(str)
    data['category bin texture'] = category_bins_texture.astype(str)


    input_types = ['caption', 'name', 'real']

    # Create the grouped bar chart
    

    figs = []

    # columns to process
    columns = list(data.columns)
    columns.remove('color saliency')
    columns.remove('texture saliency')
    string_to_match = 'to boolean'

    for input in input_types:

        fig = go.Figure(layout_yaxis_range=[0,1])

        for column in columns:
            if string_to_match in column and c_or_t in column and input in column and 'max_new_tokens' not in column:

                    
                    grouped_data = data.groupby([f'category bin {c_or_t}', column]).size().unstack().reset_index().fillna(0)

                    if True not in grouped_data.columns:
                        grouped_data[True] = 0

                    grouped_data['percentage'] = grouped_data.apply(lambda row: row[True] / (row[True] + row[False]), axis=1)

                    # print(column)
                    # print(grouped_data)
                    
                    new_name = re.sub(r'\s+to boolean', '', re.sub(r'{},+\s'.format(c_or_t), '', column))
                    bar_trace = go.Bar(
                            x=grouped_data[f'category bin {c_or_t}'],
                            y=grouped_data['percentage'],
                            name=f'{new_name}',
                        )
                    
                    fig.add_trace(bar_trace)

        # Create the layout for the grouped bar chart
        fig.update_layout(
            width=1000,
            title=f'{c_or_t} term usage rate per saliency bin for BLIP-2, {input}',
            xaxis=dict(title='Texture saliency in %', tickmode = 'array',
                    tickvals = [0, 1, 2, 3, 4],
                ticktext = ['0-20', '21-40', '41-60', '61-80', '81-100']),
            yaxis=dict(title=f'Rate of using {c_or_t} terms'),
            barmode='group')
        
        figs.append(fig)
    
    
    return figs