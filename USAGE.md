# Lsimply Icons 使用指南

## 📦 获取图标库

### 方式一：直接使用 CDN

图标库 JSON 文件可通过 CDN 直接访问：

```javascript
const iconsUrl = 'https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json';
```

### 方式二：下载到本地

```bash
# 下载 JSON 文件
curl -O https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json
```

## 📋 JSON 文件结构

```json
{
  "name": "Lsimply Icons",
  "version": "1.0.0",
  "description": "A collection of icons for Lsimply dashboard",
  "source": "https://github.com/Lsimply/icons",
  "generatedAt": "2025-12-01T01:10:50.324455",
  "totalIcons": 572,
  "statistics": {
    "png": 572,
    "svg": 250,
    "pngOnly": 332,
    "bothFormats": 240
  },
  "icons": [
    {
      "name": "arch-linux",
      "displayName": "Arch Linux",
      "url": "https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/png/arch-linux.png",
      "png": "png/arch-linux.png",
      "svg": "svg/arch-linux.svg",
      "formats": ["png", "svg"]
    }
  ]
}
```

### 字段说明

- **`name`**: 图标名称（文件名，不含扩展名）
- **`displayName`**: 显示名称（格式化后的名称）
- **`url`**: 完整的 CDN URL，可直接使用（PNG 格式）
- **`png`**: PNG 文件的相对路径
- **`svg`**: SVG 文件的相对路径（如果存在）或 `null`
- **`formats`**: 该图标可用的格式列表

## 🚀 使用方法

### 1. JavaScript / TypeScript

#### 加载图标库

```javascript
// 从 CDN 加载
async function loadIcons() {
  const response = await fetch('https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json');
  const iconLibrary = await response.json();
  return iconLibrary;
}

// 使用示例
loadIcons().then(library => {
  console.log(`共有 ${library.totalIcons} 个图标`);
  
  // 查找特定图标
  const dockerIcon = library.icons.find(icon => icon.name === 'docker');
  if (dockerIcon) {
    console.log('Docker 图标 URL:', dockerIcon.url);
  }
});
```

#### 搜索图标

```javascript
function searchIcons(iconLibrary, keyword) {
  return iconLibrary.icons.filter(icon => 
    icon.name.toLowerCase().includes(keyword.toLowerCase()) ||
    icon.displayName.toLowerCase().includes(keyword.toLowerCase())
  );
}

// 使用示例
loadIcons().then(library => {
  const linuxIcons = searchIcons(library, 'linux');
  console.log('找到的 Linux 相关图标:', linuxIcons);
});
```

#### 获取图标 URL

```javascript
function getIconUrl(iconLibrary, iconName) {
  const icon = iconLibrary.icons.find(i => i.name === iconName);
  return icon ? icon.url : null;
}

// 使用示例
loadIcons().then(library => {
  const githubUrl = getIconUrl(library, 'github');
  console.log('GitHub 图标 URL:', githubUrl);
});
```

### 2. HTML 中使用

```html
<!DOCTYPE html>
<html>
<head>
  <title>图标示例</title>
</head>
<body>
  <div id="icons-container"></div>

  <script>
    async function displayIcons() {
      const response = await fetch('https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json');
      const library = await response.json();
      
      const container = document.getElementById('icons-container');
      
      // 显示前 20 个图标
      library.icons.slice(0, 20).forEach(icon => {
        const img = document.createElement('img');
        img.src = icon.url;
        img.alt = icon.displayName;
        img.title = icon.displayName;
        img.style.width = '50px';
        img.style.height = '50px';
        img.style.margin = '10px';
        container.appendChild(img);
      });
    }
    
    displayIcons();
  </script>
</body>
</html>
```

### 3. React 组件

```jsx
import React, { useState, useEffect } from 'react';

function IconLibrary() {
  const [icons, setIcons] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetch('https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json')
      .then(res => res.json())
      .then(data => setIcons(data.icons));
  }, []);

  const filteredIcons = icons.filter(icon =>
    icon.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    icon.displayName.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <input
        type="text"
        placeholder="搜索图标..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        style={{ padding: '10px', width: '300px', marginBottom: '20px' }}
      />
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(100px, 1fr))', gap: '20px' }}>
        {filteredIcons.map(icon => (
          <div key={icon.name} style={{ textAlign: 'center' }}>
            <img
              src={icon.url}
              alt={icon.displayName}
              title={icon.displayName}
              style={{ width: '50px', height: '50px' }}
            />
            <p style={{ fontSize: '12px', marginTop: '5px' }}>{icon.displayName}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default IconLibrary;
```

