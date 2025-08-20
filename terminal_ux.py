from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

# Set terminal to dark mode (black background)
print("\033[40m")

def display_header():
    """Display the DogeChat ASCII art header in bright yellow."""
    print("\033[38;5;226m")  # Bright yellow (#FFCE00)
    print("          /##                                         ##\\                  ##\\")
    print("         | ##                                         ## |                 ## |")
    print("     /####### /#######\\  ######\\  /#######\\  #######\\ #######\\   ######\\ ######\\")
    print("    /##__  ##/## | |## \\##  __##\\ ## | |## \\##  _____|##  __##\\  \\____##\\_##  _|")
    print("   | ##   |##|## | |## |## |  ## |## |_|##_/## /      ## |  ## | ####### | ## |")
    print("   | ##   |##|## |_|## |## |  ## |##|______ ## |      ## |  ## |##  __## | ## |##\\")
    print("   |  #######\\######## /######## |######## |\\#######\\ ## |  ## |\\####### | \\####  |")
    print("    \\_______/ \\_______/ \\____ ## |\\_______/  \\_______|\\__|  \\__| \\_______|  \\____/")
    print("                        __    ## |")
    print("                       |##|   ## |")
    print("                       |######## |")
    print("                        \\_______/")
    print("\033[0m")

# Call header at startup (remove if calling from main script)
display_header()

@dataclass
class ChatMode:
    """Base class for chat modes"""
    pass

@dataclass
class Public(ChatMode):
    """Public chat mode"""
    pass

@dataclass
class Channel(ChatMode):
    """Channel chat mode"""
    name: str

@dataclass
class PrivateDM(ChatMode):
    """Private DM mode"""
    nickname: str
    peer_id: str

