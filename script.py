import pyqrcode
import png
import flask
from pyqrcode import QRCode
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route( '/qr-code', methods=['GET'] )
def genQR():

   if 'string' in request.args:
      QRString = request.args['string']
   else:
      return "You must provide a string."

   if 'fileName' in request.args:
      fileName = request.args['fileName']
   else:
      return "You must provide a file name"

   # QRString = 'https://www.alegreshow.com.br'

   url = pyqrcode.create(QRString)

   url.png(r'qr-codes/' + fileName + '.png', scale = 8)

   return "<img src='qr-codes/'"+ fileName +".png'/>"

app.run()