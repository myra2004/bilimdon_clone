from starlette_admin.contrib.sqla import Admin

from app.models import User, Topic, Submission, Question, Participation, Option, Game
from app.db import engine
from app.admin.views import *
from app.admin.auth import JSONAuthProvider


"""ADMIN"""

admin = Admin(
    engine,
    title="Bilimdon Clone API",
    auth_provider=JSONAuthProvider(login_path="/login", logout_path="/logout"),
)

admin.add_view(UserView(User, icon='fa fa-user'))
admin.add_view(TopicView(Topic, icon='fa fa-topic'))
admin.add_view(QuestionView(Question, icon='fa fa-question'))
admin.add_view(OptionView(Option, icon='fa fa-notes'))
admin.add_view(GameView(Game, icon='fa fa-trophy'))
admin.add_view(ParticipationView(Participation, icon='fa fa-users'))
admin.add_view(SubmissionView(Submission, icon='fa fa-car'))


