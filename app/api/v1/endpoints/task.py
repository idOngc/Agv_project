"""
\u4efb\u52a1\u4e0b\u53d1\u63a5\u53e3 \u2014\u2014 \u8fd9\u662f\u8fd9\u4e2a\u9879\u76ee\u300c\u7b2c\u4e00\u6b65\u300d\u7684\u6838\u5fc3\u51fa\u53e3\uff0c\u4e0b\u4e00\u8f6e\u8865\u5b8c\u3002

\u8c03\u7528\u94fe\u8def\u5f84\u8bbe\u8ba1:
    POST /api/v1/tasks
        \u2192 services.task_service.create_and_dispatch(payload)
            \u2192 connectors.seer.manager.get(agv_uuid)        # \u62ff\u5230\u8fde\u63a5
            \u2192 connectors.seer.api.navigate(target_point)    # \u9ad8\u5c42\u8c03\u7528
                \u2192 client.send_request(msg_type, body)        # \u4f4e\u5c42 TCP
"""

from fastapi import APIRouter, HTTPException, status

from app.schemas.task import TaskCreateIn, TaskOut

router = APIRouter()


@router.post("", response_model=TaskOut, summary="\u4e0b\u53d1\u4efb\u52a1 (\u5360\u4f4d)")
async def create_task(payload: TaskCreateIn) -> TaskOut:
    raise HTTPException(
        status.HTTP_501_NOT_IMPLEMENTED,
        "TODO: \u4e0b\u4e00\u6b65\u8865\u5b8c connectors/seer/api.py \u540e\u63a5\u5165",
    )


@router.get("/{task_id}", response_model=TaskOut, summary="\u67e5\u8be2\u4efb\u52a1 (\u5360\u4f4d)")
async def get_task(task_id: int) -> TaskOut:
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO")
