# from datetime import time, datetime
# from typing import Optional
#
# from pydantic import BaseModel
#
#
# class ParticipationSchema(BaseModel):
#     id: int
#     start_time: time
#     end_time: Optional[time] = None
#     gained_score: int
#     registered_at: datetime
#
# dummy_data = {
#     'id': 1,
#     'start_time': time(hour=0, minute=0, second=0, microsecond=0),
#     'end_time': time(),
#     'gained_score': 0,
#     'registered_at': time()
# }
#
# participation = ParticipationSchema(**dummy_data)
# participation_dict = participation.model_dump()
# participation_dict['is_user'] = True
# print(participation.model_dump())