from mailer import GoodMorningMailer
from services.api_service import ApiService
import re

api_service = ApiService()
mailer = GoodMorningMailer()

weather = api_service.fetch_day_weather_forcast()

will_rain = False
for hour_data in weather:
    condition_code = hour_data["weather"][0]["id"]

    if condition_code < 700:
        will_rain = True

email_subject = "Good Morning! Wishing You a Bright Day!"

quote = mailer.get_random_quote()

with open("data/message.txt", encoding="utf8") as file:
    body = file.read()
    body = body.replace("[QUOTE]", quote)
    if will_rain:
        body = body.replace(
            "[RAIN_ALERT]",
            "Also, a quick heads-up—there’s a chance of rain today! Don’t forget to bring an umbrella. "
        )
    else:
        body = re.sub(r"\n?\[RAIN_ALERT\]\n?", "", body)

mailer.send_mail(email_subject, body)