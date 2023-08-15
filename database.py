from sqlalchemy import create_engine, text, select

engine = create_engine("mysql+pymysql://root:root@localhost:3306/careers?charset=utf8mb4")

with engine.connect() as con:
    result = con.execute(text("select * from jobs"))
    print (result.all())