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
```

### 3. 設定 OpenAI API 金鑰

```bash
export OPENAI_API_KEY="你的_OpenAI_API_金鑰"
```

## 執行範例

```bash
source venv/bin/activate
export OPENAI_API_KEY="你的_API_金鑰"
python venv/Helloworld.py
```

## 檔案結構

```
AutoGen/
├── venv/                # 虛擬環境
│   └── Helloworld.py   # Hello World 範例
├── .gitignore          # Git 忽略檔案
└── README.md           # 專案說明
```

## 注意事項

- 請確保設定正確的 OpenAI API 金鑰
- 使用虛擬環境來管理 Python 套件
- venv/ 目錄已被 .gitignore 忽略，不會被提交到版本控制
