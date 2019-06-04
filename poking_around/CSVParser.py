import pandas as pd

class CSVParser:
    
#this is where the organization rows broken into chunks of 100 will live
    def __init__(self, fileToParse):
        
        
        

    # open up our file        
    def openFile(self):


        #convert the file to a large pandas df -- use the .ipynb from exploration -- if a header name is given, certain cleaning methods will be applied based off the neads of that column of information
    def convertToPandasFramework(self):
    
    #tickets needs the asignee groupId and the requesterOrgId and users need the organization name 
    #for a later callback to organzations to get the "true" orgID
    def combinePandasFrameworks(self):
    
    #based off of 'csvType', route our file through the correct type of parsing by sending in the correct header titles we need
    def routeToCorrectCreationType(self)


    #sanitize the data in each colum of unecessary characters
    def cleanData(self):
        
    def removeIdenticalData(self, ourKey): 
  
    
    def replaceAColumn(self, columnToReplace, columnToAdd)
    
    def addAColumn(self, columnToAdd):

    #create arrays of length <= 100 
    def divideDataFrameIntoPieces(self)


    #populate one array with 100 rows from the dataframr
    def populateOneArrayPiece(self)
