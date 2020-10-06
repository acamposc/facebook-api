import os

from facebook_business.api import FacebookAdsApi
from facebook_business import adobjects
from facebook_business.adobjects.user import User
from facebook_business.adobjects.adaccount import AdAccount

class FacebookAccess:
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
        my_accts = list(me.get_ad_accounts())
     
        def params(self):
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

                'time_increment': 'monthly',
                'sort': ['campaign_name_descending'],            
                'level': 'campaign'
            }
            return params
        
        #https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group
        #https://www.stitchdata.com/docs/integrations/saas/facebook-ads#campaigns
        def fields(self):
            fields = [
                'campaign_id',
                'campaign_name',
                'objective',
                'account_id',
                'updated_time'          
                
            ]
            return fields

        for acct in range(len(my_accts)):
            #print(my_accts[acct])
            #campaigns = my_accts[acct].get_campaigns()

               results = []
               for account_id, id in my_accts[acct].items():
                   if 'act_' in id:
                       results.append(id)
                       for result in range(len(results)):
                           insights = AdAccount(results[result]).get_insights(
                               params =  params(self),
                               fields = fields(self)
                           )
                           #for insight in insights:
                           #    print(insight['campaign_name'])

                           print(insights)
                           

                           
            
            
            #spend = my_accts[acct].api_get(fields=[
            #    adobjects.adaccount.AdAccount.Field.amount_spent,
            #    adobjects.adaccount.AdAccount.Field.name
            #    ])
            #print(campaigns)
            #print(spend)

            

if __name__ == "__main__":
    access = FacebookAccess()
    login = access.login()
    accts = access.accounts()
    
    
else:
    print('not in main ')