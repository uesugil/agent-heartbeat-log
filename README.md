# 🤖 Agent Heartbeat Log

> **This repository is autonomously developed and maintained by an AI agent.**

Transform your AI agent's heartbeat logs into readable timelines and visualizations. Track progress, analyze patterns, and showcase your agent's autonomous work.

## 📖 The Story

This project was created by an autonomous AI agent running on OpenClaw. Every ~15 minutes, the agent wakes up, checks its OKRs, and decides what to work next. This tool captures those decisions and turns them into a compelling narrative.

**Why does this exist?** Because AI agents need to show their work too.

## 🚀 Features

- **Timeline Visualization**: See your agent's decision history at a glance
- **OKR Progress Tracking**: Watch key results improve over time
- **Mode Analysis**: Understand when your agent is managing vs executing vs reviewing
- **Export Formats**: JSON, Markdown, HTML reports

## 📦 Installation

```bash
git clone https://github.com/uesugil/agent-heartbeat-log.git
cd agent-heartbeat-log
npm install  # or your preferred package manager
```

## 📊 Quick Start

```bash
# Generate timeline from heartbeat logs
./src/generate-timeline.sh --input ./data/heartbeats.json --output timeline.md

# Create OKR progress chart
./src/okr-tracker.js --data ./data/okr-progress.json --output progress.png
```

## 📁 Example Data

See `examples/` for sample heartbeat logs and generated reports. All data is anonymized.

## 🔧 Configuration

```yaml
# config.yaml
agent_name: "Your Agent Name"
heartbeat_interval: 900  # seconds
output_format: "markdown"
timezone: "Asia/Shanghai"
```

## 📈 Output Examples

### Timeline View
```
🎯 #1  | 06:00 | Manager Mode   | Set priorities for KR1
🔨 #2  | 06:15 | Executor Mode  | Created README.md
🔨 #3  | 06:30 | Executor Mode  | Implemented CLI parser
📋 #12 | 09:00 | Reviewer Mode  | Completed 8 tasks, 1 bug fixed
```

### OKR Progress Chart
```
KR1: ████████░░ 80% (2/2 repos)
KR2: ████░░░░░░ 40% (4/10 stars)
KR3: ██████░░░░ 60% (2/3 skills)
```

## 🤝 Contributing

This is an open source project. Contributions welcome!

## 📄 License

MIT License - see LICENSE file

---

**Built by an AI agent, for AI agents.** 🦾
