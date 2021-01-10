#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, g
from flask_restful import reqparse, Api, Resource
from flask_httpauth import HTTPTokenAuth
from basic_.flask_ import FResponse as fresp

# Flask 相关变量
app = Flask(__name__)
api = Api(app)

# 认证相关
auth = HTTPTokenAuth(scheme="token")
TOKENS = {
    "fejiasdfhu",
    "fejiuufjeh"
}


@auth.verify_token
def verify_token(token):
    if token in TOKENS:
        g.current_user = token
        return True
    return False


# 数据库相关变量声明

engine = create_engine("mysql+pymysql://{}:{}@192.168.122.110/backend".format("bkadmin", "admin@123"), encoding="utf8", echo=False)
BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)


# 构建数据模型User: object relation map
class User(BaseModel):
    __tablename__ = "Users"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8",
    }

    # 表结构
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50), nullable=False)
    age = Column("age", Integer, nullable=False)

    # 构建数据模型的json格式
    def get_json(self):
        return {"id": self.id, "name": self.name, "age": self.age}

# 初始化数据库
# init_db()

# 利用session对象连接数据库, 线程隔离
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)()


# RESTfulAPI的参数解析 -- put / post参数解析
def parput():
    parser_put = reqparse.RequestParser(trim=True)
    parser_put.add_argument("name", type=str, required=True, help="need name data")
    parser_put.add_argument("age", type=int, required=True, help="need age data")
    return parser_put


# RESTfulAPI的参数解析 -- get参数解析
def parget():
    parser_get = reqparse.RequestParser()
    parser_get.add_argument("limit", type=int, required=False)
    parser_get.add_argument("offset", type=int, required=False)
    parser_get.add_argument("sortby", type=str, required=False)
    return parser_get


# 操作（put / get / delete） 单一资源
class Todo(Resource):
    # 添加认证
    decorators = [auth.login_required]

    def put(self, user_id):
        """
        更新用户数据: curl http://127.0.0.1:5000/users/12 -X PUT -d "name=Allen&age=20" -H "Authorization: token fejiasdfhu"
        """
        args = parput().parse_args()
        user_ids_set = set([user.id for user in session.query(User.id)])

        if user_id not in user_ids_set:
            return None, 404

        user = session.query(User).filter(User.id == user_id)[0]
        user.name = args['name']
        user.age = args['age']
        # merge用来更新一个已有主键的记录而不是add
        session.merge(user)
        session.commit()

        # 更新成功， 返回201
        return fresp.statResponse(fresp.R201_CREATED)

    def get(self, user_id):
        """
        获取用户数据: curl http://127.0.0.1:5000/users/10 -X GET -H "Authorization: token fejiasdfhu"
        """
        users = session.query(User).filter(User.id == user_id)

        if users.count() == 0:
            return None, 404

        return fresp.dataResponse(fresp.R200_OK, users[0].get_json())

    def delete(self, user_id):
        """
        删除用户数据: curl http://127.0.0.1:5000/users/10 -X DELETE -H "Authorization: token fejiasdfhu"
        """
        session.query(User).filter(User.id == user_id).delete()
        session.commit()

        return fresp.statResponse(fresp.R204_NOCONTENT)


# 操作（post / get）资源列表
class TodoList(Resource):
    decorators = [auth.login_required]

    def get(self):
        """
        获取全部用户数据: curl http://127.0.0.1:5000/users -X GET -d "limit=10&offset=0&sortby=name" -H "Authorization: token fejiasdfhu"
        """
        args = parget().parse_args()
        users = session.query(User)

        if "sortby" in args:
            users = users.order_by(User.name if args["sortby"] == "name" else User.age)
        if "offset" in args:
            users = users.offset(args["offset"])
        if "limit" in args:
            users = users.limit(args["limit"])

        return fresp.dataResponse(fresp.R200_OK, [user.get_json() for user in users])

    def post(self):
        """
        添加一个新用户: curl http://127.0.0.1:5000/users -X POST -d "name=Brown&age=20" -H "Authorization: token fejiasdfhu"
        """
        args = parput().parse_args()
        user = User(name=args["name"], age=args["age"])
        session.add(user)
        session.commit()

        # 资源添加成功，返回201
        return fresp.dataResponse(fresp.R201_CREATED, user.get_json())


# 设置路由
api.add_resource(TodoList, "/users")
api.add_resource(Todo, "/users/<int:user_id>")

if __name__ == '__main__':
    app.run(debug=True)
