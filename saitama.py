"""saitama"""
import math as m

def main(push_goal, sit_goal, squad_goal, run_goal, push, sit, run, squad):
    """main"""
    push_day = m.ceil(push_goal/push)
    sit_day = m.ceil(sit_goal/sit)
    squad_day = m.ceil(squad_goal/squad)
    run_day = m.ceil(run_goal/run)
    x = push_day
    if sit_day > x:
        x = sit_day
    if squad_day > x:
        x = squad_day
    if run_day > x:
        x = run_day
    print(int(x))
main(int(input()),int(input()),int(input()),int(input()),
     int(input()),int(input()),int(input()),int(input()))
