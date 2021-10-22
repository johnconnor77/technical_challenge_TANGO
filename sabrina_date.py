#!/usr/bin/env python

from appointment_models import AppointmentModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import utils.redis_object as red
from utils.redis_functions import redis_save, redis_load
import uvicorn
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app = FastAPI(title="Sabrina Date API",
              description="Here's our API to handle appointment scheduling", version="1.0")


@app.on_event('startup')
async def connect_redis():
    red.redis = await red.redis_connection()


@app.on_event('shutdown')
async def disconnect_redis():
    red.redis.close()
    await red.redis.await_closed()


@app.post("/api/schedule/", summary="Creates an Appointment for certain User",
          description="Endpoint that takes a date/time and user ID (both required). Creates an "
                      "appointment beginning at that time for that user or returns an appropriate status"
                      "code and error if the appointment cannot be made (the user already has an"
                      "appointment that day")
async def schedule(appointment_to_schedule: AppointmentModel):
    print(appointment_to_schedule)
    key = appointment_to_schedule.user_id
    value = {'date_appointment': appointment_to_schedule.date_appointment.isoformat(),
             'start_time': appointment_to_schedule.start_time.isoformat(),
             'end_time': appointment_to_schedule.end_time.isoformat()}
    await redis_save(key, value)

    return JSONResponse({"user": key, "appointment_info": value})


@app.get("/api/appointments/", summary="List Appointments for certain User",
         description="Endpoint that takes a user ID (required) and returns all appointments for the user")
async def appointments(user_id: int):
    user_appointments = await redis_load(user_id)

    return JSONResponse({"user": user_id, "appointments": user_appointments})

if __name__ == "__main__":
    uvicorn.run("sabrina_date:app", host="127.0.0.1", port=5000, log_level="info")
