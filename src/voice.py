import os
import swiftclient
from pydub import AudioSegment
from io import BytesIO
from src.config import Config as config

storage = swiftclient.client.Connection(
    authurl='https://api.selcdn.ru/auth/v1.0',
    user=config.SELECTEL_USER,
    key=config.SELECTEL_PASSWORD,
    auth_version=1,
)

class VoiceConvering:
    def convert_voice(container_name, object_name):
        print(container_name, object_name)
        _, obj_body = storage.get_object(container_name, object_name)
        content = BytesIO(obj_body)
        audio = AudioSegment.from_file(content)
        audio_converted = audio.export(object_name, format="mp3")
        storage.put_object(container_name, object_name, audio_converted)
        content.close()
        os.remove(object_name)
        return f"Converted «{object_name}» in «{container_name}»"