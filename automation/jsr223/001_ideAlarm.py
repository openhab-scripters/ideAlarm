from openhab.rules import rule, addRule
from idealarm import ideAlarm
from mylib.utils import hasReloadFinished

@rule
class ideAlarmTrigger(object):

    """Make ideAlarm trigger on item changes"""
    def getEventTriggers(self):
        return ideAlarm.getTriggers()

    def execute(self, modules, inputs):
        if not hasReloadFinished(True): return
        ideAlarm.execute(modules, inputs)

addRule(ideAlarmTrigger())
