from flask import Flask, render_template,request
from PIL import Image
import cv2
import numpy as np
import face_recognition

app=Flask(__name__)

@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def predict():

    image = request.files['imagefile']
    #img = Image.open(image)
    #numpydata =np.asarray(img)
    #n=numpydata.shape
    rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]
    '''vinay=np.array([-0.19157137,  0.06850691,  0.07934873, -0.06794046, -0.01727131,
       -0.07596636,  0.02868884, -0.04736945,  0.15076506, -0.03761225,
        0.28175753, -0.08739531, -0.21705715, -0.14819907,  0.02326576,
        0.08962337, -0.18536565, -0.09204158, -0.02149376, -0.1646942 ,
        0.04024729,  0.06367583,  0.038443  ,  0.03517569, -0.1461761 ,
       -0.33553091, -0.08809772, -0.14187692,  0.04080311, -0.08906769,
       -0.01247013,  0.0832756 , -0.21810627, -0.08980942, -0.00038522,
        0.10127488,  0.04409426, -0.01030026,  0.10831405, -0.03331332,
       -0.08438455, -0.10973282,  0.06105034,  0.26822063,  0.10699487,
        0.08277453, -0.04430381, -0.01687061, -0.00137593, -0.19687745,
        0.08091894,  0.11540367,  0.08652898, -0.00873188,  0.04979638,
       -0.13055068, -0.00455916,  0.06067426, -0.18227744,  0.01765263,
        0.06166349, -0.10244043, -0.04059057, -0.02978872,  0.28204373,
        0.10230879, -0.10204205, -0.06018587,  0.1681944 , -0.08871274,
        0.00589845,  0.09086667, -0.06980862, -0.12645712, -0.2393146 ,
        0.08277811,  0.38116693,  0.05233041, -0.14342155,  0.00713713,
       -0.17042789, -0.02701716,  0.06275202,  0.00749566, -0.12667254,
        0.03064096, -0.16912527,  0.07049356,  0.14900567,  0.00051171,
       -0.0201486 ,  0.17595482, -0.03620774,  0.0133195 ,  0.05453828,
        0.02279649, -0.09770176, -0.00595593, -0.08596404, -0.02103219,
        0.11231838, -0.11545122, -0.05184991,  0.1305223 , -0.18462381,
        0.06212949,  0.0278845 , -0.09491114, -0.01086594, -0.03741958,
       -0.03946448, -0.0695332 ,  0.12153854, -0.25870293,  0.12731189,
        0.14095271,  0.00474058,  0.22423406,  0.00645646,  0.08243787,
       -0.04738416, -0.09775048, -0.13946912, -0.04390322,  0.07475764,
       -0.02754782,  0.07629612,  0.03196444])'''
    #if vinay==img_encoding:
    #    k=1
    #else:
    #    k=0
    return render_template('index.html',ver=img_encoding)

if __name__ == 'main':
    app.run()