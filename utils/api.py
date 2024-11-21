from fastapi import HTTPException

def handle_request(
        ticker, 
        service_class, 
        method_name, 
        include_content=False, 
        content_method_name=None  # 新增參數 content_method_name，默認為 None
    ):
    """Helper function to handle request and response generation."""
    try:
        responser = service_class(ticker)
        method = getattr(responser, method_name)
        data = method()
        
        # 如果 include_content 為 True 且 content_method_name 被提供
        if include_content:
            # 如果沒有指定 content_method_name，則根據 method_name 默認推導
            if content_method_name is None:
                content_method_name = f"{method_name}_text"

            if hasattr(responser, content_method_name):
                content_method = getattr(responser, content_method_name)
                content = content_method()
                return {'content': content, 'array': data}
            else:
                raise AttributeError(f"No content method found for {content_method_name}")
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))