### 4. Vue 组件

```vue
<template>
  <div>
    <input
      v-model="searchTerm"
      type="text"
      placeholder="搜索图标..."
      style="padding: 10px; width: 300px; margin-bottom: 20px;"
    />
    
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); gap: 20px;">
      <div
        v-for="icon in filteredIcons"
        :key="icon.name"
        style="text-align: center;"
      >
        <img
          :src="icon.url"
          :alt="icon.displayName"
          :title="icon.displayName"
          style="width: 50px; height: 50px;"
        />
        <p style="font-size: 12px; margin-top: 5px;">{{ icon.displayName }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      icons: [],
      searchTerm: ''
    };
  },
  computed: {
    filteredIcons() {
      const term = this.searchTerm.toLowerCase();
      return this.icons.filter(icon =>
        icon.name.toLowerCase().includes(term) ||
        icon.displayName.toLowerCase().includes(term)
      );
    }
  },
  mounted() {
    fetch('https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json')
      .then(res => res.json())
      .then(data => {
        this.icons = data.icons;
      });
  }
};
</script>
```

### 5. 直接使用图标 URL

如果已知图标名称，可以直接构建 URL：

```html
<!-- 直接使用 CDN URL -->
<img src="https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/png/docker.png" alt="Docker" />

<!-- 或者使用 SVG（如果存在） -->
<img src="https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/svg/docker.svg" alt="Docker" />
```

### 6. CSS 中使用

```css
.icon-docker {
  background-image: url('https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/png/docker.png');
  background-size: contain;
  background-repeat: no-repeat;
  width: 50px;
  height: 50px;
}
```

### 7. 在 Homer Dashboard 中使用

```yaml
services:
  - name: "Docker"
    logo: "https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/png/docker.png"
    url: "https://docker.example.com"
  
  - name: "GitHub"
    logo: "https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/png/github.png"
    url: "https://github.com"
```

## 🔍 实用工具函数

### 完整的图标库工具类

```javascript
class IconLibrary {
  constructor(jsonUrl) {
    this.jsonUrl = jsonUrl;
    this.library = null;
  }

  async load() {
    if (!this.library) {
      const response = await fetch(this.jsonUrl);
      this.library = await response.json();
    }
    return this.library;
  }

  async getIcon(name) {
    await this.load();
    return this.library.icons.find(icon => icon.name === name);
  }

  async search(keyword) {
    await this.load();
    const term = keyword.toLowerCase();
    return this.library.icons.filter(icon =>
      icon.name.toLowerCase().includes(term) ||
      icon.displayName.toLowerCase().includes(term)
    );
  }

  async getIconUrl(name) {
    const icon = await this.getIcon(name);
    return icon ? icon.url : null;
  }

  async getIconsByFormat(format) {
    await this.load();
    return this.library.icons.filter(icon => icon.formats.includes(format));
  }

  async getStatistics() {
    await this.load();
    return this.library.statistics;
  }
}

// 使用示例
const iconLib = new IconLibrary('https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json');

// 获取图标
iconLib.getIcon('docker').then(icon => {
  console.log('Docker 图标:', icon);
});

// 搜索图标
iconLib.search('linux').then(icons => {
  console.log('Linux 相关图标:', icons);
});

// 获取图标 URL
iconLib.getIconUrl('github').then(url => {
  console.log('GitHub 图标 URL:', url);
});
```

## 📊 统计信息

图标库包含：
- **总图标数**: 572 个
- **PNG 格式**: 572 个
- **SVG 格式**: 250 个
- **仅 PNG**: 332 个
- **双格式**: 240 个

## 🔗 相关链接

- **GitHub 仓库**: https://github.com/Lsimply/icons
- **CDN 基础 URL**: https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/
- **JSON 文件**: https://cdn.jsdelivr.net/gh/lsimply/icons@refs/heads/main/icons.json

## 💡 提示

1. **缓存**: 建议在应用中缓存 JSON 文件，避免频繁请求
2. **错误处理**: 使用图标前检查图标是否存在
3. **性能优化**: 对于大量图标展示，考虑使用虚拟滚动
4. **格式选择**: 优先使用 SVG 格式（如果可用），以获得更好的缩放效果

## 📝 示例项目

查看完整示例，请访问 GitHub 仓库的 `icons` 目录。
