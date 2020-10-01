import ksqlTests.project.utils as utils
import ksqlTests.project.paths as paths


class BaseTest:

    def __init__(self, ):
        self.log = utils.get_loger()
        self.paths = paths
