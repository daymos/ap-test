from currywurst_service.schemas.currywurst import currywurstPurchaseResponse


def return_coins(eur_inserted: int, currywurst_price: float) -> currywurstPurchaseResponse:
   global md
   change: currywurstPurchaseResponse = {
       'two_euro_coins': 0,
       'one_euro_coins': 0,
       'fifty_cent_coins': 0,
       'twenty_cent_coins': 0,
       'ten_cent_coins': 0,
       'five_cent_coins': 0,
       'two_cent_coins': 0,
       'one_cent_coins': 0,
    }

   return change