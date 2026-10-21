"""
EmoChain: Bidirectional User-to-Agent Affective State Alignment Module
Tracks and updates the emotional relationship state across interaction turns.
"""

from typing import Dict, Any, Tuple


class EmoChainState:
    """
    Manages the affective equilibrium between human input and machine output.
    Maps input emotion vectors to adaptive agent posture transitions.
    """

    def __init__(self, damping_factor: float = 0.8):
        self.damping_factor = damping_factor
        self.current_user_feel = "neutral"
        self.current_machine_feel = "empathetic_neutral"
        self.history = []

    def transition_matrix(self, user_feel: str) -> str:
        """Determines machine affective posture based on user feeling."""
        matrix = {
            "frustrated": "de_escalating_calm",
            "joyful": "enthusiastic_supportive",
            "anxious": "reassuring_grounded",
            "sad": "compassionate_attentive",
            "neutral": "empathetic_neutral",
        }
        return matrix.get(user_feel, "empathetic_neutral")

    def update_state(self, user_feel: str, confidence: float) -> Dict[str, Any]:
        """
        Updates the EmoChain state for the current interaction turn.
        
        Args:
            user_feel: Extracted sentiment label from user input.
            confidence: Extraction confidence score (0.0 to 1.0).
            
        Returns:
            Updated affective relationship state dictionary.
        """
        self.current_user_feel = user_feel
        self.current_machine_feel = self.transition_matrix(user_feel)
        
        turn_record = {
            "user_feel": self.current_user_feel,
            "confidence": confidence,
            "machine_feel": self.current_machine_feel,
            "effective_damping": self.damping_factor
        }
        self.history.append(turn_record)
        return turn_record


if __name__ == "__main__":
    chain = EmoChainState()
    state = chain.update_state("frustrated", 0.92)
    print("EmoChain State Update:", state)
