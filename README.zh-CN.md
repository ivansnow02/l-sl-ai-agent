# 短链接 ReAct Agent

[English](./README.md)

## 快速开始

假设您已经[安装了 LangGraph Studio](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file#download)，请按照以下步骤进行设置：

1. 创建一个 `.env` 文件。

```bash
cp .env.example .env
```

2. 在 `.env` 文件中定义所需的 API 密钥。

主要使用的[搜索工具](./src/react_agent/tools.py)是 [Tavily](https://tavily.com/)。在[此处](https://app.tavily.com/sign-in)创建一个 API 密钥。

<!--
设置说明由 `langgraph template lock` 自动生成。请勿手动编辑。
-->

### 设置模型

`model` 的默认值如下所示：
可以在 [GitHub Marketplace](https://github.com/marketplace/models) 获取模型。

```yaml
model: gpt-4o-mini
```

### 启动 ReAct Agent

```bash
langgraph up
```
