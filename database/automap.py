from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, relationship

# 创建引擎
engine = create_engine("sqlite:///database/db.sqlite3", echo=True)

# 反射现有的数据库到新的模型
metadata = MetaData()
metadata.reflect(engine)
AutomapBase = automap_base(metadata=metadata)
AutomapBase.prepare()

# 映射的类现在默认情况下已创建，名称与表名匹配
User = AutomapBase.classes.user
Address = AutomapBase.classes.address
Task = AutomapBase.classes.task

# 手动为 User 类添加 tasks 关系属性
User.tasks = relationship("task", back_populates="user", primaryjoin=User.id == Task.user_id)
User.address = relationship("address", primaryjoin=User.address_id == Address.id)

# 手动为 Task 类添加 user 关系属性
Task.user = relationship("user", back_populates="tasks", primaryjoin=Task.user_id == User.id)
# Address.user = relationship(
#     "user",
#     primaryjoin="Address.user_id == User.id",
#     back_populates="addresses"
# )
# # 为 User 类添加 tasks 关系属性
# User.tasks = relationship("task", back_populates="user", foreign_keys=Task.user_id)

# # 为 Task 类添加 user 关系属性
# Task.user = relationship("user", back_populates="tasks", foreign_keys=Task.user_id)
