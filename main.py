import os
import requests

from spots import SPOTS
from weather import get_weather
from scoring import calculate_score


def send_telegram(message):

    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = (
        f"https://api.telegram.org/bot{token}/sendMessage"
    )

    data = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=data)


def run():

    results = []

    for spot in SPOTS:

        weather = get_weather(
            spot["lat"],
            spot["lon"]
        )

        result = calculate_score(
            weather,
            spot
        )

        results.append(
            {
                "spot": spot["name"],
                **result
            }
        )


    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    best = results[0]


    message = f"""
🏄 Wingfoil Forecast Allgäu

🥇 Beste Option:
{best['spot']}

Score:
{best['score']}/100

Zeit:
{best['hour']}

Wind:
{best['wind']} km/h {best['direction']}


Alle Spots:
"""


    for r in results:

        message += (
            f"\n{r['spot']}: "
            f"{r['score']}/100"
        )


    send_telegram(message)


if __name__ == "__main__":
    run()
