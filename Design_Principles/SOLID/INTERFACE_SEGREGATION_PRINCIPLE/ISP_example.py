"""
    Let's consider a scenario where we have a media player application that supports
    different types of media files, such as audio files (MP3, WAV) and video files (MP4, AVI).
"""

class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self, audio_file):
        raise NotImplementedError

    def manage_volume(self, audio_file):
        raise NotImplementedError

    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self, video_file):
        raise NotImplementedError

    def increase_video_brightness(self, brightness):
        raise NotImplementedError

"""
    In the above case whichever class is implementing the interface MediaPlayer
    had to implement all of these methods despite they need these or not. 
    
    An audio player doesn't care about increase in video brightness, 
    A video player doesn't care about the stopping of video.
    
    So that's why it's important to see that audio player & video player functionalities
    are implementing the functions that they didn't need. 
      
"""

"""
    So we can make separate interfaces for audio and video players 
"""

class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self, audio_file):
        raise NotImplementedError

    def manage_volume(self, audio_file):
        raise NotImplementedError

class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self, video_file):
        raise NotImplementedError

    def increase_video_brightness(self, brightness):
        raise NotImplementedError


class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        print(f"playing {audio_file}")

    def stop_audio(self, audio_file):
        print(f"stopping {audio_file}")

    def manage_volume(self, audio_file):
        print(f"managing volume of {audio_file}")

class MP4Player(videoPlayer):
    def play_video(self, video_file):
        print(f"playing {video_file}")

    def stop_video(self, video_file):
        print(f"stopping {video_file}")

    def manage_volume(self, video_file):
        print(f"managing volume of {video_file}")

"""if need to use both """

class MultiMediaPlayer(MP3Player, MP4Player):
    def play_audio(self, audio_file):
        print(f"playing {audio_file}")

    def stop_audio(self, audio_file):
        print(f"stopping {audio_file}")

    def manage_volume(self, audio_file):
        print(f"managing volume of {audio_file}")

    def play_video(self, video_file):
        print(f"playing {video_file}")

    def stop_video(self, video_file):
        print(f"stopping {video_file}")

    def manage_volume(self, video_file):
        print(f"managing volume of {video_file}")


"""
    class that needs to implement both MP3Player and MP4Player, 
    can implement as above. 
"""
