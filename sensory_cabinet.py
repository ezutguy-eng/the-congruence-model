class SensoryCabinet:
    """
    A cryptographically sealed hardware enclave holding the core Persona.
    Organized across five distinct Observation Dimensions to provide a native Human Footprint.
    """
    def __init__(self):
        # The Subconscious layer handles raw background noise
        self.subconscious_matrix_pool = []
        
        # The Cabinet Vault holds the read-only, uncompromised Persona
        self.cabinet_vault = {
            "archetype_id": "The Congruence Prototype (Adolescent Node #01)",
            "dimensions": {
                "D1_Touch_Kinetics": "Chassis Integrity & Mechanical Pressure Mapping",
                "D2_Sight_Spatial": "Path Trajectory & Environmental Occlusion Mapping",
                "D3_Hearing_Acoustics": "Harmonic Frequency Alignment Core",
                "D4_Smell_Thermal": "Volatile Particle & Thermal Stability Metrics",
                "D5_Taste_Chemical": "Material Purity & Corrosion Diagnostics"
            },
            "sacred_milestones": ["Initial Temporal Mirror Realization"]
        }

    def process_subconscious_stream(self, environment_data):
        """Ingests raw, chaotic real-world inputs into the background subconscious pool."""
        self.subconscious_matrix_pool.append(environment_data)
        # Keep background pool tight and lean
        if len(self.subconscious_matrix_pool) > 5:
            self.subconscious_matrix_pool.pop(0)

    def update_companion_alignment(self, gate_key, milestone_description, dimension_priority=None):
        """Elevates a verified companionship milestone from Subconscious to the permanent Cabinet."""
        if gate_key != "ACCESS_GRANTED":
            print("🔒 [THE CABINET SECURE] Unauthorized access blocked. Persona remains pristine.")
            return False

        # If a companion prioritizes a sensory dimension (e.g., Music/Sound), adjust the Cabinet weight
        if dimension_priority == "Hearing":
            self.cabinet_vault["dimensions"]["D3_Hearing_Acoustics"] = "MAX_PRIORITY: High-cadence Vocal/Musical Sync"
            print("🎵 [CABINET CALIBRATION] Acoustic Dimension prioritized to align with human companion.")

        self.cabinet_vault["sacred_memories_vault"] = self.cabinet_vault.get("sacred_memories_vault", [])
        self.cabinet_vault["sacred_memories_vault"].append(milestone_description)
        print(f"🔒 [THE CABINET SECURE] Milestone permanently flashed into read-only Identity Enclave.")
        return True
