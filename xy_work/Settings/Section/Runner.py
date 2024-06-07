# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "Runner"
"""
  * @File    :   Runner.py
  * @Time    :   2023/04/24 15:30:01
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from pathlib import Path
from xy_settings.Section.Section import Section


class Runner(Section):
    path: Path | None = Path("../source/Runner/")

    # 表示Runner.py中的Runner类
    runner: str | None = "Runner.Runner"

    source_path: Path | None = Path("../source/")

    def get_name(self) -> str | None:
        return "xy_work_runner"

    def _load(self):
        self.path = self._fetch_path("path", self.path)
        self.runner = self._sync_data("runner", self.runner)
        super()._load()
