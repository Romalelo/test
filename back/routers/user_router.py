from datetime import datetime

from fastapi import APIRouter, HTTPException, Response

from routers.schemas import User, UserList, UpdateUserSchema

users = [
    User(id=1, username='romale', first_name='Roman', last_name='Lerner', age=20, created_at=datetime.now()),
    User(id=2, username='onefad', first_name='Nika', last_name='Molotkova', age=20, created_at=datetime.now()),
    User(id=3, username='quakumei', first_name='Ilya', last_name='Tampio', age=20, created_at=datetime.now()),
]

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/', name='All users', response_model=UserList)
def get_all_users():
    return UserList(count=len(users), users=users)


@user_router.post('/add', name='Add user', response_model=User)
def add_user(user: User):
    users.append(user)
    return user


@user_router.get('/{user_id}', name='Get user', response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')


@user_router.delete('/{user_id}', name='Delete user', response_class=Response)
def delete_user(user_id: int):
    for i, user in enumerate(tuple(users)):
        if user.id == user_id:
            del users[i]
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail='User not found')


@user_router.put('/{user_id}', name='NOT WORKING', description='NOT WORKING', response_model=User)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    for i in range(len(users)):
        if users[i].id == user_id:
            data = new_user_data.dict()
            for key in data:
                if data[key] is not None:
                    setattr(users[i], key, data[key])
            return users[i]
    raise HTTPException(status_code=404, detail='User not found')
