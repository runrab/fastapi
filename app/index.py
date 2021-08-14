import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()  # 必须实例化该类，启动的时候调用
class People(BaseModel):  # 必须继承
    name: str
    age: int
    address: str
    salary: float

# 请求根目录
@app.get('/')
def index():
    return {'message': '欢迎来到FastApi 服务！'}

# get请求带参数数据
@app.get('/items/{item_id}')
def items(item_id: int):
    return {'message': '欢迎来到接口页面'}



# post请求带参数数据
@app.post('/people')
def insert(people: People):
    age = people.age
    msg = f'名字：{people.name}，年龄：{age}'
    return {'success': True, 'msg': msg}
if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8080)
