from rediscluster import RedisCluster
import os
from config import REDIS_NODE_1,REDIS_NODE_2,REDIS_NODE_3,REDIS_HOST
import traceback

redis_password = os.getenv("REDIS_PASSWORD")

# Cấu hình Redis Cluster
startup_nodes = [{"host":REDIS_HOST, "port": REDIS_NODE_1},
                 {"host":REDIS_HOST, "port": REDIS_NODE_2},
                 {"host":REDIS_HOST, "port": REDIS_NODE_3}]

def append_struct_to_array(key, data):
    try:
        # Khởi tạo kết nối đến Redis Cluster
        client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        client.rpush(key, data)

    except Exception as e:
        traceback.print_exc()
        return str(e)  # Trả về thông báo lỗi nếu có lỗi
