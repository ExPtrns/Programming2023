# import json
#
#
# class User:
#     def __init__(self, name: str, user_id: str, user_level: str):
#         self.name = name
#         self.user_id = user_id
#         self.user_level = user_level
#
#
#
# def load_json(filename):
#     with open(filename, 'r', encoding='utf-8') as f_read:
#         data = json.load(f_read)
#     users = set()
#     for level, users_dict in data.items():
#         for id, name in users_dict.items():
#             users.add(User(name, id, level))
#     return users
#
#
# if __name__ == '__main__':
#     file = 'users.json'
#     users = load_json(file)
#     for user in users:
#         print(user.name, user.user_id, user.user_level)

