import os

from facebook_business.api import FacebookAdsApi
from facebook_business import adobjects
from facebook_business.adobjects.user import User
from facebook_business.adobjects.adaccount import AdAccount

'''
https://www.stitchdata.com/docs/integrations/saas/facebook-ads#campaigns
https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group

'''

'''
params are defined here:
'''
class Params():
    '''
    campaing params:
    '''
    def campaign_params(self):
        params = {
            'filtering': [
                {
                    'field': 'spend',
                    'operator': 'GREATER_THAN',
                    'value': '5'
                    }
                ],
                #'breakdowns': [
                #    'publisher_platform',
                #    'platform_position',
                #    'device_platform',  
                #],

                'time_increment': 1,
                'date_preset': 'last_3d',
                'sort': ['campaign_name_descending'],            
                'level': 'campaign'
            }
        return params

        '''
        ad_set params:
        '''

        '''
        ad_insights params:
        '''

'''
fields are defined here:
'''
class Fields():
    '''
    campaing fields:
    '''
    def campaign_fields(self):
            fields = [
                'campaign_id',
                'campaign_name',
                'objective',
                'account_id',
                'updated_time'
                ]
            return fields
    '''
    ad_set fields:
    '''
    
    '''
    ad_insights fields:
    '''


'''
Facebook authentication
'''
class FacebookAuth():
    def __init__(self):
        self.app_id = os.environ['FACEBOOK_APP_ID']
        self.app_secret = os.environ['FACEBOOK_APP_SECRET']
        self.app_token = os.environ['FACEBOOK_APP_TOKEN']

    def __call__(self):
        app_id = self.app_id
        app_secret = self.app_secret
        app_token = self.app_token
        return (app_id, app_secret, app_token)

    def login(self):
        self.creds = FacebookAdsApi.init(
            self.app_id,
            self.app_secret,
            self.app_token
        )
        
    def accounts(self):
        me = User(fbid = 'me')
        accts = list(me.get_ad_accounts())
        return accts


'''
campaign data request:
'''
class Campaigns():
    def campaigns_list(
        self,
        campaign_params,
        campaign_fields,
        accounts
    ):
        '''
        test
        
        print('params: ', campaign_params)
        print('fields: ', campaign_fields)
        print('accounts: ', len(accounts))
        
        test end
        '''
        ins = []
        for account in range(len(accounts)):
            results = []
            for account_id, id in accounts[account].items():
                if 'act_' in id:
                    results.append(id)
                    for result in range(len(results)):
                        insights = AdAccount(results[result]).get_insights(
                            params = campaign_params,
                            fields = campaign_fields 
                        )
            ins.append(insights)
        return(ins)

        #return insights

class Id():  
    def id(self, data):
        for dx in data:
            for d in dx:
                dy = dict(d)
                print('campaign_id:', dy['campaign_id'])
                print('campaign_name:', dy['campaign_name'])
                print('account_id: ', dy['account_id'])
                print('objective: ', dy['objective'])
        
     
        '''
        ax = []
        for i in range(len(data)):
            ax.append(data[i])       
        return ax    
        '''