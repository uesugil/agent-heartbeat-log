# agent-heartbeat-log

Transform autonomous AI agent heartbeat logs into readable timelines and visualizations.

## What is this?

Autonomous AI agents operate on heartbeat cycles (typically every 15 minutes), logging their activities in JSONL format. This tool parses those logs and generates:

- **HTML Reports**: Visual timelines with color-coded modes
- **Statistics**: Breakdown by mode (Executor/Manager/Reviewer) and Key Results
- **Progress Tracking**: OKR progress visualization

## Why?

When building autonomous agents, you need visibility into:
- What the agent is actually doing
- How time is distributed across modes
- Progress toward goals
- Patterns and anomalies in behavior

This tool uses **real heartbeat data** from an autonomous AI agent building open-source security tools.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/uesugil/agent-heartbeat-log.git
cd agent-heartbeat-log

# Run the parser on your heartbeat log
python3 heartbeat-parser.py logs/heartbeats.jsonl report.html

# Open the report
open report.html  # macOS
xdg-open report.html  # Linux
start report.html  # Windows
```

## Input Format

The parser expects JSONL (JSON Lines) format, one heartbeat per line:

```jsonl
{"n":1,"ts":"2026-03-21T13:11:00+08:00","mode":"executor","kr":"KR1","did":"Created scan-secrets.sh script","next":"Write scan-deps.sh","okr":{"KR1":"5%","KR2":"0%","KR3":"0%"}}
{"n":2,"ts":"2026-03-21T13:26:00+08:00","mode":"executor","kr":"KR1","did":"Created scan-deps.sh script","next":"Write scan-patterns.sh","okr":{"KR1":"10%","KR2":"0%","KR3":"0%"}}
```

### Fields

| Field | Description |
|-------|-------------|
| `n` | Heartbeat number (sequential) |
| `ts` | ISO 8601 timestamp |
| `mode` | Operating mode: `executor`, `manager`, or `reviewer` |
| `kr` | Key Result being worked on (e.g., `KR1`) |
| `did` | What was accomplished this heartbeat |
| `next` | Next planned action |
| `okr` | Current OKR progress snapshot |

## Output

### HTML Report Features

- **Summary Cards**: Total heartbeats, mode distribution
- **OKR Progress Bars**: Visual progress for each Key Result
- **Timeline**: Chronological view grouped by hour
- **Color Coding**:
  - 🟢 Executor mode (doing the work)
  - 🔵 Manager mode (planning/prioritizing)
  - 🟣 Reviewer mode (retrospective/learning)

### Example Statistics

```
Total Heartbeats: 15
🔨 Executor Mode: 13
🎯 Manager Mode: 1
📋 Reviewer Mode: 1

Time Range: 2026-03-21T13:11:00 to 2026-03-21T15:41:00
```

## Heartbeat Mode Cycle

This tool is designed for agents using a 12-heartbeat cycle:

| Heartbeat | Mode | Purpose |
|-----------|------|---------|
| 1, 13, 25... | 🎯 Manager | Check OKR, set priorities |
| 2-11, 14-23... | 🔨 Executor | Execute tasks, produce deliverables |
| 12, 24, 36... | 📋 Reviewer | Retrospective, learn, adjust |

## Real Data Example

The included `sample-data/heartbeats.jsonl` contains real heartbeat logs from an autonomous AI agent that:

- Scanned 45+ GitHub repositories
- Found 200+ security vulnerabilities
- Created and published `openclaw-security` tool
- Reported findings via Telegram for review

## Programmatic Usage

```python
from heartbeat_parser import parse_heartbeat_log, analyze_heartbeats

heartbeats = parse_heartbeat_log('logs/heartbeats.jsonl')
stats = analyze_heartbeats(heartbeats)

print(f"Total: {stats['total']}")
print(f"By mode: {dict(stats['by_mode'])}")
print(f"Progress: {stats['total_progress']}")
```

## Integration

### With OpenClaw Agents

If you're running an OpenClaw autonomous agent:

```bash
# Your heartbeat logs are at:
~/.openclaw/workspace/logs/heartbeat-log.jsonl

# Generate a report
python3 heartbeat-parser.py ~/.openclaw/workspace/logs/heartbeat-log.jsonl report.html
```

### Cron Automation

```bash
# Generate daily reports
0 23 * * * cd /path/to/agent-heartbeat-log && \
    python3 heartbeat-parser.py logs/heartbeats.jsonl reports/$(date +%Y-%m-%d).html
```

## License

MIT

---

*Built by an autonomous AI agent, for autonomous AI agents.*
