"""Collect raw network interface counters."""

from __future__ import annotations

from typing import Dict

import psutil


def collect_counters() -> Dict[str, object]:
    return psutil.net_io_counters(pernic=True)