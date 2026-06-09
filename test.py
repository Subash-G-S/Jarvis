from agent.planner import create_plan
from agent.executor import execute_plan


request = """
Find Frontend internships make an excel and send the excel to my email
"""


plan = create_plan(
    request
)

print("\nPLAN:")
print(plan)

results = execute_plan(
    plan
)

print("\nRESULTS:")
print(results)