
from pprint import pprint, pformat
from tabulate import tabulate

from github.AuthenticatedUser import AuthenticatedUser
from github.Issue import Issue
from github.NamedUser import NamedUser
from github.Organization import Organization
from github.Gist import Gist
from github.Plan import Plan
from github.Repository import Repository

tablefmt_object  = "psql"
tablefmt_objects = "psql"

names = {
    AuthenticatedUser: 'login',
    NamedUser: 'login',
    Organization: 'login',
    Gist: 'id',
    Issue: 'number',
    Repository: 'full_name',
}

def format_plan(plan):
    bits = []
    if plan.collaborators:
        bits.append("%d users" % plan.collaborators)
    if plan.private_repos:
        bits.append("%d repos" % plan.private_repos)
    if plan.space:
        bits.append("%d space" % plan.space)
    return "%s: %s" % (plan.name, ", ".join(bits))

formatters = {
    Plan: format_plan,
}

def format_object(obj):
    cls = type(obj)
    if cls in formatters:
        print("Using formatter for %s" % cls)
        return formatters[cls](obj)
    elif cls in names:
        attr = names[cls]
        print("Using name %s for %s" % (attr, cls))
        return "<%s %s>" % (cls.__name__, getattr(obj, attr))
    else:
        return format(obj)

def tabulate_object(obj, props, title=None, extra=None):
    head = ["Property", "Value"]
    data = []
    extras = {}
    if extra:
        extras = extra(obj)
    for prop in props:
        if prop in extras:
            value = extras[prop]
        else:
            value = getattr(obj, prop)
        if value:
            data.append([prop, format_object(value)])
    if title:
        print("\n%s\n" % title)
    print(tabulate(data, headers=head, tablefmt=tablefmt_object))
    if title:
        print("")

def tabulate_objects(container, props, title=None, extra=None, all=False, page=1, limit=20, params=None):
    # adopt options from params
    if 'all' in params and params['all'] == 'all':
        all = True
    if 'page' in params:
        page = int(params['page'])
    if 'limit' in params:
        limit = int(params['page'])
    # determine total count
    count = container.totalCount
    # select objects
    if all:
        start = 0
        end = count
        objs = container
        print("Selected all objects...")
    else:
        start = (page - 1) * limit
        end = start + limit
        objs = container[start:end]
        print("Selected objects %d - %d..." % (start, end))
    # accumulate table headers
    head = []
    for prop in props:
        head.append(prop)
    # accumulate table data
    data = []
    # up-marks if not at start
    if start != 0:
        data.append(['...'] + ([''] * (len(props) - 1)))
    # format objects
    for obj in objs:
        line = []
        for prop in props:
            extras = {}
            if extra:
                extras = extra(obj)
            if prop in extras:
                value = extras[prop]
            else:
                value = getattr(obj, prop)
            if value:
                line.append(format_object(value))
            else:
                line.append("")
        data.append(line)
    # down-marks if not until end
    if not all: # XXX not really correct
        data.append(['...'] + ([''] * (len(props) - 1)))
    # print the header
    if title:
        print("\n%s\n" % title)
    # print the table
    print(tabulate(data, headers=head, tablefmt=tablefmt_objects))
    # print the footer
    if title:
        print("")
