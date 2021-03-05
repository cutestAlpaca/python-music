from redis import StrictRedis


class ObjRedis:
    redis = StrictRedis(host='localhost', port=6379, db=0, password='anjie7410')

    def getObj(self):
        return self.redis;


