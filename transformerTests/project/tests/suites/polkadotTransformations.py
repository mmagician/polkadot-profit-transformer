import unittest

from transformerTests.project.tests.polkadotTransformations.transformerExtrinsicsTest import TransformerExtrinsicsTest
from transformerTests.project.tests.polkadotTransformations.transformerProfitEventsFilterTest import \
    TransformerProfitEventsFilterTest
from transformerTests.project.tests.polkadotTransformations.transformerBlocksTest import TransformerBlocksTest
from transformerTests.project.tests.polkadotTransformations.transformerEventsTest import TransformerEventsTest
from transformerTests.project.tests.polkadotTransformations.transformerBalancesTest import TransformerBalancesTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TransformerBlocksTest('test_transformer_blocks'))
    suite.addTest(TransformerEventsTest('test_transformer_events'))
    suite.addTest(TransformerExtrinsicsTest('test_transformer_extrinsics'))
    suite.addTest(TransformerProfitEventsFilterTest('test_transformer_profit_events_filter'))
    suite.addTest(TransformerBalancesTest('test_transformer_balances'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    result = runner.run(suite())
