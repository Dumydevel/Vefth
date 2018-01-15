from bottle import *
import os

@route('/')
def vid():
    return """
    <!DOCTYPE html>
           <html>
               <head>
                   <title>Mass effect</title>
                   <meta charset="utf-8">
                   

               </head>
               <body>
                   <ul>
                       <li><a href="http://tsuts.tskoli.is/2t/0711992829/vsh2/verkefni6">Mass effect</a></li>
                       <li><a href="http://tsuts.tskoli.is/2t/0711992829/Verkefni1/verkefni1.html">Biography</a></li>
                       <li><a href="/pic">Pictures</a></li>
                   </ul>

                   <h1>Mass effect</h1>
                    <img src="static/mass-effect-3.jpg" alt="Mass effect">
               </body>
           </html>
        j"""



@route('/verkefni6/')
def verk6 ():
    return static_file(filename="http://tsuts.tskoli.is/2t/0711992829/vsh2/verkefni6",root="http://tsuts.tskoli.is/2t/0711992829/vsh2/verkefni6")
@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

@error(404)
def error404(error):
    return '<p>UmbeÃƒÂ°in sÃƒÂ­ÃƒÂ°a er ekki til</p><a href="/">Mass effect</a>'

run(host='0.0.0.0', port=os.environ.get('PORT'))
#run(host='localhost', port=8080, debug=True)


