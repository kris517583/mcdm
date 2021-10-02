from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import simpful as sf
from numpy import *

def rank(arr):
    temp = arange(len(arr))
    temp.fill(-1)
    n = len(arr)
    for i in range(n):
        index = where(isclose(arr,max(arr)))
        temp[index[0][0]] = i+1
        arr[index[0][0]] = -9999
    return temp

app = Flask(__name__)
@app.route('/', methods = ['POST'])
def home():
    if(request.method == 'POST'):
        #data = request.get_json()
        print(request.json)
        inputs = ["Accountability","Agility","Assurance","Financial","Performance","Security","Usability"]
        rulesframe = [
              [["Good","Very_Good"],["Medium","Good"],["Good","Very_Good"],["Medium","Good"],["Good","Very_Good"],["Good","Very_Good"],["Good","Very_Good"]],
              [["Good","Very_Good"],["Medium","Good"],["Medium","Good"],["Good","Very_Good"],["Good","Very_Good"],["Good","Very_Good"],["Good","Very_Good"]],
              [["Good","Very_Good"],["Medium","Good"],["Good","Very_Good"],["Medium","Good"],["Good","Very_Good"],["Good","Very_Good"],["Good","Very_Good"]],
              [["Good","Very_Good"],["Medium","Good"],["Medium","Good"],["Very_Low","Very_Low"],["Medium","Good"],["Good","Very_Good"],["Medium","Good"]],
              [["Good","Very_Good"],["Medium","Good"],["Good","Very_Good"],["Medium","Good"],["Medium","Good"],["Good","Very_Good"],["Medium","Good"]]
             ]
        scale = ["Very_Low","Low","Medium","Good","Very_Good"]
        rate = [1,2,3,4,5]

        FS = sf.FuzzySystem()
        S_1 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low")
        S_2 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low")
        S_3 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium")
        S_4 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good")
        S_5 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good")
        FS.add_linguistic_variable("Accountability", sf.LinguisticVariable( [S_1, S_2, S_3,S_4,S_5] ))

        S_6 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low" )
        S_7 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low" )
        S_8 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium" )
        S_9 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good" )
        S_10 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good" )
        FS.add_linguistic_variable("Agility", sf.LinguisticVariable( [S_6, S_7, S_8,S_9,S_10] ))

        S_11 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low" )
        S_12 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low" )
        S_13 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium" )
        S_14 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good" )
        S_15 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good" )
        FS.add_linguistic_variable("Assurance", sf.LinguisticVariable( [S_11, S_12, S_13,S_14,S_15] ))

        S_16 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low" )
        S_17 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low" )
        S_18 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium" )
        S_19 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good" )
        S_20 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good" )
        FS.add_linguistic_variable("Financial", sf.LinguisticVariable( [S_16, S_17, S_18,S_19,S_20] ))

        S_21 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low" )
        S_22 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low" )
        S_23 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium" )
        S_24 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good" )
        S_25 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good" )
        FS.add_linguistic_variable("Performance", sf.LinguisticVariable( [S_21, S_22, S_23,S_24,S_25] ))

        S_26 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low" )
        S_27 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low" )
        S_28 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium" )
        S_29 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good" )
        S_30 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good" )
        FS.add_linguistic_variable("Security", sf.LinguisticVariable( [S_26, S_27, S_28,S_29,S_30] ))

        S_31 = sf.FuzzySet( points=[[0,0],[0.2,1],[0.4,0]],term="Very_Low" )
        S_32 = sf.FuzzySet( points=[[0.2,0],[0.4,1],[0.6,0]],term="Low" )
        S_33 = sf.FuzzySet( points=[[0.4,0],[0.6,1],[0.8,0]],term="Medium" )
        S_34 = sf.FuzzySet( points=[[0.6,0],[0.8,1],[0.9,0]],term="Good" )
        S_35 = sf.FuzzySet( points=[[0.8,0],[0.9,1],[1,0]],term="Very_Good" )
        FS.add_linguistic_variable("Usability", sf.LinguisticVariable( [S_31, S_32, S_33,S_34,S_35] ))

        FS.set_output_function("Very_Low","(0.2*Accountability+0.5*Agility+0.5*Assurance+0.8*Financial+0.7*Performance+0.3*Security+0.2*Usability)")
        FS.set_output_function("Low","(0.2*Accountability+0.5*Agility+0.5*Assurance+0.8*Financial+0.7*Performance+0.3*Security+0.2*Usability + 0.25)")
        FS.set_output_function("Medium","(0.2*Accountability+0.5*Agility+0.5*Assurance+0.8*Financial+0.7*Performance+0.3*Security+0.2*Usability+ 0.5)")
        FS.set_output_function("Good","(0.2*Accountability+0.5*Agility+0.5*Assurance+0.8*Financial+0.7*Performance+0.3*Security+0.2*Usability +0.75)")
        FS.set_output_function("Very_Good","(0.2*Accountability+0.5*Agility+0.5*Assurance+0.8*Financial+0.7*Performance+0.3*Security+0.2*Usability + 1)")

        RULE1 = "IF ((Accountability IS Very_Low) AND (Agility IS Very_Low) AND (Assurance IS Very_Low) AND (Financial IS Very_Low) AND (Performance IS Very_Low) AND (Security IS Very_Low) AND (Usability IS Very_Low))THEN (Out IS Very_Bad)"
        RULE2 = "IF ((Accountability IS Low) AND (Agility IS Low) AND (Assurance IS Low) AND (Financial IS Low) AND (Performance IS Low) AND (Security IS Low) AND (Usability IS Low))THEN (Out IS Bad)"
        RULE3 = "IF ((Accountability IS Medium) AND (Agility IS Medium) AND (Assurance IS Medium) AND (Financial IS Medium) AND (Performance IS Medium) AND (Security IS Medium) AND (Usability IS Medium))THEN (Out IS Medium)"
        RULE4 = "IF ((Accountability IS Good) AND (Agility IS Good) AND (Assurance IS Good) AND (Financial IS Good) AND (Performance IS Very_Low) AND (Security IS Good) AND (Usability IS Good))THEN (Out IS Good)"
        RULE5 = "IF ((Accountability IS Very_Good) AND (Agility IS Very_Good) AND (Assurance IS Very_Good) AND (Financial IS Very_Good) AND (Performance IS Very_Good) AND (Security IS Very_Good) AND (Usability IS Very_Good))THEN (Out IS Very_Good)"

        FS.add_rules([RULE1, RULE2, RULE3, RULE4, RULE5])

        response = request.json["response"]
        userinput = []
        ruleset = set([])
        userrate = []
        userdef = ""
        for i in range(len(response)):
            userinput.append(response[i]["name"])
            userrate.append(rate[scale.index(response[i]["rangeVal"])])
            if i == len(response)-1 :
                userdef = userdef + "(" + response[i]["name"] + " IS " + response[i]["rangeVal"] + ")"
            else:
                userdef = userdef + "(" + response[i]["name"] + " IS " + response[i]["rangeVal"] + ") AND "

        userdef = "IF ("+ userdef +") THEN (Out IS Very_Good)"
        ruleset.add(userdef)
        for i in range(len(rulesframe)):
            for j in range(2):
                temp = "IF ("
                relativedecrease = 0
                for k in range(len(userinput)):
                    if k == len(userinput) - 1:
                        temp = temp + "(" + userinput[k] + " IS " + rulesframe[i][inputs.index(userinput[k])][j] + ")"
                    else:
                        temp = temp + "(" + userinput[k] + " IS " + rulesframe[i][inputs.index(userinput[k])][j] + ") AND "
                    rel = userrate[k] - rate[scale.index(rulesframe[i][inputs.index(userinput[k])][j])]
                    if rel>relativedecrease :
                        relativedecrease = rel
                val = scale[4-relativedecrease]
                temp = temp + ") THEN (Out IS "+ val +")"
                ruleset.add(temp)
        for i in ruleset:
            FS.add_rules([i])

        outs = []
        data = {}
        FS.set_variable("Accountability",0.98)
        FS.set_variable("Agility",0.7)
        FS.set_variable("Assurance",0.9)
        FS.set_variable("Financial",0.767)
        FS.set_variable("Performance",0.9)
        FS.set_variable("Security",0.98)
        FS.set_variable("Usability",0.85)
        data["CSP1"] = {}

        data["CSP1"]["Out"] = FS.Sugeno_inference(['Out'])['Out']
        data["CSP1"]["Name"] = "AWS"
        data["CSP1"]["Rank"] = -1
        outs.append(data["CSP1"]["Out"])

        FS.set_variable("Accountability",0.95)
        FS.set_variable("Agility",0.7)
        FS.set_variable("Assurance",0.675)
        FS.set_variable("Financial",0.833)
        FS.set_variable("Performance",0.833)
        FS.set_variable("Security",0.96)
        FS.set_variable("Usability",0.9)
        data["CSP2"] = {}

        data["CSP2"]["Out"] = FS.Sugeno_inference(['Out'])['Out']
        data["CSP2"]["Name"] = "Azure"
        data["CSP2"]["Rank"] = -1
        outs.append(data["CSP2"]["Out"])

        FS.set_variable("Accountability",0.93)
        FS.set_variable("Agility",0.64)
        FS.set_variable("Assurance",0.825)
        FS.set_variable("Financial",0.733)
        FS.set_variable("Performance",0.833)
        FS.set_variable("Security",0.97)
        FS.set_variable("Usability",0.8)
        data["CSP3"] = {}

        data["CSP3"]["Out"] = FS.Sugeno_inference(['Out'])['Out']
        data["CSP3"]["Name"] = "Google Cloud"
        data["CSP3"]["Rank"] = -1
        outs.append(data["CSP3"]["Out"])

        FS.set_variable("Accountability",0.8)
        FS.set_variable("Agility",0.66)
        FS.set_variable("Assurance",0.7)
        FS.set_variable("Financial",0.167)
        FS.set_variable("Performance",0.7)
        FS.set_variable("Security",0.8)
        FS.set_variable("Usability",0.75)
        data["CSP4"] = {}

        data["CSP4"]["Out"] = FS.Sugeno_inference(['Out'])['Out']
        data["CSP4"]["Name"] = "Rackspace"
        data["CSP4"]["Rank"] = -1
        outs.append(data["CSP4"]["Out"])

        FS.set_variable("Accountability",0.92)
        FS.set_variable("Agility",0.68)
        FS.set_variable("Assurance",0.875)
        FS.set_variable("Financial",0.667)
        FS.set_variable("Performance",0.767)
        FS.set_variable("Security",0.89)
        FS.set_variable("Usability",0.83)
        data["CSP5"] = {}

        data["CSP5"]["Out"] = FS.Sugeno_inference(['Out'])['Out']
        data["CSP5"]["Name"] = "Alibaba"
        data["CSP5"]["Rank"] = -1
        outs.append(data["CSP5"]["Out"])
        outranks = rank(outs)
        for i in range(len(outranks)):
            data["CSP"+str(i+1)]["Rank"] = int(outranks[i])

        return jsonify({'response': data})

@app.route('/check', methods = ['POST'])
def check():
    if(request.method == "POST"):
        userdef = ""
        k = request.json["response"]
        for i in range(len(k)):
            if i == len(k)-1 :
                userdef = userdef + "(" + k[i]["name"] + " IS " + k[i]["rangeVal"] + ")"
            else:
                userdef = userdef + "(" + k[i]["name"] + " IS " + k[i]["rangeVal"] + ") AND "
        print(userdef)
        return jsonify({'data': 'hi'})

if __name__ == '__main__':
    app.run(debug = True)