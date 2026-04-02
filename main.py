#!/usr/bin/env python3
"""Top network interfaces monitor CLI entry point."""

from __future__ import annotations

import argparse
import json
import sys

from monitor.calculator import sample_interface_rates
from monitor.formatter import format_table, to_json_payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show the top network interfaces by real-time traffic rate."
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of interfaces to display (default: 5).",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=2.0,
        help="Sampling interval in seconds (default: 2).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON instead of a table.",
    )
    args = parser.parse_args()
    if args.top <= 0:
        parser.error("--top must be greater than 0")
    if args.interval <= 0:
        parser.error("--interval must be greater than 0")
    return args


def main() -> int:
    args = parse_args()
    rates = sample_interface_rates(args.interval)
    top_rates = rates[: args.top]

    if args.json:
        json.dump(to_json_payload(top_rates, args.top, args.interval), sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(format_table(top_rates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
