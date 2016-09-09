
from github.Organization import Organization

import main
import fancy

gist_props = [
    "description",
    "comments",
    "file_count",
    "file_names",
    "fork_of",
    "fork_count",
    "fork_ids",
    "public",
    "created_at",
    "updated_at",
]

gist_list_props = [
    "id",
    "description",
    "updated_at",
]

def gist_extra(gist):
    extra = {
        'file_count': len(gist.files),
        'file_names': ",".join(gist.files.keys()),
        'fork_count': len(gist.forks),
        'fork_ids':   ",".join(map(lambda f: f.id, gist.forks)),
    }
    if gist.fork_of:
        extra['fork_of'] = gist.fork_of.id
    return extra
def print_gist(gist):
    title = "Gist %s" % gist.id
    fancy.tabulate_object(gist, gist_props, title, extra=gist_extra)
def print_gist_list(gists):
    fancy.tabulate_objects(gists, gist_list_props, extra=gist_extra)

def show_gist(params):
    g = main.github()
    gist = g.get_gist(params['id'])
    print_gist(gist)

def show_gist_list(params):
    c = main.context(params)
    if isinstance(c, Organization):
        # XXX library does not support get_gists for organizations
        c = main.github().get_user(c.login)
    gists = c.get_gists()
    print_gist_list(gists)
