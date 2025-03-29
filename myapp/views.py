from django.http import JsonResponse
from database.automap import engine, User, Address, Task
from sqlalchemy.orm import Session

def user_list(request):
    with Session(engine) as session:
        users = session.query(User).all()
        data = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "tasks": [
                    {"title": task.title, "description": task.description}
                    for task in user.tasks
                ],
                "address":  {
                        "street": user.address.street,
                        "city": user.address.city,
                        "country": user.address.country
                    }
            }
            for user in users
        ]
        return JsonResponse(data, safe=False)

def address_list(request):
    with Session(engine) as session:
        addresses = session.query(Address).all()
        data = [
            {"id": addr.id, "street": addr.street, "city": addr.city, "country": addr.country}
            for addr in addresses
        ]
        return JsonResponse(data, safe=False)
