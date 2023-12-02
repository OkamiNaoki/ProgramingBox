import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
from sklearn.decomposition import FactorAnalysis
import pandas as pd
from data_preprocessing_year import preprocess_data
from tulca.tulca import TULCA
from umap import UMAP
import tensorly as tl
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots

global_X = []
global_y = []
global_Z_tda = []
global_y_value=3
app = dash.Dash(__name__)

#scatterと、pulldownBarchartを一緒にするべき
#プルダウンメニューでTDAの大きさを決めれるようにする
#tensor分解と散布図による分析にする。
#散布図をパタパタ帰れるようにする

app.layout = html.Div([
    dcc.Slider(
        id='bar1-slider',
        min=1,
        max=global_y_value,
        step=1,
        value=1,
        marks={i: str(i) for i in range(1, global_y_value, 1)},
        tooltip={'placement': 'bottom'}
    ),
    dcc.Slider(
        id='bar2-slider',
        min=1,
        max=global_y_value,
        step=1,
        value=1,
        marks={i: str(i) for i in range(1, global_y_value+1, 1)},
        tooltip={'placement': 'bottom'}
    ),
    dcc.Slider(
        id='bar3-slider',
        min=1,
        max=global_y_value,
        step=1,
        value=1,
        marks={i: str(i) for i in range(1, global_y_value+1, 1)},
        tooltip={'placement': 'bottom'}
    ),
    html.Button('決定', id='submit-button', n_clicks=0),
    dcc.Graph(id='scatter-plot'),
    html.Button('ヒートマップ', id='heatmap-button', n_clicks=0),
    dcc.Graph(id='rack-pc-loadings'),
    html.Div(id='selected-data-output'),
    # 操作用のドロップダウン
    dcc.Dropdown(
        id='dropdown-column',
        options=[
            {'label': 'Column1', 'value': 'Column1'},
            {'label': 'Column2', 'value': 'Column2'},
            {'label': 'Column3', 'value': 'Column3'},
            {'label': 'Column4', 'value': 'Column4'},
            {'label': 'Column5', 'value': 'Column5'},
            {'label': 'Column6', 'value': 'Column6'},
            {'label': 'Column7', 'value': 'Column7'},
            {'label': 'Column8', 'value': 'Column8'}
        ],
        value='Column1',  # 初期選択値
        style={'width': '50%'}
    ),
    dcc.Graph(id='bar-chart')
    
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('bar1-slider', 'value'),
     State('bar2-slider', 'value'),
     State('bar3-slider', 'value')]
)
def display_scatter_plot(n_clicks, bar1_value, bar2_value, bar3_value):
    tg = [0] * global_y_value
    bg = [0] * global_y_value
    bw = [0] * global_y_value
    tg[bar1_value-1] = 1
    bg[bar2_value-1] = 1
    bw[bar3_value-1] = 1
    tulca = TULCA(n_components=np.array([10, 2]), w_tg=tg, w_bg=bg, w_bw=bw, optimization_method="evd")
    
    X_tda = tulca.fit_transform(global_X, global_y)
    rank = 3  # 分解のランク
    factors = tl.decomposition.parafac(X_tda, rank=rank)
    data={
        'Column1':factors[1][0][:, 0],
        'Column2':factors[1][0][:, 1],
        'Column3':factors[1][0][:, 2],
        'ColorIndex':global_y
    }
    df=pd.DataFrame(data)
    
    # fig=px.scatter(df,x=df['Column1'],y=df['Column2'],color=df['y'])
    # # 棒グラフを追加
    # fig.add_trace(px.scatter(df,x=df['Column1'],y=df['Column3'],color=df['y']))
    # fig.add_trace(px.scatter(df,x=df['Column2'],y=df['Column3'],color=df['y']))
    # return fig
    # Scatterグラフを作成
    # Scatterグラフを作成
    fig = px.scatter(df, x='Column1', y='Column2', color='ColorIndex',
                    labels={'Column1': 'X-Axis', 'Column2': 'Y-Axis'},
                    title='Scatter Plots')

    # 別の Scatter グラフを追加
    scatter_trace = go.Scatter(
        x=df['Column1'],
        y=df['Column3'],
        mode='markers',
        marker=dict(color=df['ColorIndex'], colorscale='Viridis'),
        text=df['ColorIndex'],
        showlegend=False,  # 凡例を表示しないように設定
        visible=True  # 初期表示を有効に設定
    )
    fig.add_trace(scatter_trace)

    # 別の Scatter グラフを追加
    scatter_trace2 = go.Scatter(
        x=df['Column2'],
        y=df['Column3'],
        mode='markers',
        marker=dict(color=df['ColorIndex'], colorscale='Viridis'),
        text=df['ColorIndex'],
        showlegend=False,  # 凡例を表示しないように設定
        visible=True  # 初期表示を有効に設定
    )
    fig.add_trace(scatter_trace2)

    # レイアウトの設定
    fig.update_layout(
        xaxis=dict(title='Column1 or Column2'),
        yaxis=dict(title='Column3'),
        coloraxis=dict(colorbar=dict(title='Color Index')),
        updatemenus=[
            {
                'buttons': [
                    {'label': 'All',
                    'method': 'relayout',
                    'args': ['showlegend', True]},
                    {'label': 'None',
                    'method': 'relayout',
                    'args': ['showlegend', False]},
                ],
                'direction': 'down',
                'showactive': True,
                'x': 0.01,
                'xanchor': 'left',
                'y': 1.15,
                'yanchor': 'top'
            },
            {
                'buttons': [
                    {'label': 'Scatter Plot Column1 vs. Column2',
                    'method': 'update',
                    'args': [{'visible': [True, False, False]}]},
                    {'label': 'Scatter Plot Column1 vs. Column3',
                    'method': 'update',
                    'args': [{'visible': [False, True, False]}]},
                    {'label': 'Scatter Plot Column2 vs. Column3',
                    'method': 'update',
                    'args': [{'visible': [False, False, True]}]}
                ],
                'direction': 'down',
                'showactive': True,
                'x': 0.01,
                'xanchor': 'left',
                'y': 1.05,
                'yanchor': 'top'
            }
        ]
    )

    # グラフを表示

    return fig

