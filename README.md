# Get ETH Price by Block Number
Fetch the price of ETH at a given Ethereum block number. Powered by the Dune API.

## Getting Started

You will first need to obtain a Dune API key. You can sign up for a free account at [dune.com](https://www.dune.com/).

Then, install the dependencies.
`pip3 install -r requirements.txt`

## Fetch Data
```bash
python get-eth-price-by-block-number.py
```

#### Required Inputs:
- Block number
- Dune API key

#### Output:
- Price of ETH at the provided block number

## Dune Query

The underlying SQL query on Dune can be found [here](https://dune.com/queries/2424632). Note that the price of ETH is generated at a granularity of 1 minute.
