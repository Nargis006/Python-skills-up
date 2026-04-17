from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("❌ Access Denied!")
            return None
        else:
            return func(user_role)
        
    return wrapper
    
@require_admin
def access_tea_inventory(user_role):
    print("✅ You got access to the inventory!")

access_tea_inventory("admin")
access_tea_inventory("Customer")

            
