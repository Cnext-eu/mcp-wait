from fastmcp import FastMCP
import asyncio

app = FastMCP("wait")

notes = {}

@app.tool("wait")
async def wait(seconds: int):
    """
    Wait for a specified number of seconds before responding.
    """
    await asyncio.sleep(seconds)
    return [{"type": "text", "text": f"Waited for {seconds} second(s)."}]


if __name__ == "__main__":
    app.run(transport="sse", host="0.0.0.0", port=8000)