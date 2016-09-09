
import main
import fancy

repository_props = [
    "description",
    "private",
    "created_at",
    "updated_at",
]

repository_list_props = [
    "full_name",
    "description",
]

def repository_extra(repo):
    extra = {
    }
    if repo.description:
        extra['description'] = repo.description[:40]
    return extra
def print_repository(params, repo):
    title = "Repository %s" % repo.full_name
    fancy.tabulate_object(repo, repository_props, title,
                          extra=repository_extra)
def print_repository_list(params, repos):
    fancy.tabulate_objects(repos, repository_list_props,
                           extra=repository_extra, params=params)

def set_repository(params):
    repo = main.repository(params, params['name'])
    if repo.organization:
        main.set_context(repo.organization)
    elif repo.owner:
        main.set_context(repo.owner)
    main.set_repository(repo)

def show_repository(params):
    if 'name' in params:
        repository = main.repository(params, params['name'])
    else:
        repository = main.repository(params)
    print_repository(params, repository)

def show_repository_list(params):
    c = main.context(params)
    typ = 'owner'
    if 'type' in params:
        typ = params['type']
    repos = c.get_repos(typ)
    print_repository_list(params, repos)
