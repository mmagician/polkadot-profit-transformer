# Tests

## blocksTests

### Existed tests

* CompareHeadRpcTest - comparing node latest block with maximum block in the blocks table

* MissedBlocksTests - comparing the maximum block in the blocks table with the count of blocks in node

### Starting tests

* from Dockerfile
```bash
cd polkadot-profit-transformer/blocksTests
docker build -t tester .
docker run --name tests-from-dockerFile tester
```

* from docker-compose
```bash
cd polkadot-profit-transformer/blocksTests
docker-compose up --build -d blocks-tests
docker-compose logs -f blocks-tests
```

## ksqlTests

### Existed tests

* transformerBalancesTest
* transformerBlocksTest
* transformerEventsTest
* transformerExtrinsicsTest
* transformerProfitEventsFilterTest

### Starting tests

* from Dockerfile
```bash
cd polkadot-profit-transformer/transformerTests
docker build -t tester .
docker run --name tests-from-dockerFile tester
```

* from docker-compose
```bash
cd polkadot-profit-transformer/transformerTests
docker-compose up --build -d transformerTests
docker-compose logs -f transformerTests
```