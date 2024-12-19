from jug import TaskGenerator
from jug.hooks.exit_checks import exit_after_n_tasks
import time

@TaskGenerator
def slow_task(i):
    time.sleep(2)  # 模拟耗时任务
    return i * i

# 定义多个任务
results = [slow_task(i) for i in range(400)]
print(results)