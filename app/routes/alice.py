from app.utils.auth import decode_token
from app.utils.database import get_db
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.shop_list import add_items_to_shop_list_from_alice

router = APIRouter()


@router.post("/talk")
async def talk(
    event: dict,
    user_id: int | None = Depends(decode_token),
    db: AsyncSession = Depends(get_db),
):
    response = {
        "version": event["version"],
        "session": event["session"],
        "response": {
            "text": "Что-то пошло не так, попробуйте позже",
            "end_session": False,
        },
    }

    try:
        if (
            "request" not in event
            or "original_utterance" not in event["request"]
        ):
            return response

        text = event["request"]["original_utterance"].lower().strip()

        if not user_id:
            response["response"][
                "text"
            ] = "Привет, для работы с навыком нужно \
открыть телеграм бота khorn butler bot, нажать на кнопку покупки, связать \
список с Яндекс станцией. Дальше авторизоваться в приложении Яндекса и ввести \
два числа в форму."

            response["response"]["directives"] = {"start_account_linking": {}}
            return response

        if text in ["привет", "здарова", "здравствуй"]:
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
            response["response"]["text"] = "Хороших покупок!"
            response["response"]["end_session"] = True

        else:
            status = await add_items_to_shop_list_from_alice(user_id, text, db)

            if status:
                response["response"]["text"] = "Всё записала"
            else:
                response["response"]["text"] = "Ой, у меня ручка не писала, повтори, пожалуйста"

    except Exception as e:
        print(e.args)
        response["response"][
            "text"
        ] = "Что-то пошло не так, повторите команду или попробуйте позже."
    return response
