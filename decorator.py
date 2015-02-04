from functools import update_wrapper, wraps

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            session['Username']
        except:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorator
