# AGV 调度系统 (AGV Scheduler)

工厂级 AGV 调度后端，基于 **FastAPI + Tortoise-ORM + MySQL + Redis**，
通过 TCP 协议对接仙工 (SEER) 控制器。

## 总体分层

```
┌──────────────────────────────────────────────┐
│  HTTP / WebSocket  ← FastAPI 接入层 (api/v1) │
├──────────────────────────────────────────────┤
│  Services 任务层    ← 业务编排                │
├──────────────────────────────────────────────┤
│  Scheduler 调度层   ← 派车/交管/充电决策      │
├──────────────────────────────────────────────┤
│  Connectors 连接层  ← 仙工/PLC/充电桩 (★ 唯一  │
│                       允许出现硬件细节)        │
└──────────────────────────────────────────────┘
        ↓                          ↓
   ┌─────────┐                ┌─────────┐
   │  MySQL  │ 配置/历史/任务  │  Redis  │ 实时状态/锁
   └─────────┘                └─────────┘
```

## 关键约束 (始终遵守)

1. **硬件细节只允许出现在 `app/connectors/`** —— 字节、msg_type、socket、modbus 等。
   向上只暴露语义化方法 (`navigate()`, `get_status()`, `cancel_task()`)。
2. `app/services/` 只编排业务流程，不直接 carry 字节。
3. `app/scheduler/` 做全局决策，输出"派给谁"，由 services 调 connectors 落地。
4. **配置/历史落 MySQL，实时状态走 Redis**，调度热路径不查 MySQL。
5. 一台 AGV 一个长连接 + 一个 `asyncio.Task` 收包；
   `req_id → Future` 字典做请求/响应配对；主动推送走事件总线。

## 目录速览

```
app/
├── main.py              FastAPI 入口
├── core/                配置 / 日志 / 安全 (JWT)
├── db/                  Tortoise / Redis 连接
├── models/              ORM 模型 (user/agv/task/...)
├── schemas/             Pydantic 入出参
├── api/v1/endpoints/    REST 接口
├── services/            任务层 业务编排
├── scheduler/           调度层 (占位)
├── connectors/
│   ├── seer/            仙工 AGV (TCP)
│   ├── plc/             PLC (占位)
│   └── charger/         充电桩 (占位)
├── workers/             后台 asyncio (心跳轮询等，占位)
├── ws/                  WebSocket 推送 (占位)
└── utils/               通用工具/异常
```

## 本地启动 (Windows)

> 假设你已经本地装好了 MySQL 8 与 Redis 7。

```powershell
# 1. 建数据库
mysql -uroot -p -e "CREATE DATABASE agv_scheduler CHARACTER SET utf8mb4;"

# 2. Python 环境
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. 配置环境变量
copy .env.example .env
# 编辑 .env 填入 MySQL/Redis 实际地址与密码

# 4. 初始化数据库 (第一次运行)
aerich init -t app.db.tortoise_conf.TORTOISE_ORM
aerich init-db

# 5. 启动开发服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 浏览器打开:
#   http://localhost:8000/docs    Swagger UI
#   http://localhost:8000/health  健康检查
```

## 当前进度

- [x] 项目骨架搭建
- [x] 仙工协议层迁移 (`app/connectors/seer/protocol.py`)
- [ ] 仙工 TCP 客户端 (`client.py`) + 高层 API (`api.py`)
- [ ] AGV / Task 模型与 CRUD 接口
- [ ] 任务下发接口 `POST /api/v1/tasks`
- [ ] WebSocket 实时状态推送
- [ ] 调度层 (派车 / 交管 / 自动充电)
- [ ] 前端 Vue
