# Create your views here.


from project.settings import REDMINE_HOST, REDMINE_USER, REDMINE_PASS


red_login = Redmine(REDMINE_HOST, username=REDMINE_USER, password=REDMINE_PASS)