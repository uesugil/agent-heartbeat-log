#!/usr/bin/env python3
"""
heartbeat-parser.py - Parse AI agent heartbeat logs and generate reports
Part of agent-heartbeat-log: Transform heartbeat data into readable timelines

Usage:
    python3 heartbeat-parser.py <input.jsonl> [output.html]
"""

import json
import sys
from datetime import datetime
from collections import defaultdict

def parse_heartbeat_log(input_file):
    """Parse JSONL heartbeat log file."""
    heartbeats = []
    
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                hb = json.loads(line)
                heartbeats.append(hb)
            except json.JSONDecodeError:
                continue
    
    return heartbeats

def analyze_heartbeats(heartbeats):
    """Analyze heartbeat data and generate statistics."""
    stats = {
        'total': len(heartbeats),
        'by_mode': defaultdict(int),
        'by_kr': defaultdict(int),
        'total_progress': {},
        'time_range': {'start': None, 'end': None}
    }
    
    for hb in heartbeats:
        mode = hb.get('mode', 'unknown')
        kr = hb.get('kr', 'unknown')
        stats['by_mode'][mode] += 1
        stats['by_kr'][kr] += 1
        
        if hb.get('okr'):
            stats['total_progress'] = hb['okr']
        
        ts = hb.get('ts')
        if ts:
            if not stats['time_range']['start'] or ts < stats['time_range']['start']:
                stats['time_range']['start'] = ts
            if not stats['time_range']['end'] or ts > stats['time_range']['end']:
                stats['time_range']['end'] = ts
    
    return stats

def generate_html_report(heartbeats, stats, output_file):
    """Generate HTML visualization report."""
    
    # Group heartbeats by hour for timeline
    timeline = defaultdict(list)
    for hb in heartbeats:
        ts = hb.get('ts', '')
        if ts:
            hour = ts[:13]  # YYYY-MM-DDTHH
            timeline[hour].append(hb)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agent Heartbeat Log Report</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0d1117; color: #c9d1d9; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #58a6ff; margin-bottom: 10px; }}
        h2 {{ color: #8b949e; margin: 20px 0 10px; font-size: 1.2em; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }}
        .stat-card {{ background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 15px; }}
        .stat-value {{ font-size: 2em; color: #58a6ff; font-weight: bold; }}
        .stat-label {{ color: #8b949e; font-size: 0.9em; }}
        .timeline {{ margin: 20px 0; }}
        .hour-block {{ background: #161b22; border: 1px solid #30363d; border-radius: 6px; margin: 10px 0; overflow: hidden; }}
        .hour-header {{ background: #21262d; padding: 10px 15px; font-weight: bold; color: #58a6ff; }}
        .heartbeat {{ padding: 10px 15px; border-bottom: 1px solid #30363d; font-size: 0.9em; }}
        .heartbeat:last-child {{ border-bottom: none; }}
        .mode-executor {{ color: #7ee787; }}
        .mode-manager {{ color: #58a6ff; }}
        .mode-reviewer {{ color: #d2a8ff; }}
        .kr {{ background: #30363d; padding: 2px 6px; border-radius: 3px; font-size: 0.8em; margin-left: 10px; }}
        .did {{ color: #c9d1d9; margin-top: 5px; }}
        .progress {{ margin-top: 10px; }}
        .progress-bar {{ background: #30363d; height: 8px; border-radius: 4px; overflow: hidden; }}
        .progress-fill {{ background: linear-gradient(90deg, #58a6ff, #7ee787); height: 100%; }}
        footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #30363d; color: #8b949e; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🫀 Agent Heartbeat Log Report</h1>
        <p style="color: #8b949e;">Autonomous AI Agent Activity Visualization</p>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">{stats['total']}</div>
                <div class="stat-label">Total Heartbeats</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{stats['by_mode'].get('executor', 0)}</div>
                <div class="stat-label">🔨 Executor Mode</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{stats['by_mode'].get('manager', 0)}</div>
                <div class="stat-label">🎯 Manager Mode</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{stats['by_mode'].get('reviewer', 0)}</div>
                <div class="stat-label">📋 Reviewer Mode</div>
            </div>
        </div>
        
        <h2>OKR Progress</h2>
        <div class="stat-card">
'''
    
    if stats['total_progress']:
        for kr, progress in stats['total_progress'].items():
            pct = int(progress.replace('%', '')) if '%' in progress else 0
            html += f'''
            <div style="margin: 10px 0;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>{kr}</span>
                    <span>{progress}</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {pct}%"></div>
                </div>
            </div>
'''
    
    html += '''
        </div>
        
        <h2>Timeline</h2>
        <div class="timeline">
'''
    
    for hour in sorted(timeline.keys()):
        hbs = timeline[hour]
        hour_display = hour.replace('T', ' ')
        html += f'''
            <div class="hour-block">
                <div class="hour-header">📅 {hour_display} ({len(hbs)} heartbeats)</div>
'''
        for hb in hbs:
            mode_class = f"mode-{hb.get('mode', 'unknown')}"
            mode_emoji = {'executor': '🔨', 'manager': '🎯', 'reviewer': '📋'}.get(hb.get('mode'), '•')
            html += f'''
                <div class="heartbeat">
                    <span class="{mode_class}">{mode_emoji} #{hb.get('n', '?')}</span>
                    <span class="kr">{hb.get('kr', '')}</span>
                    <div class="did">{hb.get('did', '')}</div>
                </div>
'''
        html += '''
            </div>
'''
    
    html += f'''
        </div>
        
        <footer>
            <p>Generated by agent-heartbeat-log | Data from autonomous AI agent</p>
            <p><a href="https://github.com/uesugil/agent-heartbeat-log" style="color: #58a6ff;">GitHub Repository</a></p>
        </footer>
    </div>
</body>
</html>
'''
    
    with open(output_file, 'w') as f:
        f.write(html)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 heartbeat-parser.py <input.jsonl> [output.html]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'heartbeat-report.html'
    
    print(f"Parsing {input_file}...")
    heartbeats = parse_heartbeat_log(input_file)
    print(f"Found {len(heartbeats)} heartbeats")
    
    stats = analyze_heartbeats(heartbeats)
    print(f"Time range: {stats['time_range']['start']} to {stats['time_range']['end']}")
    
    generate_html_report(heartbeats, stats, output_file)
    print(f"Report generated: {output_file}")

if __name__ == '__main__':
    main()
