""" caliapactivitysummarizer.__main__: executed when caliapactivitysummarizer directory is called as script. """
import asyncio
from caliapactivitysummarizer.cli import main

if __name__ == "__main__":
    asyncio.run(main())