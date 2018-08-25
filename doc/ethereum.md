# About Ethereum

## MetaMask
- allows you to run Ethereum dApps in your browser without running a full Ethereum node

## TestNet
- Ropsten
    - Proof Of Work
- Kovan
    - Proof Of Authority (Parity only)
- Rinkeby
    - Clique Consensus (Geth only)

## Truffle

### Installation
```
npm install -g truffle


## Ganache

### Installation
```
npm install -g ganache-cli
```

## Setting up Dapp
```
mkdir metacoin
cd metacoin
truffle init  @ Initialize a default truffle project in that folder
truffle compiler
truffle migrate  # Build, compile, & deploy the dapp
truffle test test/metacoin.js
```

### Run
```
ganache-cli
ganache-cli -m "seed phrase"  --start up with accounts you already have in MetaMask
```
