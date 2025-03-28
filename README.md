# Korea Weather MCP

한국 날씨 정보를 확인할 수 있는 MCP Server입니다.


## 설치 방법 (Mac)

1. 저장소를 클론합니다:
```bash
git clone https://github.com/jikime/mcp-weather.git
cd mcp-weather
```

2. 필요한 패키지를 설치합니다:
```bash
pip install uv
uv venv
source .venv/bin/activate
uv add "mcp[cli]"
```

## 환경 변수 설정

1. 프로젝트 루트 디렉토리에 `.env` 파일을 생성합니다.
2. 다음 환경 변수를 설정합니다:

```
OPEN_DATA_API_KEY=your_api_key_here
```
* [기상청_단기예보 ((구)_동네예보) 조회서비스 OPEN API](https://www.data.go.kr/data/15084084/openapi.do) 에서 발급받을 수 있습니다.

## 실행 방법

# MCP 서버를 실행하려면 다음과 같이 실행합니다.
```bash
mcp dev ko_weather.py
```

# 또한, Claude Desktop 환경에서 실행하려면 다음 명령어를 사용할 수 있습니다.
```
mcp install ko_weather.py
```

# Claude Desktop 설정 확인 및 편집 (MAC)
- command : which uv 하여 절대 경로를 변경합니다.
- directory : mcp-weather 가 설치된 절대 경로로 변경합니다.
```
vi ~/Library/Application\ Support/Claude/claude_desktop_config.json

{
  "mcpServers": {
    "Korea Weather": {
      "command": "/path/bin/uv",
      "args": [
        "--directory",
        "/Users/Dev/mcp/mcp-weather",
        "run",
        "ko_weather.py"
      ]
    }
  }
}
```

## 주요 기능
- 시, 구, 동 검색을 통한 날씨 정보 확인
- 금일 날씨 예보 제공
- 하늘상태, 온도, 강수량,습도, 풍속, 풍향 등 상세 날씨 정보 표시
