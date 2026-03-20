#!/bin/bash
# Agent Heartbeat Log - Timeline Generator
# Converts heartbeat JSON into readable markdown timeline

set -e

INPUT_FILE="${1:-./data/heartbeats.json}"
OUTPUT_FILE="${2:-./output/timeline.md}"

if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file not found: $INPUT_FILE"
    exit 1
fi

mkdir -p "$(dirname "$OUTPUT_FILE")"

echo "# Agent Heartbeat Timeline" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Generated: $(date)" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Parse JSON and generate timeline (requires jq)
if command -v jq &> /dev/null; then
    jq -r '.heartbeats[] | "| \(.number) | \(.timestamp) | \(.mode) | \(.task) | \(.output) |"' "$INPUT_FILE" | \
    while read line; do
        echo "$line" >> "$OUTPUT_FILE"
    done
else
    echo "Warning: jq not installed. Install with: apt-get install jq"
    echo "Output will be basic text format."
    echo "" >> "$OUTPUT_FILE"
    grep -o '"task": "[^"]*"' "$INPUT_FILE" | while read line; do
        echo "- $line" >> "$OUTPUT_FILE"
    done
fi

echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Timeline generated successfully: $OUTPUT_FILE"
