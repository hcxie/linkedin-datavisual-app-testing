import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def read_merge_data(filename):
    df=pd.read_csv(filename)
    df.set_index(pd.DatetimeIndex(df['date']),inplace=True)
    df['yearmonth']=pd.to_datetime(df['date'], format='%Y/%m').map(lambda x: x.year)
    df.drop(['date'],axis=1,inplace=True) 
    return df
	
tempdf=read_merge_data('it_merge_df.csv')
x_labels=tempdf['yearmonth']
available_indicators=list(tempdf.columns[0:2])
available_indicators2=list(tempdf.columns[2:7])

sector_list={
				1:'real_estate',#XLRE
				2:'utilities',#XLU
				3:'it',#XLK
				4:'financial',#XLF
				5:'healthcare',#XLV
				6:'consumer_staples',#XLP
				7:'consumer_discretionary',#XLY
				8:'basic_material',#XLB
				9:'energy',#XLE
				10:'industrials'}#XLI

sector_name=[val for key,val in sector_list.items()]
server = app.server
app.layout = html.Div([
    html.Div([

        html.Div([
			html.Label('Sector Dropdown'),
            dcc.Dropdown(
				id='sector_dropdown',
				options=[
					{'label': 'Real Estate', 'value': 1},
					{'label': 'Utilities', 'value': 2},
					{'label': 'IT', 'value': 3},
					{'label': 'Financial', 'value': 4},
					{'label': 'Healthcare', 'value': 5},
					{'label': 'Consumer Staples', 'value': 6},
					{'label': 'Consumer Discretionary', 'value': 7},
					{'label': 'Basic Material', 'value': 8},
					{'label': 'Energy', 'value': 9},
					{'label': 'Industrials', 'value': 10}
					
				],
				value=[3],
				multi=True
		)],
		style={'width': '48%', 'display': 'inline-block'}),
		
		
		

		html.Div([
			html.Label('Linkedin info Dropdown'),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='employees_on_platform'
            ),
            
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),


    dcc.Graph(id='indicator-graphic'),
	
	
		
	html.Div([
			html.Label('time-slider'),
			dcc.Slider(
					id='year--slider',
					min=x_labels.min(),
					max=x_labels.max(),
					value=x_labels.max(),
					marks={str(year): str(year)[2:] for year in x_labels.unique()},
					step=20
			)],
			style={'width': '99%'}),

			
    html.Div([

		html.Div([
			html.Label('Stock Feature'),
            dcc.Dropdown(
                id='yaxis-column2',
                options=[{'label': i, 'value': i} for i in available_indicators2],
                value='adj_close_stock'
            ),
            
        ],style={'width': '99%'})
    ]),

    dcc.Graph(id='indicator-graphic2'),
	
	
		
	html.Div([
			html.Label('time-slider'),
			dcc.Slider(
					id='year--slider2',
					min=x_labels.min(),
					max=x_labels.max(),
					value=x_labels.max(),
					marks={str(year): str(year)[2:] for year in x_labels.unique()},
					step=20
			)],
			style={'width': '99%'}),

])


@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('year--slider', 'value'),
     Input('yaxis-column', 'value'),
     Input('sector_dropdown', 'value'),
     ])
def update_graph(selected_year,yaxis_column_name,sector_dropdown):
	traces=[]
	for i in sector_dropdown:
		sector_file_name=sector_list[i]+'_merge_df.csv'
		tempdf=read_merge_data(sector_file_name)
		sector_tempdf=tempdf[tempdf['yearmonth']<=selected_year]
		traces.append(go.Scatter(
            x=sector_tempdf.index,
            y=sector_tempdf[yaxis_column_name],
            #text=df_by_continent['country'],
            mode='lines',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
			))
	
	

	return {
        'data': traces,
        'layout': go.Layout(
            xaxis={
                'title': 'Year',
                
            },
            yaxis={
                'title': yaxis_column_name,
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }
	
@app.callback(
    Output('indicator-graphic2', 'figure'),
    [Input('year--slider2', 'value'),
     Input('yaxis-column2', 'value'),
     Input('sector_dropdown', 'value'),
     ])
def update_graph(selected_year,yaxis_column_name,sector_dropdown):
	traces=[]
	for i in sector_dropdown:
		sector_file_name=sector_list[i]+'_merge_df.csv'
		tempdf=read_merge_data(sector_file_name)
		sector_tempdf=tempdf[tempdf['yearmonth']<=selected_year]
		traces.append(go.Scatter(
            x=sector_tempdf.index,
            y=sector_tempdf[yaxis_column_name],
            #text=df_by_continent['country'],
            mode='lines',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
			))
	
	

	return {
        'data': traces,
        'layout': go.Layout(
            xaxis={
                'title': 'Year',
                
            },
            yaxis={
                'title': yaxis_column_name,
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)