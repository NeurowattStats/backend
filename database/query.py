from pymongo import collection

class QueryHelper:
    def __init__(self):
        pass

class MongoHelper(QueryHelper):
    def __init__(self):
        super().__init__()

    @staticmethod
    def find_the_latest(
        collection: collection.Collection,
        query: dict,
        projection: dict = None
    ):
        try:
            cursor = collection.find(query, projection).sort('_id', -1).limit(1)
            latest_doc = list(cursor)  # 將游標轉換為列表
            if latest_doc:
                return latest_doc[0]  # 返回第一個文檔
            return None  # 如果未找到文檔
        except Exception as e:
            print(f"Error finding the latest document: {e}")
            return None


class MilvusHelper(QueryHelper):
    """
    Milvus相關的取用...等函式
    """
    def __init__(self):
        super().__init__()
    
