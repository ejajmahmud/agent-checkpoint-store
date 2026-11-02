"""Command line interface for agent-checkpoint-store."""
from .store import CheckpointStore

def main():
    store = CheckpointStore()
    store.set_state("step", 1)
    store.create_checkpoint("cp1")
    store.set_state("step", 2)
    print("Current state step:", store.get_state("step"))
    store.rollback("cp1")
    print("Rolled back step:", store.get_state("step"))

if __name__ == "__main__":
    main()
