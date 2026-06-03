
import uuid
from datetime import datetime

class NexusCore:
    def __init__(self, platform_name="Nexus"):
        self.platform_name = platform_name
        self.active_broadcasts = {} 
        self.leaderboards = {} 
        print(f"--- {self.platform_name} Engine Initialized ---")

    def create_broadcast(self, host_id, broadcast_type):
        broadcast_id = str(uuid.uuid4())[:8]
        self.active_broadcasts[broadcast_id] = {
            "host_id": host_id,
            "type": broadcast_type,
            "guests": [],
            "status": "live"
        }
        return broadcast_id

    def handle_interaction(self, broadcast_id, user_id, action_type, payload=None):
        if broadcast_id not in self.active_broadcasts: return "Broadcast not found"
        return {"user": user_id, "action": action_type}

    def update_leaderboard(self, broadcast_id, user_id, points):
        if broadcast_id not in self.leaderboards: self.leaderboards[broadcast_id] = {}
        self.leaderboards[broadcast_id][user_id] = self.leaderboards[broadcast_id].get(user_id, 0) + points
        return sorted(self.leaderboards[broadcast_id].items(), key=lambda x: x[1], reverse=True)

    def add_guest_to_broadcast(self, broadcast_id, guest_id):
        if broadcast_id in self.active_broadcasts:
            self.active_broadcasts[broadcast_id]["guests"].append(guest_id)
            return True
        return False
