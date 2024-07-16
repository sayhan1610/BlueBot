# BlueBot

### Description:

BlueBot is a versatile Discord bot that offers various functionalities including moderation, entertainment, and utility features.

### Requirements:

- Python (Version 3.6.11 or higher)
- Required Python libraries:
  - discord.py
  - akinator
  - youtube_dl

### Installation:

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/BlueBot.git
   cd BlueBot
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Set up configuration:**

   - Replace `"token_here"` in `main.py` with your actual bot token.
   - Replace IDs (`log_channel_id`, `welcome_channel_id`, `leave_channel_id`, `confession_channel_id`) with your respective channel IDs.

4. **Run the bot:**
   ```
   python main.py
   ```

### Bot Commands:

- **/ping**: Test the bot's ping.
- **/say <message>**: Make the bot say something in the channel.
- **/confess <confession>**: Make an anonymous confession in the designated channel.
- **/uptime**: Check how long the bot has been running.
- **/server_stats**: Display server statistics.
- **/akinator**: Play the Akinator game.
- **/play <YouTube URL>**: Play a YouTube video/audio in the voice channel.
- **/stop**: Stop playing audio in the voice channel.

### Support:

For any issues, questions, or suggestions regarding BlueBot, please join our Discord server:
[Your Discord Server Invite Link](https://discord.gg/your-server-invite)

### Additional Notes:

- Ensure BlueBot has necessary permissions (like managing messages, connecting to voice channels, etc.).
- Customize BlueBot's behavior and commands to suit your server's needs.

Feel free to expand this `README.md` with more details or specific setup instructions as needed!
