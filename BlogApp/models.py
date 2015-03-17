from mongoengine import *



class User(DynamicDocument):
	name = StringField(max_length=50)


class BlogExtension(EmbeddedDocument):
	extra_field = StringField()
	some_other_field = StringField()


class Blog(DynamicDocument):
	owner = ReferenceField(User)
	result = IntField()


class Post(Document):
	author = ReferenceField(User)
	blog = ReferenceField(Blog)
	text = StringField()


class Comment(Document):
	owner = ReferenceField(User)
	post = ReferenceField(Post)
	text = StringField(max_length=140)
	isApproved = BooleanField(default=False)
