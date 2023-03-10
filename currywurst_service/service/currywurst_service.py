from currywurst_service.schemas.currywurst import currywurstPurchaseResponse


def is_price_met(eur_inserted, currywurst_price):
   if eur_inserted < currywurst_price:
      return False
   return True


def return_coins(eur_inserted: int, currywurst_price: float) -> currywurstPurchaseResponse:
   change = {}
   partial = (eur_inserted - currywurst_price) * 100
   print('partial: ', partial)
   coins = [200, 100, 50, 20, 10, 5, 2, 1]

   for coin in coins:
      coin_count = partial // coin
      print('coin count: ', coin_count)
      change[coin] = coin_count 
      partial = partial % coin

   key_map = {
       200: 'two_euro_coins',
       100: 'one_euro_coins',
       50: 'fifty_cent_coins',
       20: 'twenty_cent_coin',
       10: 'ten_cent_coins',
       5: 'five_cent_coins',
       2: 'two_cent_coins',
       1: 'one_cent_coins' 
    }

   remapped_change: currywurstPurchaseResponse = { key_map[k]:change[k] for k in change }

   return remapped_change