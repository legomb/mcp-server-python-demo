from mcp.server.fastmcp import FastMCP

# Initialize the server
mcp = FastMCP("mix_server")

# Import tools so they get registered via decorators
import tools.csv_tools
import tools.parquet_tools

# Run the server
if __name__ == "__main__":
    mcp.run()
