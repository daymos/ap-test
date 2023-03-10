from typing import Union

from pydantic import BaseModel


class currywurstPurchaseRequest(BaseModel):
    currywurst_price: float
    eur_inserted: float


class currywurstPurchaseResponse(BaseModel):
    two_euro: int
    one_euro: int
    fifty_cent: int
    twenty_cent: int
    ten_cent: int
    five_cent: int
    two_cent: int
    one_cent: int