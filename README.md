# AutoGen 專案

這是一個使用 Microsoft AutoGen 框架的 AI 多代理人系統專案。

## 專案說明

AutoGen 是一個多代理人對話框架，讓多個 AI 代理人能夠協作解決複雜問題。

## 環境設定

### 1. 建立虛擬環境

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. 安裝相依套件

```bash
pip install -U autogenstudio
pip install -U autogen-agentchat autogen-ext[openai,web-surfer]
playwright install
```

### 3. 安裝 ffmpeg（處理多媒體檔案）

```bash
brew install ffmpeg
```

### 4. 設定 OpenAI API 金鑰

```bash
export OPENAI_API_KEY="你的_OpenAI_API_金鑰"
```

## 執行範例

### Hello World 範例

```bash
source venv/bin/activate
export OPENAI_API_KEY="你的_API_金鑰"
python venv/Helloworld.py
```

### 網頁瀏覽代理人

```bash
source venv/bin/activate
export OPENAI_API_KEY="你的_API_金鑰"
python venv/Webbrowsingagent.py
```

### 研究團隊系統（NEW！）

```bash
source venv/bin/activate
export OPENAI_API_KEY="你的_API_金鑰"
python ResearchTeam.py
```

## 檔案結構

```
AutoGen/
├── venv/                     # 虛擬環境
│   ├── Helloworld.py        # Hello World 範例
│   └── Webbrowsingagent.py  # 單一網頁瀏覽代理人
├── ResearchTeam.py          # 🆕 多代理人研究團隊系統
├── .gitignore               # Git 忽略檔案
└── README.md                # 專案說明
```

## 專案特色

### 🤖 多代理人協作系統

- **Researcher**: 專業研究員，負責網路搜尋和資料收集
- **Recorder**: 記錄員，負責彙整和分析研究資料
- **User Proxy**: 用戶代理，負責最終決策和互動

### 🔄 工作流程

1. **Researcher** 根據需求進行深度網路研究
2. **Recorder** 接收並整理研究資料，生成結構化報告
3. **User Proxy** 審核報告並決定下一步行動

### 🎯 使用場景

- 市場研究和競品分析
- 技術調研和文獻蒐集
- 商業情報收集
- 學術研究輔助

## 注意事項

- 請確保設定正確的 OpenAI API 金鑰
- 使用虛擬環境來管理 Python 套件
- venv/ 目錄已被 .gitignore 忽略，不會被提交到版本控制
- 需要安裝 Playwright 瀏覽器：`playwright install`
- 需要安裝 ffmpeg 來處理多媒體檔案
