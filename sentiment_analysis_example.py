import os
from pathlib import Path

from asyncflows import AsyncFlows


async def main():
    # Data to model after (will probably be classified as janky)
    data = "WHATDDUP"

    # Load the flow from the file
    flow = AsyncFlows.from_file("sentiment_analysis_example.yaml")

    # Run the flow
    result = await flow.set_vars(data=data).run()

    # Print the result
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
