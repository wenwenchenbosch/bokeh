from bokeh.layouts import column
import time
from bokeh.models import CustomJS, Div, FileInput
from bokeh.plotting import output_file, show

# Set up widgets
file_input = FileInput(accept=".csv,.json")
para = Div(text="<h1>FileInput Values:</h1><p>filename:<p>b64 value:")
def upload_fit_data(attr, old, new):
    print("fit data upload succeeded")
    #print(file_input.value)
    print(type(new))
    #f = open(decoded, "r")
    #contents = f.read()
    #print(contents)
# Create CustomJS callback to display file_input attributes on change
callback = CustomJS(args=dict(para=para, file_input=file_input), code="""
    para.text = "<h1>FileInput Values:</h1><p>filename: " + file_input.filename  + "<p>b64 value: " + file_input.value
""")

# Attach callback to FileInput widget
file_input.on_change('filename', upload_fit_data)
file_input.on_change('value', upload_fit_data)
file_input.js_on_change('value', callback)

output_file("file_input.html")

show(column(file_input, para))
