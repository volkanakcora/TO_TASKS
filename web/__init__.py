import dash
from dash import html
from dash import dcc
import sys
import os


print(os.getcwd())
#os.chdir('/usr/local/lib/python3.8/site-packages/chuchnorris')

class web_app():
    """
    Web Application class.
    """
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.devnull, "w")
    
    app = dash.Dash()
    
    app.layout = html.Div([
        dcc.Interval(id='interval1', interval=1 * 1000, 
    n_intervals=0),
        dcc.Interval(id='interval2', interval=5 * 1000, 
    n_intervals=0),
        html.H1(id='div-out', children=''),
        html.Iframe(id='console-out',srcDoc='',style={'width': 
    '100%','height':400})
    ])

    @app.callback(dash.dependencies.Output('div-out', 
    'children'),
        [dash.dependencies.Input('interval1', 'n_intervals')])
    def update_interval(n):
        orig_stdout = sys.stdout
        #f = open('jokes.txt', 'a')
        #sys.stdout = f
        print ('Intervals Passed: ' + str(n))
        sys.stdout = orig_stdout
        #f.close()
        
    @app.callback(dash.dependencies.Output('console-out', 
    'srcDoc'),
    [dash.dependencies.Input('interval2', 'n_intervals')])
    def update_output(self):
        os.chdir('./')
        print(os.getcwd())
        file = open('jokes.txt', 'r')
        print(file)
        data=''
        lines = file.readlines()
        if lines.__len__()<=20:
            last_lines=lines
        else:
            last_lines = lines[-20:]
        for line in last_lines:
            data=data+line 
        file.close()
        return data
    

    def run(self):
        """Run the app."""

        self.app.run_server()

    #!------------------------------------------------------------------------

def main(): 
    web_app().run()

if __name__ == "__main__":
   main()