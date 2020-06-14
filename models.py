from werkzeug import generate_password_hash, check_password_hash
class Permission:
	role_user=10
	role_foruadmin=20
	role_admin=30
class User:
	def __init__(self, name, email, password, role=Permission.role_user):
		self.name=name
		self.password_hash=self.save_password(password)
		self.email=email
		self.role=role
	def save_password(self, password):
		return generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	@property
	def is_admin(self):
		return self.role==Permission.role_admin
	def change_role(self, role):
		self.role=role
def main():
	user1=User('James','james@qq.com','12356')
	user2=User('admin','admin@qq.com','12345')
	for user in (user1, user2):
		if user.is_admin:
			print('{} is admin'.format(user.name))
		else:
			print('{} is not admin'.format(user.name))
		user.change_role(Permission.role_admin)
		print('after changed, {} is the admin'.format(user.name))
if __name__=='__main__':
	main()

