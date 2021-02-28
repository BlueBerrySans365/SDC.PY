import requests
import json
import time

## Ты как в код пробрался, шизоид?!
##                                              
##               (*.            ,#            
##             (        %%*         ,         
##            (     %%%%%.                    
##           /       (%%#%%%#       .         
##         ,/,        ,(            /         
##        (           #    .#       *         
##       /%&(                  (.  (          
##      #  *#,.#    *,  /        .,.          
##     *   *,# #   #  /%&,/     /(#           
##    .       ..   (            /#.           
##   ,*    . *      (           /             
##  .,   ,            /      .  /             
##      *              *.     , ,             
##  ,      ,,********, ,       *              
##   .  .             .     ,                 
##     /.                 .(                  
##       *(      ,#*.    *                    


"""
BSDPY - This is an attempt to recreate the module to work with the server-discord.com API  \n
More features and functions will be added soon! \n

"""

class BDS:
    """
    bots.server-discord.com (or BSD) API commands. Update information about servers and shards. 
    """
    # def __init__(self):
    #     """
    #     Кто в здравом уме будет чекать инфу данной команды?!
    #     """
    #     return 
    def UpdateInfo(self, BDSID, serversC: int, shardsC: int, BDSToken, Debug: bool):
        """
        Update info - Updating servers and shards
        """
        BDSData = {
                'servers': serversC,
                'shards': shardsC
        }
        if Debug == True:
            BDSJson = {
                "url": f'https://api.server-discord.com/v2/bots/{BDSID}/stats',
                "headers": {
                    'Content-Type': 'application/json',
                    'Authorization': f'SDC {BDSToken}'
                },
                "data": f"{json.dumps(BDSData)}"
            }
            print(f"Check data what will be sended!\n{json.dumps(BDSJson)}\n# If you want to disable this message set Debug=False")
            time.sleep(6)
            BDSApi = requests.post(
                url=f'https://api.server-discord.com/v2/bots/{BDSID}/stats',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'SDC {BDSToken}'
                    },
                data=json.dumps(BDSData)
            )
            print(f"Status: {BDSApi}")
            # print(f"JSON DATA: {BDSApi.json()}")
        else:
            BDSApi = requests.post(
                url=f'https://api.server-discord.com/v2/bots/{BDSID}/stats',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'SDC {BDSToken}'
                    },
                data=json.dumps(BDSData)
            )
        return BDSApi

        # return "SPAGETTI"

class SD:
    """
    server-discord.com (or SD) API commands. Get information about user or servers. 
    """
    def getGuild(self, DSID, BDSToken):
        """
        getGuild - Get all guild information
        Returns JSON data
        """
        DSApi = requests.get(
            url=f"https://api.server-discord.com/v2/guild/{DSID}",
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'SDC {BDSToken}'
            }
        )
        return DSApi.json()
    def getPlace(self, DSID, BDSToken):
        """
        getGuild - Get guild place in list
        Returns JSON data
        """
        DSApi = requests.get(
            url=f"https://api.server-discord.com/v2/guild/{DSID}/place",
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'SDC {BDSToken}'
            }
        )
        return DSApi.json()
    def getRated(self, DSID, BDSToken):
        """
        getRated - Get guild rated list
        Returns JSON data
        """
        DSApi = requests.get(
            url=f"https://api.server-discord.com/v2/guild/{DSID}/rated",
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'SDC {BDSToken}'
            }
        )
        return DSApi.json()