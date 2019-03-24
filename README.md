# mixpanel-service
A service to receive data via webhooks and forward the same to Mixpanel

The service is live [here](https://fathomless-earth-33560.herokuapp.com/)

## Sending a sample request 
### Step 1
Change the mixpanel_token on [webhook_receiver.py](https://github.com/bharath31/mixpanel-service/blob/f5a2cc3b121b0183532a4e81990d0fa8d50f2d4b/webhook_receiver.py#L10)

### Step 2 
Run ```python webhook_receiver.py```

### Step 3
Make a sample request 

#### URL: http://0.0.0.0:8080/
#### HTTP Method: POST
#### Request Payload:
````
{"origin": "BRANCH", "last_attributed_touch_type": "CLICK", "persona_identifiers": [], "content_items": [], "name": "OPEN", "existing_user": "false", "deep_linked": "false", "custom_data":{"$mixpanel_distinct_id":"hhyu6737622df0lnnfr611i8v9a78|2nnfr611i8v9a78"}, "user_data": {"past_cross_platform_ids": [], "ip": "2405:204:93fb:954c:797c:ea7b", "geo_continent_code": "AS", "limit_ad_tracking": "false", "environment": "FULL_APP", "os_version": "27", "prob_cross_platform_ids": [], "geo_lat": 20.0, "geo_city_code": "null", "platform": "ANDROID_APP", "sdk_version": "2.19.3", "app_version": "5.2.10", "brand": "vivo", "http_referrer": "", "geo_country_code": "IN", "geo_lon": 77.0, "language": "EN", "aaid": "99c5b45c-40ab-1e63c24a4853", "is_jailbroken": "null", "user_agent": "Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1804 Build/OPM1.171019.011)", "geo_dma_code": "null", "model": "vivo 1804", "os": "ANDROID"}, "attributed": "false", "last_attributed_touch_timestamp": 1552727001000, "last_attributed_touch_data": {"~ad_set_name": "Open", "~channel": "Facebook", "~campaign_id": "8837029837y73", "~ad_name": "sampleadname", "~ad_objective_name": "APP_INSTALLS", "~feature": "paid advertising", "~secondary_publisher": "facebook", "$3p": "a_facebook", "+via_features": ["ADS"], "~campaign": "appinstall", "~ad_set_id": "23843086537400691", "~creative_name": "68y32hbjhbhj", "+click_timestamp": 1552727001, "~creative_id": "o72y378y2762332", "~ad_id": "8837029837y73", "~advertising_partner_name": "Facebook"}, "first_event_for_user": "false", "install_activity": {"event_name": "INSTALL", "timestamp": 1552727083000, "touch_data": {"tilde_advertising_partner_name": "Facebook"}}, "timestamp": 1552727083843, "id": "635390319521351354"}
````

### Step 4
View the data on [Mixpanel Liveview](https://mixpanel.com/report/1939137/live)

## Deploy this app to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
