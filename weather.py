from mcp.server.fastmcp import FastMCP


mcp = FastMCP("weather")


@mcp.tool()
async def get_weather(location:str) -> str:
    """
    Get weather location
    """

    return "It is always rainy"




if __name__ =="__main__":
    mcp.run(transport ="streamable-http")