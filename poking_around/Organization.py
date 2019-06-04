class Organization:
    #instantiate our organnization with the necessary into
    def __init__(self, orgName, domainNames, details, notes, region, tags):
        self.orgName = orgName
        self.domainNames = domainNames
        self.details = details
        self.notes = notes
        self.region = region
        self.tags = tags
     
    #get organization name
    def getOrgName(self):
    
    #get the domain name(s) associated with this organizatoin
    def getDomainNames(self):
    
    #get the details associated with this organization
    def getDetails(self):
    
    #get the notes associated with this organization
    def getNotes(self):
        
    #get the region this organization is found in
    def getRegion(self):
    
    #get any and all tags
    def getTags(self):
     
    #turn this into a json entry
    def toJson(self):
     
    #return the json entry
    def getJson(self)
        
        
        