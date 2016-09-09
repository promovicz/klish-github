
import main
import fancy

organization_props = [
    "name",
    "email",
    "blog",
    "location",
    "company",
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

organization_list_props = [
    "login",
    "name",
    "public_repos",
    "created_at",
    "updated_at",
]

def print_organization(organization):
    title = "Organization \"%s\"" % organization.login
    fancy.tabulate_object(organization, organization_props, title)
def print_organization_list(organizations):
    fancy.tabulate_objects(organizations, organization_list_props)

def show_organization(params):
    g = main.github()
    organization = g.get_organization(params['name'])
    print_organization(organization)

def show_organization_list(params):
    a = main.account()
    organization = a.get_orgs()
    print_organization_list(organization)
