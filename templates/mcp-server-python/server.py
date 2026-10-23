"""Minimal MCP server skeleton (Python SDK, FastMCP).

Run locally:   uv run server.py        (or: python server.py)
Claude Code:   claude mcp add my-server -- python /path/to/server.py
"""
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("my-server")


class LookupResult(BaseModel):
    id: str
    found: bool
    summary: str = ""


@mcp.tool()
def lookup_item(item_id: str = Field(description="Item ID, e.g. 'POL-1234'")) -> LookupResult:
    """Look up one item by ID. Use this before making any decision about the item."""
    if not item_id.startswith("POL-"):
        # Tell the model exactly how to fix the call.
        raise ValueError("item_id must look like 'POL-1234'. Ask the user for the ID if unknown.")
    # TODO: replace with real lookup (synthetic data only)
    return LookupResult(id=item_id, found=True, summary="Example item")


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
