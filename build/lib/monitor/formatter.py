"""Format monitor results for the terminal and JSON output."""

from __future__ import annotations

from typing import Dict, Iterable, List

from monitor.calculator import InterfaceRate


def format_table(rows: Iterable[InterfaceRate]) -> str:
    header = ("Interface", "RX(B/s)", "TX(B/s)", "Total(B/s)")
    formatted_rows = [
        (
            row.name,
            f"{row.rx_bps:.0f}",
            f"{row.tx_bps:.0f}",
            f"{row.total_bps:.0f}",
        )
        for row in rows
    ]

    widths = [len(part) for part in header]
    for row in formatted_rows:
        widths = [max(width, len(cell)) for width, cell in zip(widths, row)]

    lines = [
        f"{header[0]:<{widths[0]}}   {header[1]:>{widths[1]}}   {header[2]:>{widths[2]}}   {header[3]:>{widths[3]}}"
    ]
    for row in formatted_rows:
        lines.append(
            f"{row[0]:<{widths[0]}}   {row[1]:>{widths[1]}}   {row[2]:>{widths[2]}}   {row[3]:>{widths[3]}}"
        )
    return "\n".join(lines)


def to_json_payload(rows: List[InterfaceRate], top: int, interval: float) -> Dict[str, object]:
    return {
        "top": top,
        "interval": interval,
        "interfaces": [
            {
                "name": row.name,
                "rx_bps": row.rx_bps,
                "tx_bps": row.tx_bps,
                "total_bps": row.total_bps,
            }
            for row in rows
        ],
    }