#!/usr/bin/python3

import json
from pathlib import Path
from datetime import datetime

# CDN 基础 URL
CDN_BASE_URL = "https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/"

def get_icon_info(png_file, svg_dir):
    """获取图标信息"""
    name = png_file.stem
    png_path = f"{CDN_BASE_URL}png/{png_file.name}"
    
    # 检查是否存在对应的 SVG 文件
    svg_file = svg_dir / f"{name}.svg"
    svg_path = f"{CDN_BASE_URL}svg/{name}.svg" if svg_file.exists() else None
    
    return {
        "name": name,
        "displayName": name.replace("-", " ").title(),
        "png": png_path,
        "svg": svg_path,
        "formats": ["png"] + (["svg"] if svg_path else [])
    }

def main():
    png_dir = Path("./png")
    svg_dir = Path("./svg")
    
    # 获取所有 PNG 文件
    png_files = sorted(png_dir.glob("*.png"))
    
    # 生成图标信息列表
    icons = [get_icon_info(png_file, svg_dir) for png_file in png_files]
    
    # 构建 JSON 结构
    icon_library = {
        "name": "Lsimply Icons",
        "version": "1.0.0",
        "description": "A collection of icons for Lsimply dashboard",
        "source": "https://github.com/Lsimply/icons",
        "generatedAt": datetime.now().isoformat(),
        "totalIcons": len(icons),
        "statistics": {
            "png": len(png_files),
            "svg": len(list(svg_dir.glob("*.svg"))),
            "pngOnly": len([icon for icon in icons if not icon["svg"]]),
            "bothFormats": len([icon for icon in icons if icon["svg"]])
        },
        "icons": icons
    }
    
    # 写入 JSON 文件
    output_file = Path("./icons.json")
    with open(output_file, "wt", encoding="UTF-8") as f:
        json.dump(icon_library, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 成功生成图标库 JSON 文件: {output_file}")
    print(f"📊 统计信息:")
    print(f"   - 总图标数: {icon_library['statistics']['png']}")
    print(f"   - PNG 格式: {icon_library['statistics']['png']}")
    print(f"   - SVG 格式: {icon_library['statistics']['svg']}")
    print(f"   - 仅 PNG: {icon_library['statistics']['pngOnly']}")
    print(f"   - 双格式: {icon_library['statistics']['bothFormats']}")

if __name__ == "__main__":
    main()

