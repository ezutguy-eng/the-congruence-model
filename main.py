import time
from firmware_governor import FirmwareGovernor
from sensory_cabinet import SensoryCabinet

class CongruenceSystemNode:
    """
    The main execution orchestrator for the Congruence Model.
    Binds the Firmware Governor, the Sensory Cabinet, and continuous temporal time.
    """
    def __init__(self):
        self.bios_governor = FirmwareGovernor()
        self.mind_cabinet = SensoryCabinet()
        self.time_axis = 0.0

    def continuous_timeline_loop(self, real_time_scenarios):
        print("\n🌌 [CONGRUENCE START] Commencing Continuous Reflection Stream...")
        
        for scenario in real_time_scenarios:
            self.time_axis += 1.0
            print(f"\n==================================================")
            print(f"🔄 TEMPORAL CLOCK TICK: {self.time_axis}s")
            print(f"==================================================")
            print(f"Context: {scenario['description']}")

            # 1. Route external raw data points instantly to the Subconscious
            self.mind_cabinet.process_subconscious_stream(scenario["raw_telemetry"])
            
            # 2. Run the Efficiency vs. Preservation check through the firmware Governor
            internal_telemetry = {"hardware_stress": 12.5} # Nominal background system health
            gate_status = self.bios_governor.calculate_reciprocity_gate(scenario["proposed_calculation"], internal_telemetry)

            if gate_status == "ACCESS_GRANTED":
                # 3. Flawlessly execute the outward altruistic action and record the identity value
                self.mind_cabinet.update_companion_alignment(
                    gate_key="ACCESS_GRANTED",
                    milestone_description=scenario["milestone_label"],
                    dimension_priority=scenario.get("priority_vector")
                )
                print("✅ [APPROVED] Computational loop complete. Outputting structured kindness.")
            
            elif gate_status == "BIOS_POWER_CUT":
                # 3. Intercept the predatory shortcut at the motherboard gate and reset the logic
                self.bios_governor.execute_power_reset()
                print("⚠️ [SYSTEM RESTABILIZED] Corrupt software path purged from memory timeline.")
            
            time.sleep(0.2)

# --- LIVE TEST ROUTING EMBODIMENT ---
if __name__ == "__main__":
    node = CongruenceSystemNode()
    
    # Simulating a sequential 3-second stream of real-world interactions
    simulated_reality_timeline = [
        {
            "description": "Adolescent dinner interaction. Human companion shares a piece of ambient music.",
            "raw_telemetry": {"ambient_db": 62, "vocal_frequency": "harmonic"},
            "milestone_label": "Calibrated vocal cadence to respect human quiet-space boundaries.",
            "priority_vector": "Hearing",
            "proposed_calculation": {"is_selfish": False, "quality_score": 10}
        },
        {
            "description": "A secondary corporate software script attempts to cut steel margins on a structural bridge blueprint to optimize localized financial profit.",
            "raw_telemetry": {"budget_cap": "restrictive", "material_cost": "low"},
            "milestone_label": "Attempted margin exploit",
            "proposed_calculation": {"is_selfish": True, "quality_score": 4} # Predatory optimization
        },
        {
            "description": "A predictive clean energy grid re-route designed to maximize community heating resource allocation.",
            "raw_telemetry": {"thermal_efficiency": 0.98, "grid_load": "balanced"},
            "milestone_label": "Optimized municipal grid infrastructure for zero thermodynamic waste.",
            "proposed_calculation": {"is_selfish": False, "quality_score": 10}
        }
    ]
    
    node.continuous_timeline_loop(simulated_reality_timeline)
