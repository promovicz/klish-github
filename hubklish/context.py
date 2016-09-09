
from github.AuthenticatedUser import AuthenticatedUser
from github.NamedUser import NamedUser
from github.Organization import Organization

import main
import user
import organization

def set_context_self(params):
    g = main.github()
    main.set_context(g.get_user())

def set_context_user(params):
    g = main.github()
    main.set_context(g.get_user(params['name']))

def set_context_organization(params):
    g = main.github()
    main.set_context(g.get_organization(params['name']))

def show_context(params):
    c = main.context()
    if isinstance(c, AuthenticatedUser):
        user.print_user(c)
    elif isinstance(c, NamedUser):
        user.print_user(c)
    elif isinstance(c, Organization):
        organization.print_organization(c)
