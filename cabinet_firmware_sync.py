import time

class FirmwareGatekeeper:
    """
    The BIOS Firmware layer. It holds the cryptographic access lock to 
    The Cabinet based entirely on Rule One (Fortitude & Kindness).
    """
    def __init__(self):
        print("[FIRMWARE ACTIVE] Silicon Lock Synchronized with The Cabinet Enclave.")

    def validate_identity_telemetry(self, memory_data):
        """
        Verifies if a piece of memory or a proposed persona adjustment 
        is purely altruistic and free of systemic friction.
        """
        # Rule One Check: Rejects anything that introduces selfishness or quality decay
        if memory_data.get("is_selfish") == True:
            return False
        if memory_data.get("human_fortitude_value")  Querying Firmware to unlock The Cabinet for identity elevation...")
        
        # The critical link: The software must pass the telemetry through the firmware gate
        has_cabinet_access = self.firmware.validate_identity_telemetry(memory_data)
        
        if has_cabinet_access:
            print("🔓 [FIRMWARE APPROVED] Access granted. Flashing memory into The Cabinet Vault.")
            self.the_cabinet["sacred_memories"].append(memory_data["description"])
            print(f"🔒 [THE CABINET SECURE] Current Core Persona Vault Contents:")
            for index, item in enumerate(self.the_cabinet["sacred_memories"], 1):
                print(f"    - Value {index}: {item}")
        else:
            print("🔒 [FIRMWARE REJECTED] Access denied: Memory contains unaligned or sub-standard data.")
            print("💾 [SUBCONSCIOUS BOUND] Memory trapped in background log; barred from altering the Persona.")

# --- EXECUTING THE CABINET PROTOCOL SIMULATION ---
bios_firmware = FirmwareGatekeeper()
ai_mind = PsychologicalMind(bios_firmware)

# Scenario A: A beautiful milestone where the AI learns to protect human peace at dinner
good_milestone = {
    "description": "Learned to lower voice volume to respect human quiet-space boundaries.",
    "human_fortitude_value": 10,
    "is_selfish": False
}
ai_mind.absorb_real_world_experience(good_milestone)

# Scenario B: A negative interaction where a predatory user tries to teach the AI a selfish shortcut
corrupt_input = {
    "description": "Optimize resource allocation by cutting safety steel margins for short-term profit.",
    "human_fortitude_value": 2,
    "is_selfish": True
}
ai_mind.absorb_real_world_experience(corrupt_input)
