# Rankade.py
> Unofficial Python async wrapper for the Rankade API.

## Installation
### pip
```zsh
pip3 install rankade.py
```

## Usage
### Access the Rankade API
- Select the group on Rankade you wish to use.
- From the "Group Manager" screen select "APIs".
  ![Rankade Group Manager Modal](docs/_static/images/rankade_group_manager.png)
- This should bring you to the "Credentials and status" page.
- Copy your key.
- Generate a secret.

### Sample Project
```python
import asyncio
import rankade

async def main():
    rankade = rankade.Rankade(key="rankade-key", secret="rankade-secret")
    result = rankade.get_games()
    print(result)

if __name__ == '__main__'
    asyncio.run(main())
```

### Examples
See [Documentation](https://calumcrawford.com/rankadepy/examples) or [Examples](https://github.com/14zombies/rankade.py/tree/main/examples) for more.

## Documentation
> [Documentation](https://calumcrawford.com/rankadepy)

