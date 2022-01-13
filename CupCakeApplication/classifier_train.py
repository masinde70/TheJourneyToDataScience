from metaflow import FlowSpec, step


class ClassifierTrainFlow(FlowSpec):

    @step
    def start(self):
