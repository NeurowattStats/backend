from fastapi import HTTPException

def handle_request(ticker, service_class, method_name, include_content=False):
    """Helper function to handle request and response generation."""
    try:
        responser = service_class(ticker)
        method = getattr(responser, method_name)
        data = method()
        
        if include_content:
            content_method_name = f"{method_name}_text"
            if hasattr(responser, content_method_name):
                content_method = getattr(responser, content_method_name)
                content = content_method()
                return {'data': data, 'content': content}
            else:
                raise AttributeError(f"No content method found for {method_name}")
        
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))