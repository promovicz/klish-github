
from os import getenv

from github import Github

auth_token = getenv("GITHUB_AUTH")

def startup():
    account()

the_github = None
the_account = None
the_context = None
the_repository = None

def github():
    global the_github
    if not the_github:
        the_github = Github(auth_token)
    return the_github

def account():
    global the_account
    if not the_account:
        the_account = github().get_user()
    return the_account

def context(params={}):
    if 'user' in params:
        return github().get_user(params['user'])
    elif 'organization' in params:
        return github().get_organization(params['organization'])
    elif 'repository' in params:
        repository = params['repository']
        organization = repository.split('/')[0]
        return github().get_organization(organization)
    else:
        global the_context
        if not the_context:
            return account()
        return the_context

def set_context(context):
    global the_context
    the_context = context

def repository(params={}, name=None):
    if not name:
        if 'repository' in params:
            name = params['repository']
    if name:
        if name.find('/') == -1:
            c = context(params)
            full = "%s/%s" % (c.login, name)
        else:
            full = name
        return github().get_repo(full)
    else:
        global the_repository
        if not the_repository:
            raise ValueError, "No repository specified"
        return the_repository

def set_repository(repository):
    global the_repository
    the_repository = repository
