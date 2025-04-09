import requests
from requests.auth import HTTPBasicAuth

class ConnectWiseClient:

    clientId: str
    username: str
    password: str
    company: str
    basicAuth: HTTPBasicAuth
    baseUrl: str

    def __init__(self,**kwargs):
        self.clientId = kwargs.get("clientId")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.company = kwargs.get("company")
        self.baseUrl = kwargs.get("baseUrl")
        self.basicAuth = HTTPBasicAuth(self.username,self.password)


    def getBasicAuth(self):
        if self.basicAuth is None:
            self.basicAuth = HTTPBasicAuth(self.username,self.password)
        return self.basicAuth

    def getHeaders(self):
        return {'clientId': self.clientId}

    def getListOfBillingSetups(self):

        url = "%s/%s" % (self.baseUrl, "company/companies")
        response = requests.request("GET", url, headers=self.getHeaders(),auth=self.getBasicAuth())
        print(response.request.headers)
        print(response.text)