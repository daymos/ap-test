from fastapi import APIRouter,  HTTPException

from currywurst_service.schemas.currywurst import currywurstPurchaseRequest, currywurstPurchaseResponse
from currywurst_service.service.currywurst_service import return_coins, is_price_met


router = APIRouter()


@router.get("/currywurst/hello")
def introduce_yourself():
    return "Hello, I'm the currywurst machine"


@router.post("/currywurst/pay")
async def currywurst_pay(request: currywurstPurchaseRequest):
    shoud_proceed = is_price_met(request.eur_inserted, request.currywurst_price)

    if not shoud_proceed:
        raise HTTPException(status_code = 400, detail =  "Need more money.")

    change = return_coins(request.eur_inserted, request.currywurst_price) 

    # await publish method
    
    return change