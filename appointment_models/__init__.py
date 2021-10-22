import datetime
from pydantic import BaseModel


class AppointmentModel(BaseModel):
    """
        Information that comes from user input to Schedule Appointments
    """

    user_id: int
    date_appointment: datetime.date
    start_time: datetime.time
    end_time: datetime.time

    class Config:
        title = 'Appointment Input Data'
