import json
import sys

SITE_DATA = {
    "name": "华体会",
    "keywords": ["华体会", "体育", "娱乐", "电竞"],
    "url": "https://app-main-hth.com.cn",
    "description": "华体会是一个综合性的体育与娱乐平台，提供丰富的赛事、电竞和互动体验。",
    "tags": ["体育", "电竞", "娱乐", "平台"]
}

def format_summary(data: dict) -> str:
    lines = []
    lines.append(f"站点名称: {data['name']}")
    lines.append(f"URL: {data['url']}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"标签: {', '.join(data['tags'])}")
    lines.append(f"简介: {data['description']}")
    return "\n".join(lines)

def generate_structured_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)

def print_summary(data: dict) -> None:
    print("=" * 48)
    print("  站点结构化摘要")
    print("=" * 48)
    print(format_summary(data))
    print("=" * 48)

def main() -> None:
    data = SITE_DATA
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--json":
            print(generate_structured_json(data))
            return
        elif arg == "--help":
            print("用法: python site_summary.py [--json]")
            print("  --json  输出 JSON 格式")
            return
    print_summary(data)

if __name__ == "__main__":
    main()