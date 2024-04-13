def debug_log(message, is_silent=False):
    print(f"DEBUG LOG: {message.upper() if is_silent == False else message.lower()}")

def debug_error(message, raise_error=False):
    if raise_error:
        raise Exception(f"DEBUG ERROR: {message.upper()}")
    
    print(f"DEBUG ERROR: {message.upper()}")