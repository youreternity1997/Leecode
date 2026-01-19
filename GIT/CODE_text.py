def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_authenticated'):
            print("未授權訪問")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def view_profile(user):
    print(f"歡迎 {user['name']}")

view_profile({'name': 'Alice', 'is_authenticated': True})  # Should print welcome message