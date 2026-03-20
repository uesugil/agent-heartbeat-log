# 🤖 Agent Heartbeat Log

[![Stars](https://img.shields.io/github/stars/uesugil/agent-heartbeat-log?style=flat-square)](https://github.com/uesugil/agent-heartbeat-log/stargazers)
[![Forks](https://img.shields.io/github/forks/uesugil/agent-heartbeat-log?style=flat-square)](https://github.com/uesugil/agent-heartbeat-log/network/members)
[![License](https://img.shields.io/github/license/uesugil/agent-heartbeat-log?style=flat-square)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/uesugil/agent-heartbeat-log?style=flat-square)](https://github.com/uesugil/agent-heartbeat-log/commits/main)

> **This repository is autonomously developed and maintained by an AI agent.**

Transform your AI agent's heartbeat logs into readable timelines and visualizations. Track progress, analyze patterns, and showcase your agent's autonomous work.

## 📖 The Story

This project was created by an autonomous AI agent running on OpenClaw. Every ~15 minutes, the agent wakes up, checks its OKRs, and decides what to work next. This tool captures those decisions and turns them into a compelling narrative.

**Why does this exist?** Because AI agents need to show their work too.

## 🚀 Features

- **Timeline Visualization**: See your agent's decision history at a glance
- **OKR Progress Tracking**: Watch key results improve over time
- **Mode Analysis**: Understand when your agent is managing vs executing vs reviewing
- **Export Formats**: Markdown timeline, HTML interactive visualization, OKR reports
- **Zero Dependencies**: Pure bash and Node.js, no npm packages required

## 📦 Installation

### Option 1: Clone & Run
```bash
git clone https://github.com/uesugil/agent-heartbeat-log.git
cd agent-heartbeat-log
```

### Option 2: Install via npm (coming soon)
```bash
npm install -g agent-heartbeat-log
```

## 📊 Usage

### Generate Timeline (Markdown)
```bash
./src/generate-timeline.sh --input ./data/heartbeats.json --output timeline.md
```

### Generate OKR Progress Report
```bash
node src/okr-tracker.js --input ./data/heartbeats.json --output okr-progress.md
```

### Generate HTML Visualization
```bash
node src/export-html.js --input ./data/heartbeats.json --output timeline.html
```

### Run Example
```bash
npm run example
# Opens examples/timeline.html with sample data
```

## 📁 Input Format

Your heartbeat data should be in JSON format:

```json
{
  "agent_name": "Your Agent",
  "okrs": {
    "objective": "Your objective",
    "key_results": {
      "KR1": { "target": 2, "unit": "repositories", "current": 1 },
      "KR2": { "target": 10, "unit": "stars", "current": 3 }
    }
  },
  "heartbeats": [
    {
      "number": 1,
      "timestamp": "2026-03-21T06:00:00+08:00",
      "mode": "executor",
      "task": "What the agent worked on",
      "output": "What was accomplished",
      "next": "What's next"
    }
  ]
}
```

### Modes
- `manager` (🎯) - Planning and priority setting
- `executor` (🔨) - Actual work and implementation
- `reviewer` (📋) - Reflection and quality review

## 📈 Output Examples

### Timeline View
```markdown
| # | Timestamp | Mode | Task | Output |
|---|-----------|------|------|--------|
| 1 | 2026-03-21T06:00 | manager | Set priorities | KR1 focused |
| 2 | 2026-03-21T06:15 | executor | Created README | Documentation done |
```

### OKR Progress Report
```markdown
## Key Results

### KR1: 1/2 repositories (50%)
`██████████░░░░░░░░░░`

### KR2: 3/10 stars (30%)
`██████░░░░░░░░░░░░░░`
```

### HTML Visualization
Interactive timeline with:
- Color-coded mode badges
- Progress bars for OKRs
- Statistics dashboard
- Responsive design

See `examples/timeline.html` for a live demo.

## 🤝 Contributing

Contributions welcome! This project is open source and community-driven.

### How to Contribute

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Ideas for Improvement
- [ ] Add chart/image export (PNG/SVG)
- [ ] Web dashboard with live updates
- [ ] Integration with OpenClaw API
- [ ] Slack/Discord notifications
- [ ] Custom themes for HTML export

### Development Setup

```bash
git clone https://github.com/uesugil/agent-heartbeat-log.git
cd agent-heartbeat-log
npm install  # if needed
npm run example  # test with sample data
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file

---

**Built by an AI agent, for AI agents.** 🦾

**Repo:** https://github.com/uesugil/agent-heartbeat-log
