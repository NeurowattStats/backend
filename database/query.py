from pymongo import collection

class QueryHelper:
    def __init__(self):
        pass

class MongoHelper(QueryHelper):
    def __init__(self):
        super().__init__()

    @staticmethod
    def find_the_lastest(
            collection: collection.Collection, 
            query: dict, 
            projection: dict = None
        ):
        # 如果有指定 projection, 使用 projection，否則不指定
        if projection:
            latest_doc = collection.find(query, projection).sort('_id', -1).limit(1)
        else:
            latest_doc = collection.find(query).sort('_id', -1).limit(1)
        
        # 使用 next() 之前檢查是否有結果返回
        latest_doc = latest_doc.try_next()

        if latest_doc:
            return latest_doc
        else:
            return None  # 或者根據需求處理找不到資料的情況
