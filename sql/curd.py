from sqlAlchemy.base_engine import BaseSession
from sqlAlchemy.models import User
#select,insert動作：現在はとりあえずsessionをmainに返して使用
class cli_sql(BaseSession):
    def __init__(self):
        super().__init__()

    def select(self):
        for i in self.session.query(User).order_by(User.id):
            print(i.name)

    def get_session(self):
        return self.session

"""
if __name__ == '__main__':
    cli = Users()
    cli.select()

    # レコード挿入
    session=cli.get_session()
    suzuki = User ( name="Suzuki", age=19 )
    session.add ( suzuki )  # insert処理
    session.commit ()  # commit
    session.close()
"""

