from spots import SPOTS
from weather import get_weather
from scoring import calculate_score


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

    print("🏄 Wingfoil Forecast\n")

    for r in results:

        print(
            f"""
{r['spot']}
Score: {r['score']}/100
Zeit: {r['hour']}
Wind: {r['wind']} km/h {r['direction']}
"""
        )


if __name__ == "__main__":
    run()
