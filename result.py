import jug
import tasks
jug.init('tasks.py', 'redis://localhost:6379')

print(tasks.results)
results = jug.task.value(tasks.results)
