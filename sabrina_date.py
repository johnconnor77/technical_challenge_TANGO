#!/usr/bin/env python
from appointment_models import AppointmentModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import utils.redis_object as red
from utils.redis_functions import redis_save, redis_load
from utils.extra_functions import delta_time, check_time
import uvicorn
import logging
import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app = FastAPI(title="Sabrina Date API",
              description="Here's our API to handle appointment scheduling", version="1.0")


@app.on_event('startup')
async def connect_redis():
    red.redis = red.redis_connection()


@app.on_event('shutdown')
async def disconnect_redis():
    red.redis.close()


@app.post("/api/schedule/", summary="Creates an Appointment for certain User",
          description="Endpoint that takes a date/time and user ID (both required). Creates an "
                      "appointment beginning at that time for that user or returns an appropriate status"
                      "code and error if the appointment cannot be made (the user already has an"
                      "appointment that day")
async def schedule(appointment_to_schedule: AppointmentModel):
    """
        Endpoint that creates an Appointment for certain user id
        :param appointment_to_schedule: Class that represent the correct structure for Appointment Scheduling
        :return: Output for appointment created otherwise the error with details
    """
    print(appointment_to_schedule)
    key = appointment_to_schedule.user_id
    date_appointment = appointment_to_schedule.date_appointment.isoformat()
    start_time = appointment_to_schedule.start_time
    end_time = appointment_to_schedule.end_time

    time_elapsed = delta_time(end_time, start_time)

    if not check_time(start_time):
        raise HTTPException(status_code=400, detail="Start Time for Appointment is not allowed, check format")

    if not check_time(end_time):
        raise HTTPException(status_code=400, detail="End Time for Appointment is not allowed, check format ")

    if time_elapsed != datetime.timedelta(minutes=30):
        raise HTTPException(status_code=400, detail="Time Span for Appointment is not allowed")

    if not redis_load(key):
        value = [{'date_appointment': date_appointment,
                  'start_time': start_time.isoformat(),
                  'end_time': end_time.isoformat()}]

        redis_save(key, value)
    else:
        add_appointment = {'date_appointment': date_appointment,
                           'start_time': start_time.isoformat(),
                           'end_time': end_time.isoformat()}

        user_appointments = redis_load(key)

        for elem in user_appointments:
            check_existing_date = elem.get('date_appointment')
            if check_existing_date == date_appointment:
                raise HTTPException(status_code=409, detail="Date appointment was already setted")

        user_appointments.append(add_appointment)
        value = user_appointments
        redis_save(key, value)

    return JSONResponse({ f'Appointment  setted for user {key}': add_appointment})


@app.get("/api/appointments/", summary="List Appointments for certain User",
         description="Endpoint that takes a user ID (required) and returns all appointments for the user")
async def appointments_list(user_id: int):
    """
        Endpoint that retrieves a list of Appointments for certain user id
        :param user_id: query param for consulting given that user id the appointments related
        :return: list of appointments otherwise the error
    """

    user_appointments = redis_load(user_id)

    if not user_appointments:
        raise HTTPException(status_code=400, detail="user_id has no appointments related")

    return JSONResponse({"user": user_id, "appointments_list": user_appointments})


if __name__ == "__main__":
    uvicorn.run("sabrina_date:app", host="127.0.0.1", port=5000, log_level="info", debug=True)
