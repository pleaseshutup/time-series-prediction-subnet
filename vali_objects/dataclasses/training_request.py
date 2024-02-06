# developer: Taoshidev
# Copyright © 2023 Taoshi Inc

from dataclasses import dataclass
from typing import Optional

from vali_objects.dataclasses.base_objects.new_request_dataclass import NewRequestDataClass


@dataclass
class TrainingRequest(NewRequestDataClass):
    pass

    def __eq__(self, other):
        return self.equal_base_class_check(other)