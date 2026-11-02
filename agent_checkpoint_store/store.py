"""Transactional state checkpoint store."""
import copy
import time
from typing import Dict, Any, List, Optional

class CheckpointStore:
    def __init__(self):
        self._checkpoints: Dict[str, Dict[str, Any]] = {}
        self._history: List[str] = []
        self._current_state: Dict[str, Any] = {}

    def set_state(self, key: str, value: Any) -> None:
        self._current_state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        return self._current_state.get(key, default)

    def create_checkpoint(self, checkpoint_id: str) -> str:
        self._checkpoints[checkpoint_id] = {
            "timestamp": time.time(),
            "state": copy.deepcopy(self._current_state)
        }
        self._history.append(checkpoint_id)
        return checkpoint_id

    def rollback(self, checkpoint_id: str) -> bool:
        if checkpoint_id not in self._checkpoints:
            return False
        self._current_state = copy.deepcopy(self._checkpoints[checkpoint_id]["state"])
        return True

    def list_checkpoints(self) -> List[str]:
        return list(self._history)
