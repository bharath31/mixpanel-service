import web
from mixpanel import Mixpanel
import json
import base64

urls = ('/.*', 'hooks')
app = web.application(urls, globals())

# Change this to your Mixpanel account token
mixpanel_token = '149c6eedb41e473f196e4b5dba9609c8'

def post_event(token, data):
    mixpanel = Mixpanel(token)
    distinct_id = data["custom_data"]["$mixpanel_distinct_id"]
    event_name = data["name"]
    if distinct_id is None:
        return 'Missing distinct_id'
    mixpanel.track(distinct_id, event_name, data)
    print('Sent')


class hooks:
    def POST(self):
        data = json.loads(web.data())
        print
        print('Data Received:')
        print(data)
        post_event(mixpanel_token, data)
        return 'Sending to Mixpanel'

if __name__ == '__main__':
    app.run()
