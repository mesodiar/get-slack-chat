import requests


url = 'https://slack.com/api/conversations.history'
params = {
    'token': '<your_token>', # get it from https://api.slack.com/custom-integrations/legacy-tokens
    'channel': '<channel_id>', # use this repo to get those id https://github.com/zach-snell/slack-export 
    'inclusive': True
}

next_page = True
bool_next_cursor = True
next_cursor = ''
number = 1
while next_page == True:
 
    if bool_next_cursor: 
        params = {
            'token': '<your_token>', # get it from https://api.slack.com/custom-integrations/legacy-tokens
            'channel': '<channel_id>', 
            'cursor': next_cursor,
        }
    response = requests.get(url=url, params=params)
    response_json = response.json()
    print(response_json)

    next_cursor = response_json['response_metadata']['next_cursor']
    bool_next_cursor = response_json['has_more']

    number += 1
    f = open(f'response_{number}', "w")
    f.write(str(response.json()))
    f.close()



