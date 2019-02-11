'Pradeep Poddar'
'15MT3EP01'


from flask import Flask, request,render_template
from GBE import raganathan,triple_junction,list_formation
import numpy as np

app = Flask(__name__)

@app.route('/')
def test_home():
    return render_template('home.html')

@app.route('/misorientation')
def misorientation():
    return render_template('misorientation.html')

@app.route('/triple_junction')
def junction():
    return render_template('junction.html')


@app.route('/result_angle', methods=['GET','POST'])
def angle():
    try:
        if request.method=="POST":
            sigma=int(request.form.get('Sigma'))
            plan=list_formation(int(request.form.get('Axis')))
            angle=np.round(min(raganathan(sigma,plan)),1)
            angle=np.round(angle,2)
            return render_template('ang.html',mult=angle)
    except:
        message='For chosen Sigma and Axis CSL Boundry can not be formed'
        return render_template('ang.html',mult=message)

@app.route('/result_junction', methods=['GET','POST'])
def junction_cal():
    if request.method=="POST":
        sigma1=int(request.form.get('Sigma1'))
        sigma2=int(request.form.get('Sigma2'))
        sigma3=int(request.form.get('Sigma3'))
        axis=list_formation(int(request.form.get('Axis')))
        angle=triple_junction(sigma1,sigma2,sigma3,axis)
        if len(angle)==0:
            return render_template('jun.html')
        else:
            return render_template('mis.html',result=angle)
        


if __name__=="__main__" :
    app.run()
else: 
    print(__name__)