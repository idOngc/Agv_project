"""
\u4efb\u52a1\u4e1a\u52a1\u7f16\u6392 \u2014\u2014 \u4e0b\u4e00\u6b65\u8865\u5b8c\u3002

\u62df\u5b9a\u4e3b\u5165\u53e3:
    async def create_and_dispatch(payload: TaskCreateIn) -> Task:
        1. \u68c0\u67e5 AGV \u5b58\u5728 / \u542f\u7528
        2. INSERT task (status=INIT)
        3. \u8c03 connectors.seer.api.navigate(...) \u4e0b\u53d1
        4. \u6210\u529f \u2192 status=RUNNING\uff0c\u5931\u8d25 \u2192 status=FAILED+error_msg
        5. \u8fd4\u56de Task
"""
