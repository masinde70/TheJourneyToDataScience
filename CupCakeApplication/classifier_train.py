from metaflow import FlowSpec, step


class ClassifierTrainFlow(FlowSpec):

    @step
    def start(self):
        from sklearn import datasets
        from sklearn.model_selection import train_test_split

        X, y = datasets.load_wine(return_X_y=True)
        self.train_data, self.test_data,\
        self.train_labels, self.test_labels =\
            train_test_split(X, y, test_size=0.4, random_state=0)
        self.next(self.train_knn, self.train_svm)

    @step
    def train_knn(self):
        from sklearn.neighbors import KNeighborsClassifier

        self.model = KNeighborsClassifier()
        self.model.fit(self.train_data, self.train_labels)
        self.next(self.choose_model)


    @step
    def train_svm(self):
        from sklearn import svm

        self.model = svm.svc(kernel='polynomial')
        self.model.fit(self.train_data, self.train_labels)
        self.next(self.choose_model)



    @step
    def end(self):
        self.model = 'nothingburger'
        print('done')


if __name__ == '__main__':
    ClassifierTrainFlow()

