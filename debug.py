def debug_log(message, is_silent=False):
    print(f"DEBUG LOG: {message.upper() if is_silent == False else message.lower()}")

def debug_error(message):
    print(f"DEBUG ERROR: {message.upper()}")