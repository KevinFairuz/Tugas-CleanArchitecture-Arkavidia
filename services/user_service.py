from repositories.user_repository import UserRepository

class UserService:
  @staticmethod
  def get_users():
    users = UserRepository.get_users()
    return [
      {
        "id": user.id,
        "name": user.name,
        "email": user.email
      }
    ]

  @staticmethod
  def create_user(data):
    new_user = User(name=data['name'], email=data['email'])
    UserRepository.add_user(new_user)
    return {
      "message": "User created successfully"
    }
