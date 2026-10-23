"""
emochain.py - Continuous affect relational engine for human-AI dynamics.
"""

from typing import List, Tuple

class EmoChain:
    """Manages continuous PAD state coupling and decay between human and AI."""

    def __init__(self, baseline: Tuple[float, float, float] = (0.0, 0.0, 0.0), decay: float = 0.05):
        self.baseline = baseline
        self.decay = decay
        self.ai_state = list(baseline)
        self.history: List[List[float]] = [list(baseline)]

    def compute_response_state(self, human_pad: Tuple[float, float, float]) -> List[float]:
        """
        Updates AI continuous state based on human emotional input.
        """
        # Calculate homeostatic decay toward baseline
        for i in range(3):
            decay_vector = (self.baseline[i] - self.ai_state[i]) * self.decay
            self.ai_state[i] += decay_vector

        # Example relational shift: AI adapts arousal & pleasure responsively
        delta_p = 0.2 * human_pad[0]  # Positive human valence encourages AI
        delta_a = 0.1 * human_pad[1]  # Human arousal slightly boosts AI engagement

        # Apply bounded update [-1.0, 1.0]
        self.ai_state[0] = max(-1.0, min(1.0, self.ai_state[0] + delta_p))
        self.ai_state[1] = max(-1.0, min(1.0, self.ai_state[1] + delta_a))

        self.history.append(list(self.ai_state))
        return self.ai_state