class ChatContext:
    def __init__(self):
        self.current_mode: ChatMode = Public()
        self.active_channels: List[str] = []
        self.active_dms: Dict[str, str] = {}  # nickname -> peer_id
        self.last_private_sender: Optional[Tuple[str, str]] = None
    
    def format_prompt(self) -> str:
        if isinstance(self.current_mode, Public):
            return "[Public]"
        elif isinstance(self.current_mode, Channel):
            return f"[{self.current_mode.name}]"
        elif isinstance(self.current_mode, PrivateDM):
            return f"[DM: {self.current_mode.nickname}]"
        return ">"
    
    def get_status_line(self) -> str:
        parts = ["[1] Public"]
        
        for i, channel in enumerate(self.active_channels):
            parts.append(f"[{i + 2}] {channel}")
        
        dm_start = 2 + len(self.active_channels)
        for i, (nick, _) in enumerate(self.active_dms.items()):
            parts.append(f"[{i + dm_start}] DM:{nick}")
        
        return f"\033[90mActive: {' '.join(parts)}\033[0m"  # Grey for dimmed text
    
    def switch_to_number(self, num: int) -> bool:
        if num == 1:
            self.current_mode = Public()
            print("\033[90m─────────────────────────\033[0m")  # Grey separator
            print("\033[90m» Switched to Public chat. Just type to send messages.\033[0m")
            return True
        
        channel_end = 1 + len(self.active_channels)
        if 1 < num <= channel_end:
            channel_idx = num - 2
            if channel_idx < len(self.active_channels):
                channel = self.active_channels[channel_idx]
                self.current_mode = Channel(channel)
                print("\033[90m─────────────────────────\033[0m")  # Grey separator
                print(f"\033[90m» Switched to channel {channel}\033[0m")
                return True
        
        dm_start = channel_end + 1
        dm_idx = num - dm_start
        dm_list = list(self.active_dms.items())
        if dm_idx < len(dm_list):
            nick, peer_id = dm_list[dm_idx]
            self.current_mode = PrivateDM(nick, peer_id)
            print("\033[90m─────────────────────────\033[0m")  # Grey separator
            print(f"\033[90m» Switched to DM with {nick}. Just type to send messages.\033[0m")
            return True
        
        return False
    
    def add_channel(self, channel: str):
        if channel not in self.active_channels:
            self.active_channels.append(channel)
    
    def add_dm(self, nickname: str, peer_id: str):
        self.active_dms[nickname] = peer_id
    
    def enter_dm_mode(self, nickname: str, peer_id: str):
        self.add_dm(nickname, peer_id)
        self.current_mode = PrivateDM(nickname, peer_id)
        print("\033[90m─────────────────────────\033[0m")  # Grey separator
        print(f"\033[90m» Entered DM mode with {nickname}. Just type to send messages.\033[0m")
    
    def switch_to_channel(self, channel: str):
        self.add_channel(channel)
        self.current_mode = Channel(channel)
        print("\033[90m─────────────────────────\033[0m")  # Grey separator
        print(f"\033[90m» Switched to channel {channel}\033[0m")
    
    def switch_to_channel_silent(self, channel: str):
        self.add_channel(channel)
        self.current_mode = Channel(channel)
    
    def switch_to_public(self):
        self.current_mode = Public()
        print("\033[90m─────────────────────────\033[0m")  # Grey separator
        print("\033[90m» Switched to Public chat. Just type to send messages.\033[0m")
    
    def remove_channel(self, channel: str):
        if channel in self.active_channels:
            self.active_channels.remove(channel)
    
    def show_conversation_list(self):
        print("\n\033[90m╭─── Active Conversations ───╮\033[0m")  # Grey box
        print("\033[90m│                            │\033[0m")
        
        # Public
        indicator = "→" if isinstance(self.current_mode, Public) else " "
        print(f"\033[90m│ {indicator} [1] Public              │\033[0m")
        
        # Channels
        num = 2
        for channel in self.active_channels:
            is_current = isinstance(self.current_mode, Channel) and self.current_mode.name == channel
            indicator = "→" if is_current else " "
            padding = " " * (18 - len(channel))
            print(f"\033[90m│ {indicator} [{num}] {channel}{padding}│\033[0m")
            num += 1
        
        # DMs
        for nick, _ in self.active_dms.items():
            is_current = isinstance(self.current_mode, PrivateDM) and self.current_mode.nickname == nick
            indicator = "→" if is_current else " "
            dm_text = f"DM: {nick}"
            padding = " " * (18 - len(dm_text))
            print(f"\033[90m│ {indicator} [{num}] {dm_text}{padding}│\033[0m")
            num += 1
        
        print("\033[90m│                            │\033[0m")
        print("\033[90m╰────────────────────────────╯\033[0m")
    
    def get_conversation_list_with_numbers(self) -> str:
        output = "\033[90m╭─── Select Conversation ───╮\n\033[0m"  # Grey box
        
        # Public
        output += "\033[90m│  1. Public                │\n\033[0m"
        
        # Channels
        num = 2
        for channel in self.active_channels:
            padding = " " * (20 - len(channel))
            output += f"\033[90m│  {num}. {channel}{padding}│\n\033[0m"
            num += 1
        
        # DMs
        for nick, _ in self.active_dms.items():
            dm_text = f"DM: {nick}"
            padding = " " * (20 - len(dm_text))
            output += f"\033[90m│  {num}. {dm_text}{padding}│\n\033[0m"
            num += 1
        
        output += "\033[90m╰───────────────────────────╯\033[0m"
        return output

def format_message_display(
    timestamp: datetime,
    sender: str,
    content: str,
    is_private: bool,
    is_channel: bool,
    channel_name: Optional[str],
    recipient: Optional[str],
    my_nickname: str
) -> str:
    """Format a message for display"""
    time_str = timestamp.strftime("%H:%M")
    
    if is_private:
        # Light yellow (#FFF8DC) for all private messages
        if sender == my_nickname:
            # Message I sent
            if recipient:
                return f"\033[2;38;5;230m[{time_str}|DM]\033[0m \033[38;5;230m<you → {recipient}>\033[0m {content}"
            else:
                return f"\033[2;38;5;230m[{time_str}|DM]\033[0m \033[38;5;230m<you → ???>\033[0m {content}"
        else:
            # Message I received
            return f"\033[2;38;5;230m[{time_str}|DM]\033[0m \033[38;5;230m<{sender} → you>\033[0m {content}"
    elif is_channel:
        # Gold yellow (#FFD700) for channel messages
        if sender == my_nickname:
            # My messages
            if channel_name:
                return f"\033[2;38;5;220m[{time_str}|{channel_name}]\033[0m \033[38;5;220m<{sender} @ {channel_name}>\033[0m {content}"
            else:
                return f"\033[2;38;5;220m[{time_str}|Ch]\033[0m \033[38;5;220m<{sender} @ ???>\033[0m {content}"
        else:
            # Other users
            if channel_name:
                return f"\033[2;38;5;220m[{time_str}|{channel_name}]\033[0m \033[38;5;220m<{sender} @ {channel_name}>\033[0m {content}"
            else:
                return f"\033[2;38;5;220m[{time_str}|Ch]\033[0m \033[38;5;220m<{sender} @ ???>\033[0m {content}"
    else:
        # Bright yellow (#FFCE00) for public messages
        if sender == my_nickname:
            # My messages
            return f"\033[2;38;5;226m[{time_str}]\033[0m \033[38;5;226m<{sender}>\033[0m {content}"
        else:
            # Other users
            return f"\033[2;38;5;226m[{time_str}]\033[0m \033[38;5;226m<{sender}>\033[0m {content}"