@app.callback(
    Output('rack-pc-loadings', 'figure'),
    [Input('heatmap-button', 'n_clicks')],
    [State('bar1-slider', 'value'),
     State('bar2-slider', 'value'),
     State('bar3-slider', 'value')]
)
def display_heat_map_plot(n_clicks, bar1_value, bar2_value, bar3_value):
    tg = [0] * 12
    bg = [0] * 12
    bw = [0] * 12
    tg[bar1_value] = 1
    bg[bar2_value] = 1
    bw[bar3_value] = 1
    tulca = TULCA(n_components=np.array([10, 2]), w_tg=tg, w_bg=bg, w_bw=bw, optimization_method="evd")
    
    X_tda = tulca.fit_transform(global_X, global_y)
    Us = tulca.get_projection_matrices()
    print(len(Us[0][:,1]))
    print(len(Us[0][0,:]))
    
    Z_heatmap =[]
    for i in range(10):
        heat=Us[0][:,i].reshape(36,24)
        Z_heatmap.append(heat)
    
    fig_heatmap = make_subplots(rows=10, cols=1, subplot_titles=[f'Heatmap {i+1}' for i in range(10)], shared_xaxes=True)

    for i in range(10):
        fig_heatmap.add_trace(go.Heatmap(
            z=Z_heatmap[i],
            x=[i for i in range(Z_heatmap[i].shape[1])],
            y=[i for i in range(Z_heatmap[i].shape[0])],
            colorscale='Viridis'
        ), row=i+1, col=1)

    fig_heatmap.update_layout(
        title='Heatmap Subplots',
        xaxis_title='X軸',
        yaxis_title='Y軸',
        height=3600,  # 適切な高さに調整
        width=360    # 適切な幅に調整
    )


    return fig_heatmap


