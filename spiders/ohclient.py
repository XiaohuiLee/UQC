from otcbtc_client.client import OTCBTCClient

api_key = "KPDoOixz1hgzx9DDn4728A4Sg3oTXMUvVWkApWfx"
secret_key = "UAlDxhkbK38CH50vJHHQmFnyKHmGtrHJJnoPnZNO"
client = OTCBTCClient(api_key, secret_key)


# client.market.all()

# print(client.user.fetch())

# print(client.order.list_orders(market=None, state=None, limit=None, page=None, order_by=None))


print(client.trade.my_trades(market="ETH", limit=None, timestamp=None, from_=None, to=None, order_by=None)
)
