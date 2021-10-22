import json
import utils.redis_object as red


async def redis_save(key: object, value: object) -> object:
    """
        Function that allows to load certain value from Redis Database
    :param key: Our redis Key that stores each element by its user_id
    :param value: Our values to be stored
        {date_appointment:'', start_time:'', end_time: ''}
    :return: object
    """
    if key is not None and value is not None:
        await red.redis.set(json.dumps(key), json.dumps(value))


async def redis_load(key: object) -> object:
    """
        Function that allows to load certain value from Redis Database
    :param key: Our redis Key that stores each element by its user_id
    :return: object
    """
    if key is None:
        return None
    value = await red.redis.get(key)
    if value is not None:
        return json.loads(value)
    return "error, dataplugin_id is not related to any bot"