@app.callback(
    Output('selected-data-output', 'children'),
    [Input('scatter-plot', 'selectedData')]
)
def display_selected_data(selectedData):
    if selectedData is None:
        return "選択されたデータはありません。"
    # 選択されたデータの座標を取得
    points = selectedData['points']
    # pointIndexでインデックスを取得可能
    selected_indices = [point['pointIndex'] for point in points]

    # 時系列に沿って864個のプロットを重ねて表示
    fig1 = go.Figure()

    # 以下が変更された部分です
    average_data = np.mean(global_X[:, :, 0], axis=1)
    fig1.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=average_data,
        mode='lines',
        name='Average Data'
    ))
    # selected_indices に基づいてハイライトする点を表示
    highlighted_points = np.full_like(average_data, np.nan)
    highlighted_points[selected_indices] = average_data[selected_indices]

    fig1.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=highlighted_points,
        mode='markers',
        marker=dict(
            size=8,
            color='red',  # ハイライトの色を設定
        ),
        name='Selected Points'
    ))

    # 新しいプロットを表示
        # 時系列に沿って864個のプロットを重ねて表示
    fig2 = go.Figure()

    # 以下が変更された部分です
    average_data = np.mean(global_X[:, :, 1], axis=1)
    fig2.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=average_data,
        mode='lines',
        name='Average Data'
    ))
    highlighted_points = np.full_like(average_data, np.nan)
    highlighted_points[selected_indices] = average_data[selected_indices]

    fig2.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=highlighted_points,
        mode='markers',
        marker=dict(
            size=8,
            color='red',  # ハイライトの色を設定
        ),
        name='Selected Points'
    ))

    # 新しいプロットを表示
        # 時系列に沿って864個のプロットを重ねて表示
    fig3 = go.Figure()

    # 以下が変更された部分です
    average_data = np.mean(global_X[:, :, 2], axis=1)
    fig3.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=average_data,
        mode='lines',
        name='Average Data'
    ))
    highlighted_points = np.full_like(average_data, np.nan)
    highlighted_points[selected_indices] = average_data[selected_indices]

    fig3.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=highlighted_points,
        mode='markers',
        marker=dict(
            size=8,
            color='red',  # ハイライトの色を設定
        ),
        name='Selected Points'
    ))

    # 新しいプロットを表示
        # 時系列に沿って864個のプロットを重ねて表示
        # 時系列に沿って864個のプロットを重ねて表示
    fig4 = go.Figure()

    # 以下が変更された部分です
    average_data = np.mean(global_X[:, :, 3], axis=1)
    fig4.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=average_data,
        mode='lines',
        name='Average Data'
    ))
    highlighted_points = np.full_like(average_data, np.nan)
    highlighted_points[selected_indices] = average_data[selected_indices]

    fig4.add_trace(go.Scatter(
        x=np.arange(average_data.shape[0]),
        y=highlighted_points,
        mode='markers',
        marker=dict(
            size=8,
            color='red',  # ハイライトの色を設定
        ),
        name='Selected Points'
    ))

        
    Z_heatmap =[]
    for i in selected_indices:
        heat=global_X[i,:,0].reshape(36,24)
        Z_heatmap.append(heat)
    
    fig_heatmap1 = make_subplots(rows=len(selected_indices), cols=1, subplot_titles=[f'Heatmap {i+1}' for i in range(10)], shared_xaxes=True)

    for i in range(len(selected_indices)):
        fig_heatmap1.add_trace(go.Heatmap(
            z=Z_heatmap[i],
            x=[i for i in range(Z_heatmap[i].shape[1])],
            y=[i for i in range(Z_heatmap[i].shape[0])],
            colorscale='Viridis'
        ), row=i+1, col=1)

    fig_heatmap1.update_layout(
        title='Heatmap Subplots',
        xaxis_title='X軸',
        yaxis_title='Y軸',
        height=360*len(selected_indices),  # 適切な高さに調整
        width=360    # 適切な幅に調整
    )
    Z_heatmap =[]
    for i in selected_indices:
        heat=global_X[i,:,1].reshape(36,24)
        Z_heatmap.append(heat)
    
    fig_heatmap2 = make_subplots(rows=len(selected_indices), cols=1, subplot_titles=[f'Heatmap {i+1}' for i in range(10)], shared_xaxes=True)

    for i in range(len(selected_indices)):
        fig_heatmap2.add_trace(go.Heatmap(
            z=Z_heatmap[i],
            x=[i for i in range(Z_heatmap[i].shape[1])],
            y=[i for i in range(Z_heatmap[i].shape[0])],
            colorscale='Viridis'
        ), row=i+1, col=1)

    fig_heatmap2.update_layout(
        title='Heatmap Subplots',
        xaxis_title='X軸',
        yaxis_title='Y軸',
        height=360*len(selected_indices),  # 適切な高さに調整
        width=360    # 適切な幅に調整
    )
    Z_heatmap =[]
    for i in selected_indices:
        heat=global_X[i,:,2].reshape(36,24)
        Z_heatmap.append(heat)
    
    fig_heatmap3 = make_subplots(rows=len(selected_indices), cols=1, subplot_titles=[f'Heatmap {i+1}' for i in range(10)], shared_xaxes=True)

    for i in range(len(selected_indices)):
        fig_heatmap3.add_trace(go.Heatmap(
            z=Z_heatmap[i],
            x=[i for i in range(Z_heatmap[i].shape[1])],
            y=[i for i in range(Z_heatmap[i].shape[0])],
            colorscale='Viridis'
        ), row=i+1, col=1)

    fig_heatmap3.update_layout(
        title='Heatmap Subplots',
        xaxis_title='X軸',
        yaxis_title='Y軸',
        height=360*len(selected_indices),  # 適切な高さに調整
        width=360    # 適切な幅に調整
    )
    Z_heatmap =[]
    for i in selected_indices:
        heat=global_X[i,:,3].reshape(36,24)
        Z_heatmap.append(heat)
    
    fig_heatmap4 = make_subplots(rows=len(selected_indices), cols=1, subplot_titles=[f'Heatmap {i+1}' for i in range(10)], shared_xaxes=True)

    for i in range(len(selected_indices)):
        fig_heatmap4.add_trace(go.Heatmap(
            z=Z_heatmap[i],
            x=[i for i in range(Z_heatmap[i].shape[1])],
            y=[i for i in range(Z_heatmap[i].shape[0])],
            colorscale='Viridis'
        ), row=i+1, col=1)

    fig_heatmap4.update_layout(
        title='Heatmap Subplots',
        xaxis_title='X軸',
        yaxis_title='Y軸',
        height=360*len(selected_indices),  # 適切な高さに調整
        width=360    # 適切な幅に調整
    )
    # 新しいプロットを表示
    fig1.show()
    fig2.show()
    fig3.show()
    fig4.show()
    fig_heatmap1.show()
    fig_heatmap2.show()
    fig_heatmap3.show()
    fig_heatmap4.show()
    
    print(selected_indices)
    return f"heat"

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('dropdown-column', 'value')],
    [State('bar1-slider', 'value'),
     State('bar2-slider', 'value'),
     State('bar3-slider', 'value')]
    
)
def display_heat_map_plot(selected_column, bar1_value, bar2_value, bar3_value):
    tg = [0] * 12
    bg = [0] * 12
    bw = [0] * 12
    tg[bar1_value] = 1
    bg[bar2_value] = 1
    bw[bar3_value] = 1
    tulca = TULCA(n_components=np.array([10, 2]), w_tg=tg, w_bg=bg, w_bw=bw, optimization_method="evd")
    
    X_tda = tulca.fit_transform(global_X, global_y)
    rank = 3  # 分解のランク
    factors = tl.decomposition.parafac(X_tda, rank=rank)
    Us = tulca.get_projection_matrices()
    data={
        'Column1':factors[1][1][:, 0],
        'Column2':factors[1][1][:, 1],
        'Column3':factors[1][1][:, 2],
        'Column4':factors[1][2][:, 0],
        'Column5':factors[1][2][:, 1],
        'Column6':factors[1][2][:, 2],
        'Column7':Us[1][:,0],
        'Column8':Us[1][:,1],
        'ColorIndex':global_y
    }
    x_range = np.arange(len(data[selected_column]))
    return {
        'data': [
            {'x': x_range, 'y': data[selected_column], 'type': 'bar', 'name': selected_column},
        ],
        'layout': {
            'title': f'Bar Chart - {selected_column}',
            'xaxis': {'title': 'ColorIndex'},
            'yaxis': {'title': 'Values'}
        }
    }

if __name__ == '__main__':
    global_X, global_y = preprocess_data()
    #global_y -= 1
    app.run_server(debug=True)
