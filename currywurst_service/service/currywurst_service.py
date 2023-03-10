from currywurst_service.schemas.currywurst import currywurstPurchaseResponse


def is_price_met(eur_inserted, currywurst_price):
   if eur_inserted < currywurst_price:
      return False
   return True


def return_coins(eur_inserted: int, currywurst_price: float) -> currywurstPurchaseResponse:
   change = {}
   partial = (eur_inserted - currywurst_price) * 100
   coins = [200, 100, 50, 20, 10, 5, 2, 1]

   for coin in coins:
      coin_count = partial // coin
      change[coin] = coin_count 
      partial = partial % coin

   key_map = {
       200: 'two_euro',
       100: 'one_euro',
       50: 'fifty_cent',
       20: 'twenty_cent',
       10: 'ten_cent',
       5: 'five_cent',
       2: 'two_cent',
       1: 'one_cent' 
    }

   remapped_change: currywurstPurchaseResponse = { key_map[k]:change[k] for k in change }

   return remapped_change