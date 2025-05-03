from starlette_admin.contrib.sqla import ModelView


class UserView(ModelView):
    fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    export_fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    export_types = ['pdf', 'png', 'jpg', 'jpeg', 'webp', 'print']
    searchable_fields = ['email', 'first_name', 'last_name']


class TopicView(ModelView):
    fields = ["id", "name"]


class QuestionView(ModelView):
    fields = ['id', 'title', 'description', 'topic']


class OptionView(ModelView):
    fields = ["id", "question", "title", "is_correct"]


class GameView(ModelView):
    fields = ['id', 'title', 'start_time', 'end_time', 'topic', 'score']


class ParticipationView(ModelView):
    fields = ['id', 'user', 'game', 'start_time', 'end_time', 'gained_score']
    exclude_fields_from_create = ['start_time', 'end_time']


class SubmissionView(ModelView):
    fields = ["id", "owner", "game", "question", "option", "is_correct"]


