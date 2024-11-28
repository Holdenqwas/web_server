from fastapi import APIRouter

router = APIRouter()


@router.post("/talk")
async def talk(event: dict):
    print(event)
    response = {
        "version": event["version"],
        "session": event["session"],
        "response": {"text": "загулшка", "end_session": False},
    }
    try:
        if (
            "request" not in event
            or "original_utterance" not in event["request"]
        ):
            response

        text = event["request"]["original_utterance"].lower().strip()
        print("\t", text)
        if text in ["привет", "здарова", "здравствуй"]:
            print("if")
            response["response"][
                "text"
            ] = "Привет, навык позволяет добавлять список покупок в \
телеграм бота"
        elif text in [
            "стоп",
            "закончили",
            "не надо",
            "все",
            "хватит",
            "пока",
            "до свидания",
            "конец",
            "нет",
            "отбой",
            "хватит",
        ]:
            print("elif")
            response["response"]["text"] = "Хороших покупок!"
            response["response"]["end_session"] = True

        else:
            print("\telse")
            response["response"]["text"] = text
    except Exception as e:
        print(e.args)
        response["response"][
            "text"
        ] = "Что-то пошло не так, повторите команду или попробуйте позже."
    return response
