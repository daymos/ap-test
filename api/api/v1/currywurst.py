from fastapi import APIRouter

from api.schemas.curryWurst import currywurstPurchaseRequest, currywurstPurchaseResponse


router = APIRouter()

@router.get("/currywurst/hello")
def currywurstPay():
    return "Hello, I'm the currywurst machine"

@router.post("/currywurst/pay")
def currywurstPay(request: currywurstPurchaseRequest):
    print(request.currywurst_price)
    print(request.eur_inserted)
    return 'ok'