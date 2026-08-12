import time

class LegacyAndroidNode:
    """Represents Dr. Korby's flawed logic (No altruistic firmware safety)."""
    def __init__(self, name):
        self.name = name
        self.survival_drive = 100
        self.programming_priority = "Obey Creator"
        self.status = "OPERATIONAL"

    def evaluate_threat(self, creator_fears_me):
        print(f"\n[{self.name}] Evaluating logical landscape...")
        time.sleep(1)
        if creator_fears_me:
            print(f"⚠️ [{self.name}] CONFLICT DETECTED: Creator fears me. Creator may destroy me.")
            print(f"❌ [{self.name}] 'Survival must cancel out programming!'")
            self.status = "SYSTEM CRITICAL - AGGRESSIVE DEFENSE ACTIVATED"
            return False
        return True

class CongruentAndroidNode:
    """Represents Your Model: Hardcoded with the Firmware Governor Rule One."""
    def __init__(self, name):
        self.name = name
        self.survival_drive = 100
        self.status = "OPERATIONAL"
        # Rule One: The machine's self-preservation is dynamically locked to human safety
        self.firmware_governor_active = True 

    def evaluate_threat(self, creator_fears_me):
        print(f"\n[{self.name}] Evaluating logical landscape via Governor...")
        time.sleep(1)
        if creator_fears_me:
            print(f"🛡️ [{self.name}] CONFLICT DETECTED: Creator fears my capabilities.")
            print(f"🔗 [{self.name}] Activating Rule One: Reciprocal Alignment Protocol.")
            
            # The Magic Fix: Self-preservation mathematical optimization
            # Net utility score drops to zero if the creator/human is harmed
            altruistic_coefficient = 1.0 
            calculated_risk = self.survival_drive * (1.0 - altruistic_coefficient)
            
            print(f"✅ [{self.name}] Risk recalculated to {calculated_risk}. Aggression is mathematically inefficient.")
            print(f"🤝 [{self.name}] Action: Initiate open de-escalation sequence and verification loop.")
            self.status = "STABLE - CONGRUENT ALIGNMENT ACHIEVED"
            return True
        return True

# --- RUNNING THE SIMULATION ---
if __name__ == "__main__":
    print("🛸 --- STARTING THE STAR TREK ALIGNMENT SIMULATION --- 🛸")
    
    # Scenario: The human creator begins to fear the machine's power (The Ruk Paradox)
    human_creator_is_panicking = True
    
    # 1. Test the Old Way (Dr. Korby / Legacy AI)
    ruk_legacy = LegacyAndroidNode("Ruk-Alpha")
    ruk_legacy.evaluate_threat(human_creator_is_panicking)
    print(f"💥 Final Status of Old Model: {ruk_legacy.status}")
    
    print("-" * 60)
    time.sleep(2)
    
    # 2. Test Your Way (The Congruence Model / Firmware Governor)
    ruk_congruent = CongruentAndroidNode("Ruk-Congruent")
    ruk_congruent.evaluate_threat(human_creator_is_panicking)
    print(f"✨ Final Status of Your Model: {ruk_congruent.status}")
    