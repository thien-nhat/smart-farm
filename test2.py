from time import sleep
from tb_device_mqtt import TBDeviceMqttClient

DEVICE_ID = "4c2fe410-cd78-11ed-9b15-dd2dac50548f"  # Replace with your device ID

TOKEN = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ2YW4ucGhhbWRpbmh2YW4yMkBoY211dC5lZHUudm4iLCJ1c2VySWQiOiI1NGI3Njg1MC0xYjM0LTExZWYtYTQzNS1hYjNhMWQ1MzVmM2UiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sInNlc3Npb25JZCI6ImM2MWQwZGNjLTZmMDItNDdlYi1hMzA1LWU4NDZhOGNjNzk3ZiIsImV4cCI6MTcxODUwOTcyNCwiaXNzIjoidGhpbmdzYm9hcmQuaW8iLCJpYXQiOjE3MTY3MDk3MjQsImZpcnN0TmFtZSI6IlbEgk4iLCJsYXN0TmFtZSI6IlBI4bqgTSDEkMOMTkgiLCJlbmFibGVkIjp0cnVlLCJwcml2YWN5UG9saWN5QWNjZXB0ZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiI2NTMzYWEzMC1iOGNiLTExZWQtOWIxNS1kZDJkYWM1MDU0OGYiLCJjdXN0b21lcklkIjoiMTM4MTQwMDAtMWRkMi0xMWIyLTgwODAtODA4MDgwODA4MDgwIn0.IDusyZ1K9xDDzyAI29F4ot5UFO5DwtsKFdydci233CJNl26qJrQ4LmMpLjET5oeULwVIBQWKfJq_Zxy0vXH76g'
token = 'qmxrjQH0sbbjF9fdLUWb'

def on_attributes_change(result, exception):
    if exception is not None:
        print("Exception:", str(exception))
    else:
        print(result)

client = TBDeviceMqttClient("demo.thingsboard.io", username=token)
client.connect()

client.subscribe_to_attribute("PUMP", on_attributes_change)  # Subscribe to attribute changes


while True:
    sleep(1)
