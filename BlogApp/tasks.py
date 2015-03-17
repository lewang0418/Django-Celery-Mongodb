from functools import wraps
from .celeryconf import app

from .models import User, Blog

# decorator to avoid code duplication

def update_job(fn):
	"""Decorator that will update Job with result of the function"""

	# wraps will make the name and docstring of fn available for introspection
	@wraps(fn)
	def wrapper(job_id, *args, **kwargs):
		user = User.objects.get(id=job_id)
		user.name = "lewang"
		result = fn(*args, **kwargs)
		blog = Blog.objects.create(owner=user, result=result)
		blog.save()
		user.save()
	return wrapper

@app.task
@update_job
def task(n):
	"""Return 2 to the n'th power"""
	return 2 ** n

