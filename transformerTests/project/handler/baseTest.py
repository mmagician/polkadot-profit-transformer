import transformerTests.project.utils as utils
import transformerTests.project.paths as paths


class BaseTest:

    def __init__(self, ):
        self.log = utils.get_loger()
        self.paths = paths
