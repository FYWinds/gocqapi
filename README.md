# Nonebot-plugin-gocqapi

通过 pydantic 为 go-cqhttp 的 API 添加了完善的类型注解和返回值models

__目前还在测试阶段__

### 安装与使用

并不需要作为nonebot的插件安装

```powershell
poetry add gocqapi
# 或使用
pip install gocqapi
```

仅连接单机器人使用
```python
from gocqapi import api

await api.xxxxxx()
```

多机器人指定调用某个机器人
```python
from gocqapi import API

api = API(bot_id)
await api.xxxxxx()
```

使用类型Models
```python
from gocqapi.models import *  # 已使用__all__限制能够引入的Model
# 或使用
from gocqapi.models import Xxxxx
```

### Example
```python
# 范例
foo = await api.get_group_system_msg()
for joinreq in foo.join_requests:
    print(foo.message)
```