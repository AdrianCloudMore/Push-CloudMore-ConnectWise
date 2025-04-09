import connectwise.client
from connectwise.client import ConnectWiseClient
import configparser

def main():
    try:

        config = configparser.ConfigParser()
        config.read("settings.ini")

        print("Push Cloudmore -> ConnectWise Integration ")
        client = ConnectWiseClient(clientId=config['connectwise']["CLIENT_ID"],
                                   username=config['connectwise']['USERNAME'],
                                   password=config['connectwise']['PASSWORD'],
                                   company=config['connectwise']['COMPANY'],
                                   baseUrl=config['connectwise']['BASE_URL'])

        client.getListOfBillingSetups()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()