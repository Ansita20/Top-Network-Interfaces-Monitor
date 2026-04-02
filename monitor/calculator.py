"""Compute per-interface transfer rates from sampled counters."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import List

from monitor.collector import collect_counters


@dataclass(frozen=True)
class InterfaceRate:
    name: str
    rx_bps: float
    tx_bps: float

    @property
    def total_bps(self) -> float:
        return self.rx_bps + self.tx_bps


def sample_interface_rates(interval: float) -> List[InterfaceRate]:
    start = collect_counters()
    time.sleep(interval)
    end = collect_counters()

    names = sorted(set(start) | set(end))
    rates: List[InterfaceRate] = []
    for name in names:
        start_counters = start.get(name)
        end_counters = end.get(name)
        if start_counters is None or end_counters is None:
            continue
        rx_bps = max(0.0, (end_counters.bytes_recv - start_counters.bytes_recv) / interval)
        tx_bps = max(0.0, (end_counters.bytes_sent - start_counters.bytes_sent) / interval)
        rates.append(InterfaceRate(name=name, rx_bps=rx_bps, tx_bps=tx_bps))
    rates.sort(key=lambda item: (-item.total_bps, item.name))
    return rates