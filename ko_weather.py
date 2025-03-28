from mcp.server.fastmcp import FastMCP
import asyncio
from api import get_forecast_api
from utils import make_api_request

mcp = FastMCP("weather")

# Constants
LOCATION_API_BASE = "http://localhost:8888/api/v1"

def format_location(location: dict) -> str:
    """Format an alert feature into a readable string."""
    return f"""
City(시): {location.get('level1', 'Unknown')}
Gu(구): {location.get('level2', 'Unknown')}
Dong(동): {location.get('level3', 'Unknown')}
Nx: {location.get('grid_x', 'Unknown')}
Ny: {location.get('grid_y', 'Unknown')}
"""

# 기상청_단기예보 ((구)_동네예보) 조회서비스 OPEN API - https://www.data.go.kr/data/15084084/openapi.do
@mcp.tool()
async def get_grid_location(city: str, gu: str, dong: str) -> str:
    """Get grid location(nx, ny) for Korea Weather

    Args:
        city: City Name (e.g. 서울특별시)
        gu: Gu Name (e.g. 서초구)
        dong: Dong Name (e.g. 양재1동)
    """
    url = f"{LOCATION_API_BASE}/geo/location/{city}/{gu}/{dong}"
    data = await make_api_request(url)
    if not data or data["id"] == "":
        return "Unable to fetch grid location or no grid location found."

    return format_location(data)

@mcp.tool()
async def get_forecast(city: str, gu: str, dong: str, nx: float, ny: float) -> str:
    """Get weather forecast for a location.

    Args:
        city: City Name (e.g. 서울특별시)
        gu: Gu Name (e.g. 서초구)
        dong: Dong Name (e.g. 양재1동)
        nx: Grid X coordinate
        ny: Grid Y coordinate
    """
    
    return await get_forecast_api(city, gu, dong, nx, ny)
  
if __name__ == "__main__":
  # Initialize and run the server
  mcp.run(transport='stdio')
  # asyncio.run(get_grid_location("서울특별시", "서초구", "양재1동"))
  # asyncio.run(get_forecast(37.7749, -122.4194))

# 설치
# uv init weather
# uv venv
# uv add "mcp[cli]" httpx  
# MCP 서버를 실행하려면 다음과 같이 실행합니다.
# mcp dev ko_weather.py

# 또한, Claude Desktop 환경에서 실행하려면 다음 명령어를 사용할 수 있습니다.
# mcp install ko_weather.py