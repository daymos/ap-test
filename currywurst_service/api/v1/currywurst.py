from fastapi import APIRouter

from currywurst_service.schemas.currywurst import currywurstPurchaseRequest, currywurstPurchaseResponse
from currywurst_service.service.currywurst_service import return_coins


router = APIRouter()


@router.get("/currywurst/hello")
def introduce_yourself():
    return "Hello, I'm the currywurst machine"


@router.post("/currywurst/pay")
async def currywurst_pay(request: currywurstPurchaseRequest):
    print(request)
    change = return_coins(request.currywurst_price, request.eur_inserted)

    # await publish method
    
    return change