def print_help():
    """Print help menu"""
    print("\n\033[38;5;226m━━━ Dogechat Commands ━━━\033[0m\n")
    
    # General
    print("\033[38;5;220m▶ General\033[0m")
    print("  \033[38;5;226m/help\033[0m         Show this help menu")
    print("  \033[38;5;226m/name\033[0m \033[90m<name>\033[0m  Change your nickname")
    print("  \033[38;5;226m/status\033[0m       Show connection info")
    print("  \033[38;5;226m/clear\033[0m        Clear the screen")
    print("  \033[38;5;226m/exit\033[0m         Quit Dogechat\n")
    
    # Navigation
    print("\033[38;5;220m▶ Navigation\033[0m")
    print("  \033[38;5;226m1-9\033[0m           Quick switch to conversation")
    print("  \033[38;5;226m/list\033[0m         Show all conversations")
    print("  \033[38;5;226m/switch\033[0m       Interactive conversation switcher")
    print("  \033[38;5;226m/public\033[0m       Go to public chat\n")
    
    # Messaging
    print("\033[38;5;220m▶ Messaging\033[0m")
    print("  \033[90m(type normally to send in current mode)\033[0m")
    print("  \033[38;5;226m/dm\033[0m \033[90m<name>\033[0m    Start private conversation")
    print("  \033[38;5;226m/dm\033[0m \033[90m<name> <msg>\033[0m Send quick private message")
    print("  \033[38;5;226m/reply\033[0m        Reply to last private message\n")
    
    # Channels
    print("\033[38;5;220m▶ Channels\033[0m")
    print("  \033[38;5;226m/j\033[0m \033[90m#channel\033[0m   Join or create a channel")
    print("  \033[38;5;226m/j\033[0m \033[90m#channel <password>\033[0m Join with password")
    print("  \033[38;5;226m/leave\033[0m        Leave current channel")
    print("  \033[38;5;226m/pass\033[0m \033[90m<pwd>\033[0m   Set channel password (owner only)")
    print("  \033[38;5;226m/transfer\033[0m \033[90m@user\033[0m Transfer ownership (owner only)\n")
    
    # Discovery
    print("\033[38;5;220m▶ Discovery\033[0m")
    print("  \033[38;5;226m/channels\033[0m     List all discovered channels")
    print("  \033[38;5;226m/online\033[0m       Show who's online")
    print("  \033[38;5;226m/w\033[0m            Alias for /online\n")
    
    # Privacy & Security
    print("\033[38;5;220m▶ Privacy & Security\033[0m")
    print("  \033[38;5;226m/block\033[0m \033[90m@user\033[0m  Block a user")
    print("  \033[38;5;226m/block\033[0m        List blocked users")
    print("  \033[38;5;226m/unblock\033[0m \033[90m@user\033[0m Unblock a user\n")
    
    print("\033[38;5;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def clear_screen():
    """Clear the terminal screen"""
    print("\033[2J\033[1;1H", end='')

# Export classes
__all__ = ['ChatMode', 'Public', 'Channel', 'PrivateDM', 'ChatContext', 'format_message_display', 'print_help', 'clear_screen']
