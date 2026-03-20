#!/usr/bin/env node
/**
 * OKR Progress Tracker
 * Generates progress charts and statistics from heartbeat data
 */

const fs = require('fs');
const path = require('path');

function parseArgs() {
    const args = process.argv.slice(2);
    const config = {
        input: './data/heartbeats.json',
        output: './output/okr-progress.md'
    };
    
    for (let i = 0; i < args.length; i++) {
        if (args[i] === '--input' || args[i] === '-i') config.input = args[++i];
        if (args[i] === '--output' || args[i] === '-o') config.output = args[++i];
    }
    
    return config;
}

function calculateOKRProgress(heartbeats) {
    const progress = {};
    const modeCounts = { manager: 0, executor: 0, reviewer: 0 };
    
    heartbeats.forEach(hb => {
        // Count modes
        if (modeCounts[hb.mode] !== undefined) {
            modeCounts[hb.mode]++;
        }
        
        // Track task completion
        if (hb.output && hb.output.includes('✅')) {
            progress.completed = (progress.completed || 0) + 1;
        }
    });
    
    return {
        totalHeartbeats: heartbeats.length,
        modeDistribution: modeCounts,
        completedTasks: progress.completed || 0,
        efficiency: heartbeats.length > 0 
            ? Math.round((progress.completed || 0) / heartbeats.length * 100) 
            : 0
    };
}

function generateProgressBar(current, target, width = 20) {
    const filled = Math.round((current / target) * width);
    const empty = width - filled;
    return '█'.repeat(filled) + '░'.repeat(empty);
}

function generateReport(data, config) {
    const stats = calculateOKRProgress(data.heartbeats || []);
    const okrs = data.okrs?.key_results || {};
    
    let report = `# OKR Progress Report\n\n`;
    report += `**Generated:** ${new Date().toISOString()}\n\n`;
    report += `## Objective\n\n${data.okrs?.objective || 'N/A'}\n\n`;
    report += `## Key Results\n\n`;
    
    for (const [kr, info] of Object.entries(okrs)) {
        const bar = generateProgressBar(info.current, info.target);
        const pct = Math.round(info.current / info.target * 100);
        report += `### ${kr}: ${info.current}/${info.target} ${info.unit} (${pct}%)\n\n`;
        report += `\`${bar}\`\n\n`;
    }
    
    report += `## Activity Statistics\n\n`;
    report += `- **Total Heartbeats:** ${stats.totalHeartbeats}\n`;
    report += `- **Completed Tasks:** ${stats.completedTasks}\n`;
    report += `- **Efficiency:** ${stats.efficiency}%\n\n`;
    
    report += `### Mode Distribution\n\n`;
    report += `- 🎯 Manager: ${stats.modeDistribution.manager}\n`;
    report += `- 🔨 Executor: ${stats.modeDistribution.executor}\n`;
    report += `- 📋 Reviewer: ${stats.modeDistribution.reviewer}\n`;
    
    return report;
}

function main() {
    const config = parseArgs();
    
    if (!fs.existsSync(config.input)) {
        console.error(`Error: Input file not found: ${config.input}`);
        process.exit(1);
    }
    
    const data = JSON.parse(fs.readFileSync(config.input, 'utf8'));
    const report = generateReport(data, config);
    
    const outputDir = path.dirname(config.output);
    if (outputDir && !fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }
    
    fs.writeFileSync(config.output, report);
    console.log(`✓ OKR progress report generated: ${config.output}`);
}

main();
