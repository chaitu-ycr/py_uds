import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

gui_app = dash.Dash(__name__)

gui_app.layout = html.Div([
    html.H1("UDS diagnostics"),
    dcc.Input(id="diag_request", type="text", placeholder="Enter diag request in byte stream"),
    html.Button("SEND", id="send_request"),
    html.Div(id="diag_response")
])

@gui_app.callback(
    Output("diag_response", "children"),
    [Input("send_request", "n_clicks")],
    [State("diag_request", "value")]
)
def process_input(n_clicks, textinput):
    if n_clicks is None:
        return ""  # Initial state
    elif textinput == "":
        return "No input"  # Do nothing if button is clicked and input is blank
    else:
        # Perform some calculations based on the input
        return f"diagnostic request [{textinput}] sent 🐱‍🏍successfully 👍"

if __name__ == "__main__":
    gui_app.run_server(debug=True)
