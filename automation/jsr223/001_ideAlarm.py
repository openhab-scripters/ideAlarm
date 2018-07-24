from lucid.rules import rule, addRule
from idealarm import ideAlarm
from lucid.utils import hasReloadFinished

@rule
class ideAlarmTrigger(object):

    """Make ideAlarm trigger on item changes"""
    def getEventTriggers(self):
        return ideAlarm.getTriggers()

    def execute(self, modules, inputs):
        if not hasReloadFinished(True): return
        ideAlarm.execute(self, modules, inputs)

addRule(ideAlarmTrigger())
