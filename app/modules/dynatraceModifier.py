import requests
import json

from app import app

class dynatraceModifier:
    
    payloadDict = {}
    outputDict = {}

    def __init__(self, payload):
 
        app.logger.debug("Request from Dynatrace: " + json.dumps(payload) )
        self.payloadDict = payload 
        
    

    #########################
    # transformTags
    #########################

    def __transformTags(self):
        
        outputTags = {}
        
        tmp = self.payloadDict['Tags']
        if str(tmp) != "":
            x = str(tmp).split(", ")
            if len(x)>0:
                for i in x:
                    y = i.split(":")
                    outputTags[y[0]] = y[1]
                    
        return outputTags


    #########################
    # Process
    #########################

    def process(self):
        
        self.outputDict['event_id'] = self.payloadDict['ProblemID']
        self.outputDict['tags'] = self.__transformTags()

        if self.payloadDict['State'] == 'OPEN':
            self.outputDict['status'] = 'trigger'
        elif self.payloadDict['State'] == 'CLOSED':
            self.outputDict['status'] = 'resolve'
        
        self.outputDict['message'] = self.payloadDict['ProblemTitle']
        self.outputDict['description'] = self.payloadDict['ProblemDetailsMarkdown']
        
        
        app.logger.debug("Output payload: " + json.dumps(self.outputDict))