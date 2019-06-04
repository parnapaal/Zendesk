import pandas as pd

class csvParser:
    organizationHeaders = []
    userHeaders = []
    ticketHeaders = []
    
    jsonOrganizationHeaders = []
    jsonUserHeaders = []
    jsonTicketHeaders = []
    
#this is where the organization rows broken into chunks of 100 will live
    def __init__(self, fileToParse, kindOfFile):
        self.name = fileToParse
        self.csvType = kindOfFile
        self.arr = []
        openFile()
        

    # open up our file        
    def openFile(self):


        #convert the file to a large pandas df -- use the .ipynb from exploration -- if a header name is given, certain cleaning methods will be applied based off the neads of that column of information
    def convertToPandasFramework(self)
    
    #based off of 'csvType', route our file through the correct type of parsing by sending in the correct header titles we need
    def routeToCorrectTableType(self)


    #sanitize the data in each colum of unecessary characters
    def cleanData(self)


    #create an array of organization features from each row of the dataframe
    def importOrgs(self)
    
    #create an array of user features from each row of the dataframe
    def importUsers(self)
    
    #create an array of ticket features from each row of the dataframe
    def importTickets(self)


    #create arrays of length <= 100 
    def divideDataFrameIntoPieces(self)


    #populate one array with 100 rows from the dataframr
    def populateOneArrayPiece(self)
