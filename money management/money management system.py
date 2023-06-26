import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Total income (allowance + job)
total_income = 500 + 700

# Monthly bills
phone_bill = 38
miscellaneous = 20
total_bills = phone_bill + miscellaneous

# Daily lunch expense
lunch_expense_per_day = 7

# Amount to save
saving_goal = 700

# Calculate total available for daily expenses (excluding lunch)
daily_expenses_available = total_income - saving_goal - total_bills - (lunch_expense_per_day * 30)

# Calculate how much money should be spent each day (excluding lunch)
spending_per_day = daily_expenses_available / 30

expenses = ['Daily Expenses', 'Lunch', 'Phone Bill', 'Miscellaneous', 'Savings']
values = [daily_expenses_available, lunch_expense_per_day*30, phone_bill, miscellaneous, saving_goal]

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="input-money", type="number", placeholder="Input remaining money"),
    html.Button('Submit', id='submit-button', n_clicks=0),
    dcc.Graph(id='my-pie', figure={}),
    html.Div(id='my-output')
])

@app.callback(
    [Output(component_id='my-pie', component_property='figure'),
     Output(component_id='my-output', component_property='children')],
    [Input(component_id='submit-button', component_property='n_clicks')],
    [dash.dependencies.State(component_id='input-money', component_property='value')]
)
def update_output_div(n_clicks, value):
    if value is not None:
        values[0] = float(value) - sum(values[1:])
    
    fig = go.Figure(data=[go.Pie(labels=expenses, values=values)])
    return fig, f'You have €{values[0]} left for daily expenses for the rest of the month.'

if __name__ == '__main__':
    app.run_server(debug=True)
