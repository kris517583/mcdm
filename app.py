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
        k = request.json["all_reports"]
        print(k)
        return jsonify({'data': 'hi'})

@app.route('/storage', methods = ['POST'])
def storage():
    if(request.method == "POST"):
        data = request.json["all_reports"]
        result = []
        weights = [0,0,0,0,0,0]
        for i in data:
            if i["TAB"]  == "3" :
                result.append(i)

        tab3 = {
        "5848fce2-a6de-43bf-a878-cc8e63687f06" : {
            "Web applicaiton" : [1,0,0,0,0,0],
            "Big data analytics" :  [1,0,0,0,0,0],
            "Data storage" :  [1,1,0,0,0,0],
            "File sharing" :  [0,1,1,0,0,0],
            "Data backup" :  [0,0,0,1,1,0],
            "Video streaming" :  [0,0,0,0,0,0],
            "Social media" :  [0,0,0,0,0,0],
            "Financial Application" :  [0,0,0,0,0,0],
            "Local archive" :  [0,0,1,0,0,0],
            "Scientific modelling" : [0,1,0,0,0,0],
            "Gaming Application" :  [1,0,0,0,0,0]
        },
        "1d820edb-424c-4442-b15f-929e1fcf7e02" : {
            "Less than 1000" : [0,0,0,0,0,0],
            "1000 to 1 million" : [0,0,0,0,0,0],
            "More than 1 million" :[0,0,0,0,0,0]
        },
        "9b93c7ed-de5a-4da7-8914-6c4fecb2e653" : {
            "Once in a week" : [1,1,1,0,0,0],
            "Once in a month" : [0,0,0,1,0,0],
            "Once in a year" : [0,0,0,0,1,0]
        },
        "1af7ea0c-5568-4d43-8248-74f423f4a30e" : {
            "Photos and Videos" : [1,1,0,0,0,0],
            "Music" : [1,1,0,0,0,0],
            "Numerical data" : [0,1,0,0,0,0],
            "Text data" : [1,1,0,0,0,0]
        },
        "a82279df-7ce2-4fbc-a3cc-bff3766a4bf8" : {
            "Yes" : [1,1,1,0,0,0],
            "No" : [0,0,0,0,0,0]
        },
        "c6236767-d347-44e7-9b5c-3fcba2144410" : {
            "Yes" : [1,0,0,0,0,0],
            "No" : [0,1,1,0,0,0]    
        },
        "bff16ea2-7e48-42e4-b749-fe75bf01cc62" :{
            "Yes" : [0,0,0,0,0,0],
            "No" : [0,0,0,0,0,0]    
        },
        "9c14beaa-1b87-4666-b067-4dafb5ba0dc0" :{
            "Yes" : [0,0,0,0,0,1],
            "No" : [0,0,0,0,0,0]    
        },
        "07b4b16d-6fcb-4be6-a7fb-14ffff16c487" :{
            "Yes" : [0,0,0,0,1,0],
            "No" : [0,0,0,0,0,0]    
        },
        "86a757f6-3bf9-4caf-9688-b4e787533f14" :{
            "Yes" : [0,0,1,0,0,0],
            "No" : [0,0,0,0,0,0]
        },
        "64183286-50e3-47b6-894b-6db050156d15" :{
            "Dev" : [0,0,0,0,0,0],
            "Staging" : [0,0,0,0,0,0],
            "Prod" : [0,0,0,0,0,0]
        },
        "0ca3e6e7-89ce-4932-a0bc-b5c4eb9e5f0d" :{
            "Seasonal peaks" : [0,0,0,0,0,0],
            "Certain time every day" : [0,0,0,0,0,0],
            "All time" : [0,0,0,0,0,0],
            "Not much traffic" : [0,0,0,0,0,0],
            "Not sure" : [0,0,0,0,0,0]
        },
        "9553e4d6-dd7e-46f5-ad89-a28edb63de05" :{
            "Faster" : [0,0,0,0,0,0],
            "Slower" : [0,0,0,0,0,0],
            "Not sure" : [0,0,0,0,0,0]
        },
        "0454a74d-2223-4914-89ef-89eccb7670cb": {
            "Low" : [0,0,0,0,0,0],
            "Low to Moderate" : [0,0,0,0,0,0],
            "Moderate" : [0,0,0,0,0,0],
            "High" : [0,0,0,0,0,0],
        }}

        for i in result:
            k = tab3[i["UUID"]][i["OPTION_NAME"]]
            for i in range(len(k)):
                weights[i] += k[i]

        response = {}
        labels = ["Object storage","Block storage","File storage","Cool","Cold","Hybrid Storage"]

        for i in range(len(labels)):
            response[labels[i]] = weights[i]
            
        print(response)
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug = True)