"""
Author       : FYWinds i@windis.cn
Date         : 2021-11-19 19:17:02
LastEditors  : FYWinds i@windis.cn
LastEditTime : 2022-09-05 22:12:38
FilePath     : /gocqapi/_api.py

Copyright (c) 2022 by FYWinds i@windis.cn
All Rights Reserved.
Any modifications or distributions of the file
should mark the original author's name.
"""
from typing import Any, Union, Optional, Dict

import nonebot
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Message, escape, Bot


class BaseAPI:
    bot: Optional[Bot] = None
    bot_id: Optional[str] = None

    def __init__(
        self, bot_id: Optional[Union[int, str]] = None, bot: Optional[Bot] = None
    ) -> None:
        self.bot_id = str(bot_id) if isinstance(bot_id, int) else bot_id
        self.bot = bot

    async def call(self, api: str, **kwargs: Any) -> Dict[Any, Any]:
        if self.bot is None:
            try:
                _bot = (
                    nonebot.get_bot(self.bot_id) if self.bot_id else nonebot.get_bot()
                )
                assert _bot is Bot
            except (ValueError, KeyError) as e:
                logger.error("请求API失败，未连接Bot")
                raise e
            except (AssertionError) as e:
                logger.error("请求API失败，Bot类型错误")
                raise e
        try:
            try:
                kwargs["user_id"] = (
                    int(kwargs["user_id"]) if kwargs["user_id"] else None
                )
                kwargs["group_id"] = (
                    int(kwargs["group_id"]) if kwargs["group_id"] else None
                )
                kwargs["message_id"] = (
                    int(kwargs["message_id"])
                    if kwargs["message_id"].isdigit()
                    else kwargs["message_id"]
                )
                if "message" in kwargs:
                    message = kwargs["message"]
                    message = (
                        escape(message, escape_comma=False)
                        if isinstance(message, str)
                        else message
                    )
                    message = (
                        message if isinstance(message, Message) else Message(message)
                    )
            except ValueError:
                raise TypeError("请求API参数类型错误")

            assert self.bot is not None
            return await self.bot.call_api(api, **kwargs)
        except (ValueError, AssertionError) as e:
            logger.error("请求API失败，未连接Bot")
            raise e
