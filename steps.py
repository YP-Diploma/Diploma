import configuration
import requests
import order_body

def get_order(steps):
    return requests.post(configuration.URL_ORDER + configuration.CREATE_ORDER,
                         json=order_body.order_body)

response_get_order = get_order(order_body)
#print(response_get_order.json())

def get_order_by_track():
    return requests.get(configuration.URL_ORDER + configuration.CREATE_ORDER,
                         params={"track":response_get_order.json()['track']})


response_get_order_by_track = get_order_by_track()
#print(response_get_order_by_track.json())