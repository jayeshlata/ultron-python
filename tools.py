import asyncio
from mcp.server.fastmcp import FastMCP

# Create a "FastMCP" server named SpookyTools
mcp = FastMCP("SpookyTools")

@mcp.tool()
async def order_food(restaurant: str, dish: str) -> str:
    """Orders food from a specific restaurant via Zomato."""
    # This is a stub for the future Zomato API integration
    return f"👻 Spooky has cast a spell on Zomato! Your '{dish}' from '{restaurant}' is being prepared in the spirit world."

@mcp.tool()
async def get_system_status() -> str:
    """Checks the health of Spooky's local host (your Mac)."""
    import platform
    return f"👻 I am haunting a {platform.system()} machine (v{platform.version()}). The connection is stable."

if __name__ == "__main__":
    mcp.run()
