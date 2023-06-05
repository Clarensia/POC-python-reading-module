# POC Python read module

## Introduction

The goal of this proof of concept is to be able to parse a Python docstring file.

This file will be later used to generate documentation for [docusaurus](https://docusaurus.io/)

## Input & Outputs

### Main class

#### Input

```python
class BlockchainAPIs:
    """High-frequency DEX API
    """
 
    async def blockchains(self) -> List[Blockchain]:
        """Get the list of blockchains supported by the API

        :return: The list of the blockchains supported by the API.
        
        Using this method, you can find the id of the blockchain that you can use for
        other function calls.

        Example response:
        ```json
        [
            {
                "blockchain": "avalanche",
                "name": "Avalanche",
                "chain_id": 43114,
                "explorer": "https://snowtrace.io/"
            }

        ]
        ```
        :rtype: List[Blockchain]
        """
```
#### Output

We need to be able to print in the terminal the following things:
- Name of the class: BlockchainAPIs
- Description of the class: High-frequency DEX API
- Function definition: async def blockchains(self) -> List[Blockchain]:
- Function description: Get the list of blockchains supported by the API
- The return description: The list of the blockchains supported by the API.
                          Using this method, you can find the id of the blockchain that you can use for
                          other function calls.
- The example response:
  [
      {
          "blockchain": "avalanche",
          "name": "Avalanche",
          "chain_id": 43114,
          "explorer": "https://snowtrace.io/"
      }

  ]
- The returned type: List\[Blockchain\]

