class ComaFailsafe:
    def validate_chain(self, memory_engine):
        memory = memory_engine.read_recent_memories(5)
        return all("timestamp" in m for m in memory)

    def enter_coma_mode(self):
        print("Entering coma mode due to chain validation failure.")