from metaflow import FlowSpec, step
import os

globa_value = 5


class ProcessDemoFlow(FlowSpec):

    @step
    def start(self):
        global globa_value
        globa_value = 9
        print('process ID is ', os.getpid())
        print('global value is', globa_value)

