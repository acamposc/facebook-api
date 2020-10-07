import os
from fn import fn

'''
Params and fields 
'''         
def metrics():
    params = fn.Params()
    campaign_params = params.campaign_params()

    fields = fn.Fields()
    campaign_fields = fields.campaign_fields()

    return campaign_params, campaign_fields

#metrics = metrics() 

'''
Authentication and sign in  
'''
def authenticate():
    auth = fn.FacebookAuth()
    login = auth.login()
    accts = auth.accounts()
    return accts
    '''
    test
    
    if len(accts) > 0:
        acct_len = 'y'
    else: 
        acct_len = 'n'
    print('accts > 0: ', acct_len)
    
    test end
    '''
#authenticate = authenticate()
#print(authenticate)



'''
Campaign data 
'''                

def campaigns_get():
    campaigns = fn.Campaigns()
    campaign_data = campaigns.campaigns_list(
        campaign_params = metrics[0],
        campaign_fields = metrics[1],
        accounts = authenticate
    )
    return campaign_data

def tbl(campaign):
    for i in campaign:
        print(i['campaign_name'])
             
            
            

if __name__ == "__main__":
    metrics = metrics()
    authenticate = authenticate()
    campaign = campaigns_get()
    tbl(campaign)

    
else:
    print('not in main ')