
from github.AuthenticatedUser import AuthenticatedUser
from github.NamedUser import NamedUser

import main
import fancy

user_props = [
    "login",
    "name",
    "email",
    "blog",
    "bio",
    "location",
    "company",
    "hireable",
    "public_gists",
    "private_gists",
    "public_repos",
    "owned_private_repos",
    "total_private_repos",
    "collaborators",
    "followers",
    "following",
    "disk_usage",
    "plan",
    "id",
    "created_at",
    "updated_at",
    "gravatar_id",
]

user_list_props = [
    "name",
    "email",
    "location",
    "public_gists",
    "private_gists",
    "created_at",
    "updated_at",
]

def print_user(user):
    if isinstance(user, AuthenticatedUser):
        title = "User %s (authenticated)" % user.login
    elif isinstance(user, NamedUser):
        title = "User %s" % user.login
    fancy.tabulate_object(user, user_props, title)
def print_user_list(users):
    fancy.tabulate_objects(users, user_list_props)

def show_user(params):
    g = main.github()
    if 'name' in params:
        user = g.get_user(params['name'])
    else:
        user = g.get_user()
    print_user(user)
