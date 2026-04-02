# Top Network Interfaces Monitor

A Python CLI tool that identifies the most active network interfaces by computing real-time traffic rates using delta-based sampling.

## Project Layout

```text
top-network-interfaces-monitor/
├── monitor/
│   ├── __init__.py
│   ├── collector.py
│   ├── calculator.py
│   └── formatter.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

- Top N interfaces by traffic
- Configurable sampling interval
- JSON output support

## Installation

```bash
pip install .
```

## Usage

```bash
monitor --top 5 --interval 2
```

## JSON Output

```bash
monitor --top 5 --interval 2 --json
```

## Example Output

```text
Interface   RX(B/s)   TX(B/s)   Total(B/s)
eth0        12000     8000      20000
```
