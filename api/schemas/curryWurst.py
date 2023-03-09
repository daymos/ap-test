from typing import Union

from pydantic import BaseModel


class currywurstPurchaseRequest(BaseModel):
    currywurst_price: float
    eur_inserted: float


class currywurstPurchaseResponse(BaseModel):
    two_euro_coins: int
    one_euro_coins: int
    fifty_cent_coins: int
    twenty_cent_coins: int
    ten_cent_coins: int
    five_cent_coins: int
    two_cent_coins: int
    one_cent_coins: int