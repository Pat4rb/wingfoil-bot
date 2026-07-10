def wind_direction_name(deg):

    directions = [
        "N","NE","E","SE",
        "S","SW","W","NW"
    ]

    index = round(deg / 45) % 8

    return directions[index]


def calculate_score(weather, spot):

    hourly = weather["hourly"]

    results = []

    for i, wind in enumerate(hourly["windspeed_10m"]):

        score = 0

        direction = wind_direction_name(
            hourly["winddirection_10m"][i]
        )

        if 12 <= wind <= 30:
            score += 40
        elif 8 <= wind < 12:
            score += 25

        if direction in spot["ideal_wind"]:
            score += 25

        clouds = hourly["cloudcover"][i]

        if clouds < 30:
            score += 15
        elif clouds < 60:
            score += 8

        if hourly["precipitation"][i] > 0:
            score -= 20

        score *= spot["thermal_factor"]

        results.append({
            "hour": hourly["time"][i],
            "score": round(min(score,100)),
            "wind": wind,
            "direction": direction
        })

    return max(
        results,
        key=lambda x: x["score"]
    )
