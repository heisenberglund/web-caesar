from flask import Flask, request
from caesar import rotate_string

app =  Flask(__name__)
app.config['DEBUG'] = True



form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }

                #textarea{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }

            </style>
        </head>
        <body>
            <form method="POST">
                <label>Rotate by:
                </label>
                <input name="rot" type="text" value="0"/>
                </br>
                <input name="text" id="textarea" ></textarea>
                </br>
                <input type="submit" value="Submit"  
                 />

            </form>
        </body>
    </html>
"""


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']

    

    result = rotate_string(text, rot)
    
    return result


app.run()