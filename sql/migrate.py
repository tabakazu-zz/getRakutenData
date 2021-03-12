from base_engine import BaseEngine
from models import User,Base
#databaseを作成する場合,class migrationを呼び出し
class Migration(object):
    def __init__(self):
        self.e = BaseEngine().engine

    def users(self):
        Base.metadata.create_all(self.e)

if __name__ == '__main__':
    Migration().users()
