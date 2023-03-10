from fastapi import APIRouter,  HTTPException, Request
from datetime import datetime
import logging

from currywurst_service.schemas.currywurst import currywurstPurchaseRequest, currywurstPurchaseResponse
from currywurst_service.service.currywurst_service import return_coins, is_price_met
from currywurst_service.service.event_service import publish_event
from currywurst_service.api.middleware import get_request_id


router = APIRouter()


@router.get("/currywurst/hello")
def introduce_yourself():
    return "Hello, I'm the currywurst machine"


@router.post("/currywurst/pay")
async def currywurst_pay(currywurstPurchaseRequest: currywurstPurchaseRequest, request: Request) -> currywurstPurchaseResponse:
    
    shoud_proceed = is_price_met(currywurstPurchaseRequest.eur_inserted, currywurstPurchaseRequest.currywurst_price)

    if not shoud_proceed:
        raise HTTPException(status_code = 400, detail =  "Need more money.")

    change = return_coins(currywurstPurchaseRequest.eur_inserted, currywurstPurchaseRequest.currywurst_price) 

    request_id = get_request_id()

    event = {
        "correlation_id": request_id,
        "timestamp": datetime.now().isoformat(),
        "transaction": {
            "currywurst_price": currywurstPurchaseRequest.currywurst_price,
            "eur_inserted": currywurstPurchaseRequest.eur_inserted,
            "change_given": change
        }
    }

    # await publish method
    await publish_event(request.app.state.mb, event, 'dataqueue')
    
    return change