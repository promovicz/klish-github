
import main
import fancy

issue_props = [
    "repository",
    "number",
    "title",
    "state",
    "assignee",
    "user",
    "labels",
    "comments",
    "pull_request",
    "id",
    "created_at",
    "updated_at",
    "closed_at",
    "closed_by"
]

issue_list_props = [
    "number",
    "state",
    "assignee",
    "user",
    "title",
]

def issue_extra(issue):
    extra = {
        'title':      issue.title[:40],
        'labels':     ", ".join(map(lambda l: l.name, issue.labels)),
    }
    if issue.user:
        extra['user'] = issue.user.login
    if issue.closed_by:
        extra['closed_by'] = issue.closed_by.login
    if issue.repository:
        extra['repository'] = issue.repository.full_name
    return extra
def print_issue(params, issue):
    title = "Issue %s" % issue.number
    fancy.tabulate_object(issue, issue_props, title,
                          extra=issue_extra, params=params)
def print_issue_list(params, issues):
    fancy.tabulate_objects(issues, issue_list_props,
                           extra=issue_extra, params=params)

def show_issue(params):
    r = main.repository(params)
    issue = r.get_issue(int(params['number']))
    print_issue(params, issue)

def show_issue_list(params):
    r = main.repository(params)
    state = 'open'
    issues = r.get_issues(state=state)
    print_issue_list(params, issues)
