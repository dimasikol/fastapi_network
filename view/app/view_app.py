from fastapi import APIRouter

router_app = APIRouter(prefix='',tags=['main','body'])

@router_app.get('/')
async def test():
    context = {"list_app":['app','user','quiz']}
    return context
