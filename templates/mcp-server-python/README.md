# MCP server skeleton (Python)

```bash
pip install "mcp[cli]" pydantic
python server.py                      # runs over stdio
mcp dev server.py                     # opens the MCP Inspector to test tools
claude mcp add my-server -- python "$(pwd)/server.py"   # add to Claude Code
```

Checklist for a good tool (from module 04):
- Clear name and a description that says when to use it
- Typed inputs with descriptions
- Errors that tell the model how to fix the call
- Small, token-efficient outputs
