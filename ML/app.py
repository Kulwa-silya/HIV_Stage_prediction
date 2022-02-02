from flask import Flask , render_template, request
import predict as p

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def submit(stage_value=0):
    cxr, conf_yes ,csr_ve, ss_plus, ss_neg, tb_susp = 0,0,0,0,0,0
    OK, MOD = 0, 0
    if request.method == "POST":
        weight = request.form["weight"]
        ArvStatusCode =request.form["ArvStatusCode"]
        cd4 = request.form["cd4"]

        Tb_Screening_ID = request.form["Tb_Screening_ID"]
        # if Tb_Screening_ID in "cxr- cxr+ conf_yes csr_ve ss_plus ss_neg tb_susp".split():
        if Tb_Screening_ID == "cxr-":
            cxr = 1
        if Tb_Screening_ID == "conf_yes":
            conf_yes = 1
        if Tb_Screening_ID == "csr_ve":
            csr_ve = 1
        if Tb_Screening_ID == "ss_plus":
            ss_plus = 1
        if Tb_Screening_ID == "ss_neg":
            ss_neg = 1
        if Tb_Screening_ID == "tb_susp":
            tb_susp = 1
    
        NutritionalStatusId = request.form["NutritionalStatusId"]
        OK, MOD = 0,0
        if NutritionalStatusId == "OK":
            OK = 1
        if NutritionalStatusId == "MOD":
            MOD = 1

        functionalStatusId = request.form["functionalStatusId"]
        Bedridden, Working = 0,0
        if functionalStatusId == "Bedridden":
            Bedridden = 1
        if functionalStatusId == "Working":
            Working = 1
        
        ARVAdherenceCode = request.form["ARVAdherenceCode"]
        poor = 0
        if ARVAdherenceCode == "p":
            poor = 1

        patient_stage = p.inference(weight, ArvStatusCode, cd4, cxr, conf_yes ,csr_ve, ss_plus, ss_neg, tb_susp, OK, MOD, Bedridden, Working, poor)
        stage_value = patient_stage
        print((stage_value[0][0]))
   
    return render_template("index.html", stage = stage_value)

if __name__ == "__main__":
    app.run(debug=True)
