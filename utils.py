import httpx
from typing import Any

USER_AGENT = "weather-app/1.0"

async def make_api_request(url: str) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

# print(get_location("서울특별시 강남구 테헤란로 14길 6 남도빌딩 2층"))
async def get_kakao_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    headers = {"Authorization": "KakaoAK 7dc999da8d93bee8dacebcd23b8f0f23"}
    async with httpx.AsyncClient() as client:
      try:
          response = await client.get(url, headers=headers, timeout=30.0)
          response.raise_for_status()
          return response.json()
      except Exception:
          return None
          